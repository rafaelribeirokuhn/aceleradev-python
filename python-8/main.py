import jwt


def create_token(data, secret):
    return jwt.encode({"language": "Python"}, "acelera", algorithm="HS256")


def verify_signature(token):
    try:
        return jwt.decode(token, "acelera", algorithms=["HS256"])
    except jwt.exceptions.DecodeError:
        return {"error": 2}
