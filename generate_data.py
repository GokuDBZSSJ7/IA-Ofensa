import pandas as pd
import random

def generate_data():
    comentarios_aceitaveis = [
        "Ótimo trabalho!",
        "Parabéns pelo seu esforço!",
        "Continue assim, você está indo muito bem.",
    ]
    
    comentarios_ofensivos = [
        "Você é um idiota.",
        "Ninguém gosta de você.",
        "Seu trabalho é péssimo.",
    ]
    
    comentarios_discurso_de_odio = [
        "Vocês deveriam ser todos exterminados.",
        "O mundo seria melhor sem essa raça.",
        "Esses imigrantes só trazem problemas.",
    ]
    
    data = []
    
    for comentario in comentarios_aceitaveis:
        data.append([comentario, "aceitável"])
    
    for comentario in comentarios_ofensivos:
        data.append([comentario, "ofensivo"])
    
    for comentario in comentarios_discurso_de_odio:
        data.append([comentario, "discurso de ódio"])
    
    for i in range(100):
        comentario_aceitavel = random.choice(comentarios_aceitaveis)
        comentario_ofensivo = random.choice(comentarios_ofensivos)
        comentario_discurso_de_odio = random.choice(comentarios_discurso_de_odio)
        
        data.append([comentario_aceitavel, "aceitável"])
        data.append([comentario_ofensivo, "ofensivo"])
        data.append([comentario_discurso_de_odio, "discurso de ódio"])
    
    df = pd.DataFrame(data, columns=["comentario", "categoria"])
    df.to_csv("comentarios.csv", index=False)
    
if __name__ == "__main__":
    generate_data()
