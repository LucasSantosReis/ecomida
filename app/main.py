from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.routes import pedidos, auth
from app.database import engine, Base


security = HTTPBasic()

app = FastAPI(
    title="Minha API",
    description="Uma API com autenticação básica no Swagger",
    version="1.0.0",
    openapi_tags=[{"name": "Auth", "description": "Endpoints relacionados à autenticação"}],
)


def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"  # Defina o nome de usuário
    correct_password = "admin"  # Defina a senha
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=401, detail="Credenciais inválidas"
        )


app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(pedidos.router, prefix="/pedidos", tags=["Pedidos"])


Base.metadata.create_all(bind=engine)

