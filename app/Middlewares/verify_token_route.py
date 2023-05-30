from fastapi import Request
from fastapi.routing import APIRoute
from ..routers.Validate_token.validate_token import validate_token
from fastapi.responses import JSONResponse

class VerifyTokenRoute(APIRoute):
    def get_route_handler(self):
        original_route = super().get_route_handler()
        
        async def verify_token_middleware(request:Request):
            token = False  
            
            try:
                token = request.headers['Authorization'].split(" ")[1]   
            except:
                print("No existe token")
            
            if not token:
                return JSONResponse(content={"message":"Token invalido"},status_code=401)
            else:
                validation_response = validate_token(token, output=False)
            
            if validation_response == None:
                return await original_route(request)
            else:
                return validation_response
        return verify_token_middleware  