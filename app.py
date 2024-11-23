from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("modelo_comentarios.pkl")

@app.route('/classify', methods=['POST'])
def classify_comment():
    data = request.json
    comentario = data.get("comentario", "")
    
    categoria = model.predict([comentario])[0]
    
    return jsonify({"comentario": comentario, "categoria": categoria})

if __name__ == "__main__":
    app.run(port=7000)
