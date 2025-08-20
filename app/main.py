from fastapi import FastAPI
import pickle
from pydantic import BaseModel

app = FastAPI()
model, vectorizer = pickle.load(open("app/model.pkl", "rb"))

class Item(BaseModel):
    text: str

@app.post("/predict")
def predict(item: Item):
    X = vectorizer.transform([item.text])
    prediction = model.predict(X)[0]
    return {"prediction": prediction}
