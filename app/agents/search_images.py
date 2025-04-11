import requests
import os

class BuscaImagem:
    def executar(self, nome):
        SERPAPI_KEY = os.getenv("SERPAPI_KEY", "")
        url = "https://serpapi.com/search.json"
        params = {"q": f"{nome} site:instagram.com", "tbm": "isch", "api_key": SERPAPI_KEY}
        response = requests.get(url, params=params)
        data = response.json()
        return [img["thumbnail"] for img in data.get("images_results", [])[:3]]
