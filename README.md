# Sistema Multiagente IA para Coleta Pública de Dados

Este projeto é uma API construída com FastAPI que usa múltiplos agentes inteligentes para buscar e consolidar informações públicas de leads (nome e telefone), utilizando inteligência artificial.

---

## Funcionalidades

- Busca automática no Google usando SerpAPI
- Identificação de redes sociais (LinkedIn, Instagram, Facebook)
- Extração de menções públicas em sites e artigos
- Coleta de imagens públicas
- Análise de imagem com IA (BLIP da HuggingFace)
- Inferência de profissão com base em imagem e contexto textual
- Detecção de interesses a partir de imagem, nome e menções
- Armazenamento dos resultados em banco SQLite

---

## Tecnologias Utilizadas

- FastAPI
- Uvicorn
- Requests
- Pillow (PIL)
- HuggingFace Transformers
- BLIP Image Captioning
- SerpAPI
- SQLite

---

## Como Executar

1. Clonar o projeto e navegar até o diretório:

    git clone <repositorio>
    cd client_insights

2. Instalar as dependências:

    pip install -r requirements.txt

3. Definir a chave da SerpAPI:

    export SERPAPI_KEY="sua_chave_aqui"  (Linux/macOS)
    set SERPAPI_KEY="sua_chave_aqui"    (Windows)

4. Rodar o servidor:

    uvicorn app.main:app --reload

5. Acessar a documentação automática:

    http://localhost:8000/docs

---

## Exemplo de Consulta

Requisição:
http://localhost:8000/buscar?nome=Donald%20Trump&telefone=2024567041

Resposta:

{
  "nome": "Donald Trump",
  "telefone": "2024567041",
  "nome_completo": "Donald Trump",
  "profissao": "Presidente",
  "redes_sociais": {
    "instagram": "https://www.instagram.com/realdonaldtrump/?hl=en"
  },
  "interesses": [
    "política", "comunicação", "negócios"
  ],
  "mencoes": [
    "Donald Trump - https://en.wikipedia.org/wiki/Donald_Trump",
    "Donald J. Trump: Home - https://www.donaldjtrump.com/",
    "President Donald J. Trump - https://www.whitehouse.gov/administration/donald-j-trump/"
  ],
  "imagens": [
    "https://serpapi.com/searches/.../image1.jpeg",
    "https://serpapi.com/searches/.../image2.jpeg",
    "https://serpapi.com/searches/.../image3.jpeg"
  ],
  "inferencias": {
    "descricao_imagem": "a man in a suit"
  }
}

---

## Banco de Dados

- Nome: `clientes.db`
- Tipo: SQLite
- Armazena o histórico completo de buscas realizadas

---

## Licença

Este projeto é de uso livre para fins de estudo, validação técnica e testes em ambientes controlados.
