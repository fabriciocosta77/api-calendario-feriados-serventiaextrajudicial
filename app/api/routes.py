from fastapi import APIRouter
from app.services.pdf_service import extract_holidays
from app.core.config import settings

router = APIRouter()

@router.get("/")
def get_holidays():
    return extract_holidays(settings.PDF_PATH)