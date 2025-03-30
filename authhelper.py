import jwt
import datetime

class ValidationError(Exception):
    pass

class InvalidTokenError(Exception):
    pass

class MissingTokenError(Exception):
    pass

def validate_request(url_request):
    # Get token from headers
    token = url_request.headers.get('token')
    if token is None:
        raise MissingTokenError("Missing token")

    # Validate token
    if is_valid_token(token):
        return
    else:
        raise InvalidTokenError("Invalid token")

def is_valid_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        token_date = datetime.datetime.fromtimestamp(payload['exp'])
        if token_date < datetime.datetime.utcnow():
            print("Token expired")
            return False
        print("valid token received: " + str(token_date))
        return True
    except:
        print("Decoding token failed")
        return False

# Authorized users (really good database)
authorized_users = dict({'admin': 'password123'})

# Secret key to encode the JWT token
SECRET_KEY = 'honda_access_virus'

# Verify if username matches password
def is_authorized_user(username, password):
    if authorized_users[username] == password:
        return True
    else:
        return False

# Create a JWT token
def create_auth_token(username):
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)  # Token expires in 30 days
    }
    auth_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return auth_token