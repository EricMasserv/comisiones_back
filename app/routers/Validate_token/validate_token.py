from jwt import decode, encode, exceptions
from fastapi.responses import JSONResponse
from ...Config.config_env import *

def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key= os.getenv("SECRET_KEY"), algorithms=os.getenv("ALGORITHM"))
        decode(token, key= os.getenv("SECRET_KEY"), algorithms=os.getenv("ALGORITHM"))
    except exceptions.DecodeError:
        return JSONResponse(content={"message":"Token invalido"},status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message":"Token invalido"},status_code=401)