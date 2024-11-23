import joblib

def classify_comment(comentario):
    model = joblib.load("modelo_comentarios.pkl")
    
    categoria = model.predict([comentario])
    return categoria[0]

if __name__ == "__main__":
    comentario = input("Digite um comentário: ")
    categoria = classify_comment(comentario)
    print(f"O comentário é: {categoria}")
