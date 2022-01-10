from typing import Optional
import jwt
from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from fastapi.exceptions import HTTPException

from app.utils.get_payload import get_payload


class Authentication(HTTPBearer):
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        authorization = await super().__call__(request)

        try:
            payload = get_payload(authorization.credentials)
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                401,
                detail={
                    'message': 'Token expired',
                    'code': 40100
                }
            )
        except jwt.DecodeError:
            raise HTTPException(
                401,
                detail={
                    'message': 'Token invalid',
                    'code': 40101
                }
            )
        
        return payload
