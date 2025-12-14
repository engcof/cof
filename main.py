
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from core.templates import templates

#from routers import names

# =========================================
# إعداد التطبيق
# =========================================
app = FastAPI()

# =========================================
# Static Files
# =========================================
app.mount("/static", StaticFiles(directory="static"), name="static")

# =========================================
# تضمين الراوترات
# =========================================

#app.include_router(names.router)

# =========================================
# # الصفحة الرئيسية
# # =========================================
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
    })
    


# uvicorn main:app --reload


