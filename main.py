from fastapi import FastAPI, HTTPException, Request
from contextlib import asynccontextmanager
from app.services.pdf_service import extract_holidays
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        app.state.holidays_cache = extract_holidays(settings.PDF_PATH)
        print("Feriados carregados com sucesso")
    except Exception as e:
        print(f"Erro ao carregar feriados: {e}")
        app.state.holidays_cache = []

    yield
    print("Encerrando aplicação")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def get_holidays(request: Request):
    try:
        return request.app.state.holidays_cache
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))