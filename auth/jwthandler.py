from datetime import datetime, timedelta, timezone
from typing import Dict

import jwt

JWT_SECRET = "ungabunga"
JWT_ALGORITHM = "HS256"


def decodeJWT(token: str) -> Dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        return {}
    except jwt.InvalidTokenError:
        return {}
    return decoded_token

def signAcessJWT(user_id: str):
    payload = {
        "user_id": user_id,
        
        "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=10)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token
def signRefreshJWT(user_id: str): 
    payload = {
        "user_id": user_id,
        "exp":  datetime.now(tz=timezone.utc) + timedelta(days=30),
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token