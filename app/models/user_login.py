import sqlalchemy as sa

from app.models import Base


class UserLogin(Base):
    __tablename__ = 'UserLogin'

    id = sa.Column('id', sa.Integer, primary_key=True)
    user_id = sa.Column('user_id', sa.Integer)
    refresh_token = sa.Column('refresh_token', sa.String)
    expired_at = sa.Column('expired_at', sa.DateTime, default=sa.func.NOW())
    created_at = sa.Column('created_at', sa.DateTime, default=sa.func.NOW())
    modified_at = sa.Column('modified_at', sa.DateTime, default=sa.func.NOW(), onupdate=sa.func.NOW())
