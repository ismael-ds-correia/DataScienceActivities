import asyncio
import json
import time
from pathlib import Path
from playwright.async_api import async_playwright

async def get_rounds(page, base_url, tournament_id, season_id):
    """Obtém todas as rodadas da temporada"""
    url = f"{base_url}/api/v1/unique-tournament/{tournament_id}/season/{season_id}/rounds"
    await page.goto(f"{base_url}/pt/torneio/futebol/france/ligue-1/{tournament_id}")
    await page.wait_for_timeout(1000)
    
    response_text = await page.evaluate(f"""
        async () => {{
            const response = await fetch("{url}");
            return await response.text();
        }}
    """)
    
    data = json.loads(response_text)
    print("Chaves na resposta da API:", list(data.keys()))
    
    # Adaptação para diferentes estruturas de resposta
    if 'rounds' in data:
        rounds_data = data['rounds']
    elif 'uniqueTournamentSeasonRounds' in data:
        rounds_data = data['uniqueTournamentSeasonRounds']['rounds']
    else:
        print("Estrutura da API mudou!")
        with open("api_debug_rounds.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Resposta da API salva em api_debug_rounds.json para análise")
        return []
        
    # Filtra rodadas válidas (ignora qualificações e finais)
    rounds = [r['round'] for r in rounds_data 
              if isinstance(r.get('round'), int) and r['round'] <= 34]
    return sorted(set(rounds))

async def get_events_for_round(page, base_url, tournament_id, season_id, round_number):
    """Obtém todos os jogos de uma rodada"""
    url = f"{base_url}/api/v1/unique-tournament/{tournament_id}/season/{season_id}/events/round/{round_number}"
    
    response_text = await page.evaluate(f"""
        async () => {{
            const response = await fetch("{url}");
            return await response.text();
        }}
    """)
    
    data = json.loads(response_text)
    return data.get('events', [])

async def get_statistics_for_event(page, base_url, event_id):
    """Obtém estatísticas de um jogo específico"""
    url = f"{base_url}/api/v1/event/{event_id}/statistics"
    
    try:
        response_text = await page.evaluate(f"""
            async () => {{
                const response = await fetch("{url}");
                return await response.text();
            }}
        """)
        
        data = json.loads(response_text)
        return data
    except Exception as e:
        print(f"  ⚠️ Erro ao obter estatísticas (ID {event_id}): {e}")
        return None

async def scrape_team_data(team_name, tournament_id, season_id, output_file=None, base_url="https://www.sofascore.com"):
    """Coleta todos os jogos de um time em uma liga específica"""
    if output_file is None:
        team_slug = team_name.replace(" ", "_").lower()
        output_file = f"{team_slug}_{tournament_id}_{season_id}.json"
    
    all_stats = []
    
    async with async_playwright() as p:
        # Inicia o navegador
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # Obtém rodadas
        print(f"📋 Obtendo rodadas do torneio {tournament_id}...")
        rounds = await get_rounds(page, base_url, tournament_id, season_id)
        
        if not rounds:
            print("❌ Não foi possível obter as rodadas.")
            await browser.close()
            return
            
        print(f"✅ Rodadas encontradas: {rounds}")
        
        # Itera por cada rodada
        for round_number in rounds:
            print(f"\n🔍 Buscando jogos da rodada {round_number}...")
            events = await get_events_for_round(page, base_url, tournament_id, season_id, round_number)
            
            if not events:
                print(f"⚠️ Nenhum jogo encontrado na rodada {round_number}")
                continue
                
            # Filtra apenas jogos do time especificado
            team_events = [e for e in events 
                           if e['homeTeam']['name'] == team_name 
                           or e['awayTeam']['name'] == team_name]
            
            if not team_events:
                print(f"ℹ️ Nenhum jogo do {team_name} na rodada {round_number}")
                continue
            
            print(f"📊 Encontrado(s) {len(team_events)} jogo(s) do {team_name} na rodada {round_number}")
            
            # Coleta estatísticas de cada jogo do time
            for event in team_events:
                event_id = event['id']
                home = event['homeTeam']['name']
                away = event['awayTeam']['name']
                
                # Adiciona informações básicas do jogo
                match_data = {
                    "event_id": event_id,
                    "home": home,
                    "away": away,
                    "round": round_number,
                    "date": event.get('startTimestamp'),
                    "status": event.get('status', {}).get('description', 'Agendado')
                }
                
                # Adiciona placar do jogo (se disponível)
                if 'homeScore' in event and 'awayScore' in event:
                    match_data["homeScore"] = event['homeScore']
                    match_data["awayScore"] = event['awayScore']
                else:
                    match_data["homeScore"] = {"current": 0}
                    match_data["awayScore"] = {"current": 0}
                
                # Verifica se o jogo já aconteceu ou está em andamento
                if event.get('status', {}).get('type') in ['finished', 'inprogress']:
                    print(f"  📈 Coletando estatísticas: {home} vs {away} (ID: {event_id})...")
                    stats = await get_statistics_for_event(page, base_url, event_id)
                    
                    if stats:
                        match_data["statistics"] = stats
                        print(f"  ✅ Estatísticas coletadas com sucesso")
                    else:
                        print(f"  ⚠️ Sem estatísticas disponíveis")
                else:
                    print(f"  ⏳ Jogo agendado (sem estatísticas): {home} vs {away}")
                
                all_stats.append(match_data)
                await page.wait_for_timeout(1000)  # Pausa para evitar bloqueio
        
        await browser.close()
    
    # Salva os dados coletados
    if all_stats:
        Path(output_file).parent.mkdir(exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(all_stats, f, ensure_ascii=False, indent=2)
        print(f"\n🎉 Coleta finalizada! {len(all_stats)} jogos do {team_name} salvos em {output_file}")
    else:
        print("\n❌ Nenhum dado coletado.")

async def main():
    # Array de times para scraping - cada item é uma tupla (time, torneio, temporada)
    teams_to_scrape = [
        ("Paris Saint-Germain", 34, 61736),  # PSG na Ligue 1 2024/25
        ("Olympique Lyonnais", 34, 61736)    # Lyon na Ligue 1 2024/25
    ]

    # Executa o scraping para cada time na lista
    for team_name, tournament_id, season_id in teams_to_scrape:
        print(f"\n==== Iniciando coleta para: {team_name} ====")
        await scrape_team_data(team_name, tournament_id, season_id)
        print(f"==== Coleta finalizada para: {team_name} ====\n")
    

if __name__ == "__main__":
    asyncio.run(main())