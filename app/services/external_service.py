import httpx

async def fetch_post(post_id: int):
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        response.raise_for_status()
        return response.json()
