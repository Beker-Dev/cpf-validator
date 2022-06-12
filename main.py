from cpf_validator import search_cpf
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def main():
    return {'message': 'call this endpoint -> (/validate-cpf/<YOUR_CPF>) with GET method'}


@app.get('/validate-cpf/{cpf}')
def validate_cpf(cpf: str):
    result = search_cpf(cpf)
    return {'status': 200, 'cpf': cpf, 'message': result, 'github': 'https://github.com/Beker-Dev'}

