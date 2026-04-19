from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    PDF_PATH: str = ""

    def __init__(self, **values):
        super().__init__(**values)

        input_dir = BASE_DIR / "input"
        pdfs = list(input_dir.glob("*.pdf"))

        if not pdfs:
            raise FileNotFoundError("Nenhum PDF encontrado na pasta input")

        latest_pdf = max(pdfs, key=lambda p: p.stat().st_mtime)
        self.PDF_PATH = str(latest_pdf)


settings = Settings()