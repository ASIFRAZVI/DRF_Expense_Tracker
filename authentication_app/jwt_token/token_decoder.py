import jwt

def decode_jwt_token(request, secret_key):
    jwt_token = request.COOKIES.get('access_token')
    
    try:
        payload = jwt.decode(jwt_token, secret_key, algorithms=['HS256'])
        return payload
    
    except jwt.ExpiredSignatureError:
        raise Exception("JWT token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid JWT token")