from fastapi import FastAPI, Query
from app.models import ClientePerfil
from app.database import init_db, insert_cliente
from app.agents.search_google import BuscaGoogle
from app.agents.search_images import BuscaImagem
from app.agents.analyze_image import AnalisaImagem

app = FastAPI()
init_db()

@app.get("/buscar", response_model=ClientePerfil)
def buscar(nome: str = Query(...), telefone: str = Query(...)):
    perfil = ClientePerfil(nome=nome, telefone=telefone)

    redes_sociais, mencoes = BuscaGoogle().executar(nome)
    imagens = BuscaImagem().executar(nome)

    interesses = []

    # 1. Interesses a partir de nome (mock)
    nome_lower = nome.lower()
    if "trump" in nome_lower:
        interesses.extend(["política", "negócios", "comunicação"])
    elif "beatriz" in nome_lower:
        interesses.extend(["moda", "saúde", "instagram"])
    elif "felipe" in nome_lower or "felipestin" in nome_lower:
        interesses.extend(["medicina", "fórmula 1", "marketing"])

    # 2. Análise de imagem com BLIP
    inferencias = None
    if imagens:
        analisador = AnalisaImagem()
        inferencias = analisador.executar(imagens[0])
    
        legenda = inferencias.get("descricao_imagem", "").lower()
    
        if "golf" in legenda:
            interesses.append("golfe")
        if "bike" in legenda or "cycling" in legenda:
            interesses.append("ciclismo")
        if "beach" in legenda:
            interesses.append("praia")
        if "gym" in legenda or "fitness" in legenda:
            interesses.append("academia")

    # 3. Extração de palavras das menções
    for mencao in mencoes:
        if "carros" in mencao.lower():
            interesses.append("carros")
        if "tecnologia" in mencao.lower():
            interesses.append("tecnologia")
        if "viagem" in mencao.lower() or "travel" in mencao.lower():
            interesses.append("viagens")
    
    # Remover duplicatas
    interesses = list(set(interesses))
    
    # Preencher no perfil final
    perfil.nome_completo = nome
    profissao = None
    
    # Modo 1: a partir das menções
    for mencao in mencoes:
        if "president" in mencao.lower():
            profissao = "Presidente"
            break
        elif "businessman" in mencao.lower():
            profissao = "Empresário"
        elif "doctor" in mencao.lower():
            profissao = "Médico"
        elif "engineer" in mencao.lower():
            profissao = "Engenheiro"
    
    # Modo 2: pela imagem
    if inferencias:
        desc = inferencias.get("descricao_imagem", "").lower()
        if "podium" in desc or "microphone" in desc:
            profissao = profissao or "Palestrante"
        elif "white coat" in desc:
            profissao = profissao or "Médico"
        elif "construction" in desc:
            profissao = profissao or "Engenheiro"
    
    # Modo 3: fallback
    if not profissao and "trump" in nome.lower():
        profissao = "Empresário e Político"
    
    perfil.profissao = profissao  # Usa o campo já existente
    perfil.redes_sociais = redes_sociais
    perfil.mencoes = mencoes
    perfil.imagens = imagens
    perfil.inferencias = inferencias
    perfil.interesses = interesses if interesses else None

    insert_cliente(perfil)
    return perfil
