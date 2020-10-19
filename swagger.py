import requests
import json

class methods():
    def get_token():
        apiurl = "https://api-250.aurus-sp.app/api"
        data = {"password" : "password!D1",
        "email" : "superuser@test.tst"
        }
        response = requests.request('POST',url = '%s/main/login'%apiurl, data=data).json()
        token=response["jwtacc"]
        return token

    def get_user_id (email):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'jwtacc': '%s'%token
            }
        response = requests.request('GET',url = f'{apiurl}/users?fields=id&query=%7B%22email%22%3A%22{email}%22%7D', headers=headers, data = {}).json()
        user_id=json.loads(json.dumps(response))['rows'][0]['id']
        print(f'User ID is {user_id}')
        return user_id

    def delete_user (user_id):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'jwtacc': '%s'%token
            }
        response = requests.request('DELETE',url = f'{apiurl}/users/{user_id}', headers=headers, data = {}).json()
        print(response)
        deleted_user = json.loads(json.dumps(response))['email']
        print(f'User {deleted_user} successfully deleted')
    
    def create_user (name, email, role, gsdb):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'jwtacc': '%s'%token
            }
        data = "{\"name\":\"%s\",\"role\":[ \"%s\" ], \"email\" : \"%s\",\"gsdb\" : \"%s\"}"% (name, role, email, gsdb)
        print(data)
        response = requests.request('POST', url = f'{apiurl}/users', headers=headers, data=data).json()
        print(response)
        created_user = json.loads(json.dumps(response))['name']
        print(f'User {created_user} successfully created')