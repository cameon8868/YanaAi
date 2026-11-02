import base64
import os

import aiohttp
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_ID = os.getenv("CLOUDINARY_CLOUD_ID")
API_TOKEN = os.getenv("CLOUDINARY_API_TOKEN")

MODEL = "@cf/black-forest-labs/flux-1-schnell"
URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/{MODEL}"

async def generate_image(prompt: str) -> bytes:
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload = {"prompt": prompt, "steps": 4}

    async with aiohttp.ClientSession() as session:
        async with session.post(URL, json=payload, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                image_base64 = data["result"]["image"]
                return base64.b64decode(image_base64)
            else:
                raise Exception(f"Error generating image: {response.status} - {await response.text()}")