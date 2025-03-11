from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Pedido, User
from app.schemas import PedidoCreate, PedidoResponse
from app.routes.auth import get_current_user 

router = APIRouter()


@router.post("/", response_model=PedidoResponse)
def criar_pedido(
    pedido: PedidoCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    novo_pedido = Pedido(user_id=current_user.id)
    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)
    return novo_pedido


@router.get("/id/{pedido_id}", response_model=PedidoResponse)
def consultar_status(
    pedido_id: int, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    if pedido.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Você não tem permissão para acessar este pedido")
    
    return pedido


@router.get("/status", response_model=list[PedidoResponse])
def consultar_pedidos_por_status(
    status: str, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):

    if status not in ['Em andamento', 'Entregue', 'Cancelado']:
        raise HTTPException(status_code=400, detail="Status inválido")


    pedidos = db.query(Pedido).filter(Pedido.status == status, Pedido.user_id == current_user.id).all()

    if not pedidos:
        raise HTTPException(status_code=404, detail="Nenhum pedido encontrado com esse status")
    
    return pedidos
