import pandas as pd
import json
import os
from pathlib import Path

# Definindo pastas
raw_data_folder = "raw_data"
processed_data_folder = "processed_data"

# Criando pastas se não existirem
Path(processed_data_folder).mkdir(exist_ok=True)

# Função para extrair estatísticas de um evento/partida
def extract_match_stats(match_data):
    """Extrai estatísticas relevantes de uma partida"""
    
    # Informações básicas da partida
    match_info = {
        "event_id": match_data["event_id"],
        "home_team": match_data["home"],
        "away_team": match_data["away"],
        "round": match_data["round"],
        "date": match_data["date"],
        "status": match_data["status"]
    }
    
    # Inicializa dicionário para estatísticas
    home_stats = {}
    away_stats = {}
    
    # Verifica se há estatísticas na partida
    if "statistics" in match_data and "statistics" in match_data["statistics"]:
        # Busca período "ALL" (toda a partida)
        for period in match_data["statistics"]["statistics"]:
            if period["period"] == "ALL":
                # Percorre grupos de estatísticas
                for group in period["groups"]:
                    for stat in group["statisticsItems"]:
                        # Estatísticas que queremos extrair
                        if stat["key"] in [
                            "totalShotsOnGoal",  # Total de chutes
                            "shotsOnGoal",       # Chutes no gol
                            "fouls",             # Faltas
                            "offsides",          # Impedimentos
                            "goalKicks",         # Tiros de meta
                            "throwIns",          # Laterais
                            "hitWoodwork",       # Bolas na trave
                            "yellowCards",       # Cartões amarelos
                            "redCards",          # Cartões vermelhos
                            "cornerKicks"        # Escanteios
                        ]:
                            # Extrai valores para casa e visitante
                            home_value = stat.get("homeValue", 0)
                            away_value = stat.get("awayValue", 0)
                            
                            home_stats[stat["key"]] = home_value
                            away_stats[stat["key"]] = away_value
    
    # Calcula total de cartões (amarelos + vermelhos)
    home_stats["totalCards"] = home_stats.get("yellowCards", 0) + home_stats.get("redCards", 0)
    away_stats["totalCards"] = away_stats.get("yellowCards", 0) + away_stats.get("redCards", 0)
    
    # Adiciona valores ausentes com 0
    for key in [
        "totalShotsOnGoal", "shotsOnGoal", "fouls", "offsides", 
        "goalKicks", "throwIns", "hitWoodwork", "yellowCards", 
        "redCards", "cornerKicks", "totalCards"
    ]:
        if key not in home_stats:
            home_stats[key] = 0
        if key not in away_stats:
            away_stats[key] = 0
    
    return match_info, home_stats, away_stats

# Lista para armazenar dados de todas as partidas
all_matches = []

# Processa todos os arquivos JSON na pasta raw_data
for json_file in Path(raw_data_folder).glob("*.json"):
    with open(json_file, "r", encoding="utf-8") as f:
        team_data = json.load(f)
        
        team_name = json_file.stem.split("_")[0]  # Extrai nome do time do arquivo
        
        # Processa cada partida
        for match in team_data:
            match_info, home_stats, away_stats = extract_match_stats(match)
            
            # Determina se o time focal é mandante ou visitante
            is_home = match_info["home_team"] == team_name
            
            # Configura time focal e adversário
            if is_home:
                team_role = "home"
                opponent = match_info["away_team"]
                team_stats = home_stats
                opponent_stats = away_stats
            else:
                team_role = "away"
                opponent = match_info["home_team"]
                team_stats = away_stats
                opponent_stats = home_stats
            
            # Cria um registro para esta partida
            match_record = {
                "team": team_name,
                "opponent": opponent,
                "home_away": team_role,
                "round": match_info["round"],
                "date": match_info["date"],
                "status": match_info["status"],
                
                # Estatísticas do time
                "total_shots": team_stats["totalShotsOnGoal"],
                "shots_on_target": team_stats["shotsOnGoal"],
                "fouls": team_stats["fouls"],
                "offsides": team_stats.get("offsides", 0),  # Alguns jogos podem não ter esta estatística
                "goal_kicks": team_stats["goalKicks"],
                "throw_ins": team_stats["throwIns"],
                "hit_woodwork": team_stats["hitWoodwork"],
                "yellow_cards": team_stats["yellowCards"],
                "red_cards": team_stats.get("redCards", 0),
                "total_cards": team_stats["totalCards"],
                "corners": team_stats["cornerKicks"],
                
                # Estatísticas do adversário
                "opp_total_shots": opponent_stats["totalShotsOnGoal"],
                "opp_shots_on_target": opponent_stats["shotsOnGoal"],
                "opp_fouls": opponent_stats["fouls"],
                "opp_offsides": opponent_stats.get("offsides", 0),
                "opp_goal_kicks": opponent_stats["goalKicks"],
                "opp_throw_ins": opponent_stats["throwIns"],
                "opp_hit_woodwork": opponent_stats["hitWoodwork"],
                "opp_yellow_cards": opponent_stats["yellowCards"],
                "opp_red_cards": opponent_stats.get("redCards", 0),
                "opp_total_cards": opponent_stats["totalCards"],
                "opp_corners": opponent_stats["cornerKicks"]
            }
            
            all_matches.append(match_record)

# Cria DataFrame com todas as partidas
df_matches = pd.DataFrame(all_matches)

# Converte timestamp para datetime legível
if not df_matches.empty and "date" in df_matches.columns:
    df_matches["date"] = pd.to_datetime(df_matches["date"], unit="s")

# Salva dados para cada time separadamente
for team in df_matches["team"].unique():
    team_df = df_matches[df_matches["team"] == team]
    output_file = f"{processed_data_folder}/{team.lower().replace(' ', '_')}_stats.csv"
    team_df.to_csv(output_file, index=False)
    print(f"Estatísticas de {team} salvas em: {output_file}")

# Salva dataset completo
all_teams_file = f"{processed_data_folder}/all_matches_stats.csv"
df_matches.to_csv(all_teams_file, index=False)
print(f"Dataset completo salvo em: {all_teams_file}")

print(f"Total de partidas processadas: {len(df_matches)}")