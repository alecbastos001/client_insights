import requests
import os

class BuscaGoogle:
    def executar(self, nome):
        SERPAPI_KEY = os.getenv("SERPAPI_KEY", "")
        url = "https://serpapi.com/search.json"
        params = {"q": nome, "api_key": SERPAPI_KEY, "num": 5}
        response = requests.get(url, params=params)
        data = response.json()

        mencoes = []
        redes_sociais = {}
        for r in data.get("organic_results", []):
            link = r.get("link", "")
            title = r.get("title", "")
            if "linkedin.com" in link:
                redes_sociais["linkedin"] = link
            elif "instagram.com" in link:
                redes_sociais["instagram"] = link
            elif "facebook.com" in link:
                redes_sociais["facebook"] = link
            else:
                mencoes.append(f"{title} - {link}")
        return redes_sociais, mencoes
