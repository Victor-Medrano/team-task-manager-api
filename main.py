

from fastapi import FastAPI


app = FastAPI(title="Task-manager")


@app.get("/")
def home():
    return {"message": "Hola mundo"}
