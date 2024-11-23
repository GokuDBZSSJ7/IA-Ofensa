import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_model():
    df = pd.read_csv("comentarios.csv")
    
    X = df["comentario"]
    y = df["categoria"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print(f"Acurácia: {accuracy_score(y_test, y_pred)}")
    print(f"Relatório de classificação:\n{classification_report(y_test, y_pred)}")
    
    joblib.dump(model, "modelo_comentarios.pkl")
    
if __name__ == "__main__":
    train_model()
