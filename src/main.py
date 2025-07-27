from fastapi import FastAPI, Request
from src.routes import auth
from src.middleware.auth import verify_token_middleware

app = FastAPI()

@app.middleware("http")
async def middleware_dispatcher(request: Request, call_next):
    if request.url.path.startswith("/tasks"):
        await verify_token_middleware(request)
    response = await call_next(request)
    return response

app.include_router(auth.router)