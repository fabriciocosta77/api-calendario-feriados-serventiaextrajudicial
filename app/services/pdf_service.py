import pdfplumber
import re

MESES = {
    "JANEIRO": 1,
    "FEVEREIRO": 2,
    "MARÇO": 3,
    "ABRIL": 4,
    "MAIO": 5,
    "JUNHO": 6,
    "JULHO": 7,
    "AGOSTO": 8,
    "SETEMBRO": 9,
    "OUTUBRO": 10,
    "NOVEMBRO": 11,
    "DEZEMBRO": 12,
}


def extract_holidays(pdf_path: str):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            page = pdf.pages[2]
            text = page.extract_text()

        raw_lines = [l.strip() for l in text.split("\n") if l.strip()]

        lines = []
        for line in raw_lines:
            if (
                lines
                and not re.match(r"^\d{1,2}", line)
                and not any(m in line for m in MESES)
            ):
                lines[-1] += " " + line
            else:
                lines.append(line)

        resultados = []
        mes_atual = None

        for line in lines:
            match_full = re.match(
                r"(JANEIRO|FEVEREIRO|MARÇO|ABRIL|MAIO|JUNHO|JULHO|AGOSTO|SETEMBRO|OUTUBRO|NOVEMBRO|DEZEMBRO)\s+(\d{1,2})º?\s*\(.*?\)\s*(.+)",
                line
            )

            if match_full:
                mes_atual = MESES[match_full.group(1)]
                dia = int(match_full.group(2))
                descricao = match_full.group(3)

                resultados.append({
                    "dia": dia,
                    "mes": mes_atual,
                    "descricao": descricao.strip()
                })
                continue

            for mes_nome in MESES:
                if mes_nome in line:
                    mes_atual = MESES[mes_nome]
                    break

            if re.match(r"^\d{1,2}\s*\(", line):

                dia = extrair_dia(line)

                descricao = re.sub(
                    r"^\d{1,2}º?\s*\(.*?\)\s*",
                    "",
                    line
                )

                resultados.append({
                    "dia": dia,
                    "mes": mes_atual,
                    "descricao": normalizar_descricao(descricao)
                })

    except Exception as e:
        raise ValueError(f"Erro encontrado: {e}")
    else:
        return resultados

def extrair_dia(texto):
    texto = texto.replace("º", "").replace(".", "/")
    match = re.match(r"(\d{1,2})", texto)
    return int(match.group(1)) if match else None

def normalizar_descricao(texto: str) -> str:
    texto = re.sub(r"\(", " (", texto)
    texto = re.sub(r"([a-záéíóúãõç])([A-Z])", r"\1 \2", texto)
    texto = re.sub(r"([a-záéíóúãõç])([A-ZÁÉÍÓÚÃÕÇ])", r"\1 \2", texto)
    texto = re.sub(r"([a-záéíóúãõç])([A-ZÁÉÍÓÚÃÕÇ])", r"\1 \2", texto)
    texto = re.sub(r"\s+", " ", texto)

    return texto.strip()