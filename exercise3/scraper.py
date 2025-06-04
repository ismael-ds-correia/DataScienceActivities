import asyncio
import json
import time
from pathlib import Path
from playwright.async_api import async_playwright

TOURNAMENT_ID = 34  # Ligue 1
SEASON_ID = 61736   # 2024/25
BASE_URL = "https://www.sofascore.com"
OUTPUT_FILE = "psg_ligue1_24_25.json"

async def get_rounds(page):
    """Obtém todas as rodadas da temporada"""
    url = f"{BASE_URL}/api/v1/unique-tournament/{TOURNAMENT_ID}/season/{SEASON_ID}/rounds"
    await page.goto(f"{BASE_URL}/pt/torneio/futebol/france/ligue-1/{TOURNAMENT_ID}")
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

async def get_events_for_round(page, round_number):
    """Obtém todos os jogos de uma rodada"""
    url = f"{BASE_URL}/api/v1/unique-tournament/{TOURNAMENT_ID}/season/{SEASON_ID}/events/round/{round_number}"
    
    response_text = await page.evaluate(f"""
        async () => {{
            const response = await fetch("{url}");
            return await response.text();
        }}
    """)
    
    data = json.loads(response_text)
    return data.get('events', [])

async def get_statistics_for_event(page, event_id):
    """Obtém estatísticas de um jogo específico"""
    url = f"{BASE_URL}/api/v1/event/{event_id}/statistics"
    
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

async def main():
    all_stats = []
    
    async with async_playwright() as p:
        # Inicia o navegador
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # Obtém rodadas
        print("📋 Obtendo rodadas da Ligue 1 24/25...")
        rounds = await get_rounds(page)
        
        if not rounds:
            print("❌ Não foi possível obter as rodadas.")
            await browser.close()
            return
            
        print(f"✅ Rodadas encontradas: {rounds}")
        
        # Itera por cada rodada
        for round_number in rounds:
            print(f"\n🔍 Buscando jogos da rodada {round_number}...")
            events = await get_events_for_round(page, round_number)
            
            if not events:
                print(f"⚠️ Nenhum jogo encontrado na rodada {round_number}")
                continue
                
            # Filtra apenas jogos do PSG
            psg_events = [e for e in events 
                         if e['homeTeam']['name'] == "Paris Saint-Germain" 
                         or e['awayTeam']['name'] == "Paris Saint-Germain"]
            
            if not psg_events:
                print(f"ℹ️ Nenhum jogo do PSG na rodada {round_number}")
                continue
            
            print(f"📊 Encontrado(s) {len(psg_events)} jogo(s) do PSG na rodada {round_number}")
            
            # Coleta estatísticas de cada jogo do PSG
            for event in psg_events:
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
                
                # Verifica se o jogo já aconteceu ou está em andamento
                if event.get('status', {}).get('type') in ['finished', 'inprogress']:
                    print(f"  📈 Coletando estatísticas: {home} vs {away} (ID: {event_id})...")
                    stats = await get_statistics_for_event(page, event_id)
                    
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
        Path(OUTPUT_FILE).parent.mkdir(exist_ok=True)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(all_stats, f, ensure_ascii=False, indent=2)
        print(f"\n🎉 Coleta finalizada! {len(all_stats)} jogos do PSG salvos em {OUTPUT_FILE}")
    else:
        print("\n❌ Nenhum dado coletado.")

if __name__ == "__main__":
    # Windows requer este ajuste para asyncio
    asyncio.run(main())