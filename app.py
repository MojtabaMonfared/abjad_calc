from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory='templates')

KABIR = {
    'ا': 1,
    'ب': 2,
    'ج': 3,
    'د': 4,
    'ه': 5,
    'و': 6,
    'ز': 7,
    'ح': 8,
    'ط': 9,
    'ی': 10,
    'ک': 20,
    'ل': 30,
    'م': 40,
    'ن': 50,
    'س': 60,
    'ع': 70,
    'ف': 80,
    'ص': 90,
    'ق': 100,
    'ر': 200,
    'ش': 300,
    'ت': 400,
    'ث': 500,
    'خ': 600,
    'ذ': 700,
    'ض': 800,
    'ظ': 900,
    'غ': 1000
}

SAQIR = {
    'ا': 1,
    'ب': 2,
    'ج': 3,
    'د': 4,
    'ه': 5,
    'و': 6,
    'ز': 7,
    'ح': 8,
    'ط': 9,
    'ی': 9,
    'ک': 8,
    'ل': 6,
    'م': 4,
    'ن': 2,
    'س': 5,
    'ع': 10,
    'ف': 8,
    'ص': 1,
    'ق': 4,
    'ر': 8,
    'ش': 3,
    'ت': 4,
    'ث': 8,
    'خ': 7,
    'ذ': 2,
    'ض': 8,
    'ظ': 9,
    'غ': 4
}

@app.get('/', response_class=HTMLResponse)
def Index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post('/api')
def handle_abjad(text: str = Form(), mode: str = Form()):
    if mode == 'saqir':
        a = []
        for i in str(text):
            if i in SAQIR:
                a.append((SAQIR[str(i)]))
        return sum(a)
        
    if mode == 'kabir':
        a = []
        for i in str(text):
            if i in KABIR:
                a.append((KABIR[str(i)]))
        return sum(a)
