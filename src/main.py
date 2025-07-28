from fastapi import FastAPI, Request
from src.routes import items, auth
from src.middleware.auth import verify_token_middleware

app = FastAPI(
    title="Proyecto API Segura con FastAPI",
    description="API con autenticación JWT y CRUD protegido",
    version="1.0.0"
)

@app.middleware("http")
async def middleware_dispatcher(request: Request, call_next):
    if request.url.path.startswith("/items"):
        await verify_token_middleware(request)
    response = await call_next(request)
    return response

app.include_router(auth.router)
app.include_router(items.router)