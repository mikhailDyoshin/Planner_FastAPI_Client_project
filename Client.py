import requests
from requests.structures import CaseInsensitiveDict


class Client():

    def get_all(self):
        url = 'http://localhost:8080/event/'
        response = requests.get(url)

        return {'status':response.status_code, 'json': response.json()}

    def get_single(self, id: str) -> dict:

        url = 'http://localhost:8080/event/' + id

        headers = CaseInsensitiveDict()
        headers["accept"] = "application/json"

        response = requests.get(url, headers=headers)

        return {'status':response.status_code, 'json': response.json()}


    def sign_up(self, email, password):
        url = 'http://localhost:8080/user/signup/'

        json = {"email": email, "password": password}
        responce = requests.post(url, json=json)
        
        return {'status': responce.status_code, 'json': responce.json()}


    def sign_in(self, email, password):
        url = "http://localhost:8080/user/signin"

        headers = CaseInsensitiveDict()
        headers["accept"] = "application/json"
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        data = f"grant_type=&username={email}&password={password}&scope=&client_id=&client_secret="

        responce = requests.post(url, headers=headers, data=data)

        return {'status': responce.status_code, 'json': responce.json()}


    def post(self, token, tokenType, data):

        url = "http://localhost:8080/event/new"

        headers = CaseInsensitiveDict()
        headers["accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers["Authorization"] = ' '.join((tokenType, token))

        responce = requests.post(url, headers=headers, json=data)

        return {'status': responce.status_code, 'json': responce.json()}


    def put(self, token:str, tokenType:str, id:str, data:dict) -> dict:

        url = "http://localhost:8080/event/" + id

        headers = CaseInsensitiveDict()
        headers["accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers["Authorization"] = ' '.join((tokenType, token))

        responce = requests.put(url, headers=headers, json=data)

        return {'status': responce.status_code, 'json': responce.json()}


    def delete(self, token:str, tokenType:str, id:str) -> dict:

        url = "http://localhost:8080/event/" + id

        headers = CaseInsensitiveDict()
        headers["accept"] = "application/json"
        headers["Authorization"] = ' '.join((tokenType, token))

        responce = requests.delete(url, headers=headers)

        return {'status': responce.status_code, 'json': responce.json()}
