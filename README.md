# API de Feriados CNJ

API desenvolvida com **FastAPI** para extrair automaticamente os feriados do calendário forense a partir de um PDF oficial utilizando `pdfplumber`.

---

## Tecnologias utilizadas

* Python 3.10+
* FastAPI
* Uvicorn
* pdfplumber
* pandas (opcional, dependendo da versão)
* pydantic-settings

---

## Estrutura do projeto

```
.
├── app/
│   ├── core/
│   │   └── config.py
│   ├── services/
│   │   └── pdf_service.py
│   └── schemas/
│       └── holiday.py
├── input/
│   └── pdf/
│       └── arquivo.pdf
├── main.py
├── requirements.txt
└── README.md
```

---

## Como rodar o projeto pela primeira vez

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPO.git
cd SEU_REPO
```

---

### 2. Crie e ative um ambiente virtual

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Adicione o PDF

Coloque o arquivo PDF dentro da pasta:

```
input/pdf/
```

> A API irá automaticamente utilizar o primeiro PDF encontrado na pasta.

---

### 5. Execute a API

```bash
uvicorn main:app --reload
```

---

### 6. Acesse no navegador

* API:

```
http://127.0.0.1:8000/
```

* Documentação automática (Swagger):

```
http://127.0.0.1:8000/docs
```

---

## Exemplo de resposta

```json
[
  {
    "dia": 1,
    "mes": 1,
    "descricao": "Confraternização universal (feriado nacional)"
  },
  {
    "dia": 17,
    "mes": 2,
    "descricao": "Carnaval (ponto facultativo)"
  }
]
```

---

## 📄 Licença

Este projeto está sob a licença MIT.
