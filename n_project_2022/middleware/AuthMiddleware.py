from rest_framework import authentication
from rest_framework import exceptions

import json
import requests

class IAuthMiddleware(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("access")
        if not token:
            raise exceptions.AuthenticationFailed("Not able tp find authenitication")
        try:
            response = IAuthMiddleware.token_varification(token)
            # IAuthMiddleware.get_user(request)
            if response.status_code != 200:
                raise exceptions.AuthenticationFailed("Token Invalid or expired")
        except Exception:
            raise exceptions.APIException("authentication servr is not reachable")
        
    
    @staticmethod
    def token_varification(token):
        payload = json.dumps({
            'access':token
        })
        header = {
            "Content-Type" : "application/json"
        }
        url = ""
        try:
            response = requests.get("POST",url,headers=header,data=payload,verify=False)
            return response
        except Exception as e:
            raise Exception(e)
        