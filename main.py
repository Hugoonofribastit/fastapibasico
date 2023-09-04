from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial:Optional[str]

#http://http://127.0.0.1:8000/

@app.get("/")
def index():
    return {"message":"Hola, Fastapieros"}


""" uvicorn main:app --reload    EN CONSOLA PARA LAVANTAR Y EL RELOAD PARA NO LEVANTAR EL SV CADA CAMBIO QUE HACEMOS, QUEDA ESCUCHANDO"""

@app.get("/libros/{id}")
def mostrar_libro(id : int):
    return {"data":id}

@app.post("/libros")
def insertar_libro(libro: Libro):
    return {"message": f"libro {libro.titulo} insertado"}