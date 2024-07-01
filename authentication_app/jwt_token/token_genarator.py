import jwt
from datetime import datetime, timedelta

def generate_jwt_token(user_id, secret_key, expiration_hours=1):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=expiration_hours)
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def generate_refresh_token(user_id, secret_key, expiration_days=7):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=expiration_days)
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token