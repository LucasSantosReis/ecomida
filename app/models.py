from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
import bcrypt

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)

    def set_password(self, password: str):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def verify_password(self, password: str):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    @classmethod
    def create_user(cls, username: str, password: str, db_session):
        user = db_session.query(User).filter(User.username == username).first()
        if user:
            raise Exception("Usuário já existe")
        new_user = User(username=username)
        new_user.set_password(password)
        db_session.add(new_user)
        db_session.commit()
        db_session.refresh(new_user)
        return new_user


class Pedido(Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum('Em andamento', 'Entregue', 'Cancelado', name='status_enum'), default='Em andamento')
    user_id = Column(Integer)

    def __repr__(self):
        return f"<Pedido id={self.id} status={self.status}>"
