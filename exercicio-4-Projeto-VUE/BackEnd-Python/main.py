from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # sem essa importação política de CORS nao permite conexao de um localhost diferente
from db.conn import connection
import utils.utils as utils 

app = FastAPI()

app.add_middleware( #parametros pra liberar a conexao
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def executar_consulta(query):
    if connection is None:
        return "Nao existem dados a serem procurados"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


resultados = executar_consulta("SELECT * FROM operadoras_ativas;")
@app.get('/buscar/{input}')
def buscar(input : str):  
    return utils.buscar(input , resultados)

@app.get('/')
def buscar_todos():  
    return resultados


# python -m uvicorn main:app --reload