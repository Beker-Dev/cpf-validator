from cpf_validator import search_cpf
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def main():
    return {'message': 'call this endpoint -> (/validate-cpf/<YOUR_CPF>) with GET method'}


@app.get('/validate-cpf/{cpf}')
def validate_cpf(cpf: str):
    result = search_cpf(cpf)
    message = 'VALID CPF' if result else 'INVALID CPF'
    return {'status': 200, 'cpf': cpf, 'is_valid': result, 'message': message, 'github': 'https://github.com/Beker-Dev'}

