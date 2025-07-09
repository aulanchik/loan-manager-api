import httpx

async def get_country_code(ip: str) -> str:
    try:
        async with httpx.AsyncClient(follow_redirects=False) as client:
            r = await client.get(f"http://ip-api.com/json/{ip}", timeout=5)
            if r.status_code == 200:
                data = r.json()
                return data.get("countryCode", "GB")
    except Exception:
        pass
    return "GB"
