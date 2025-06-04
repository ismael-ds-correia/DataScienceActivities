import asyncio
import json
import os
from pathlib import Path
from playwright.async_api import async_playwright

async def fetch_performance_with_playwright(team_id, team_slug, output_path):
    """
    1. Abre um browser headless
    2. Monitora as requisições de rede até encontrar /performance
    3. Extrai o JSON da resposta e salva em arquivo
    """
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/134.0.0.0 Safari/537.36"
            )
        )
        page = await context.new_page()
        performance_data = None

        # Registra um callback para cada resposta de rede:
        async def handle_response(response):
            url = response.url
            if f"/api/v1/team/{team_id}/performance" in url:
                try:
                    performance_data_raw = await response.json()
                    # Pode vir em duas chamadas: sem e com ?_=
                    performance_data = performance_data_raw
                    # Salvamos imediatamente (mas ainda queremos fechar a página depois)
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    with open(output_path, "w", encoding="utf-8") as f:
                        json.dump(performance_data, f, ensure_ascii=False, indent=4)
                    print(f"✓ JSON salvo em: {output_path}")
                except Exception as e:
                    print(f"✗ Erro ao ler JSON da resposta: {e}")

        page.on("response", handle_response)

        # Acesse a página do time para que ela dispare a chamada /performance
        team_url = f"https://www.sofascore.com/pt/time/futebol/{team_slug}/{team_id}"
        await page.goto(team_url)
        # Aguardar um pouco (ou até a resposta ser capturada)
        await page.wait_for_timeout(5000)  # 5 segundos

        await browser.close()

async def main():
    base_dir = Path("json/performance")
    os.makedirs(base_dir, exist_ok=True)

    teams = {
        "lyon": {
            "team_id": 1649,
            "slug": "olympique-lyonnais",
            "filename": "lyon-performance.json"
        },
        "psg": {
            "team_id": 1644,
            "slug": "paris-saint-germain",
            "filename": "psg-performance.json"
        }
    }

    for team_name, info in teams.items():
        team_id = info["team_id"]
        slug = info["slug"]
        output_path = base_dir / info["filename"]
        print(f"\n📥 Baixando performance do {team_name.upper()} (ID={team_id})…")
        await fetch_performance_with_playwright(team_id, slug, str(output_path))

if __name__ == "__main__":
    asyncio.run(main())
