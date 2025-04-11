from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import requests
from io import BytesIO

class AnalisaImagem:
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    def executar(self, url_img):
        try:
            raw_image = Image.open(BytesIO(requests.get(url_img).content)).convert('RGB')
            inputs = self.processor(raw_image, return_tensors="pt")
            out = self.model.generate(**inputs)
            legenda = self.processor.decode(out[0], skip_special_tokens=True)
            return {"descricao_imagem": legenda}
        except:
            return {"descricao_imagem": "Erro ao processar imagem"}
