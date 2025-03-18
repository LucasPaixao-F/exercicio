from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Minha API esta no ar!"}


@app.get("/soma")
def soma(a: int, b: int):
    return {"resultado": a + b}


# teste
