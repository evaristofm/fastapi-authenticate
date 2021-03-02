# fastapi-authenticate
Implementando autenticação no FastAPI com banco de dados Tortoise-ORM 

# Como rodar o código?
git clone https://github.com/evaristofm/fastapi-authenticate.git
cd fastapi-authenticate
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --reload
