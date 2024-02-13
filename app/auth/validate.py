import requests
from typing import Tuple
from flask import Response, current_app

def token(request: Response)-> Tuple:
    if not "Authorization" in request.headers:
        return None, ("missing credentials", 401)
    
    token = request.headers["Authorization"]

    if not token:
        return None, ("missing credentials", 401)
    
    response = requests.post(
        f"http://{current_app.config['AUTH_SVC_ADDRESS']}/validate",
        headers={"Authorization": token}
    )

    if response.status_code == 200:
        return response.txt, None
    else:
        return None, (response.txt, response.status_code)