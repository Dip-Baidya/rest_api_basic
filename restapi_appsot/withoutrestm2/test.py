import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'


# def get_resources(id=None):
#     data={}
#     if data is not None:
#         data={
#             'id':id
#         }
#     resp = requests.get(BASE_URL + ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resources()

# def create_resource():
#     new_std = {
#         'name':'Aziz',
#         'rollno':106,
#         'marks':80,
#         'gf':'Shirin',
#         'bf':'sakif'
        
#     }
#     resp = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_std))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()

# def update_resource(id):
#     new_emp = {
#         'id':id,
#         'gf': 'Putul',
#     }
#     resp = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(2)


def delete_resource(id):
    data={
        'id': id
    }
    resp = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

delete_resource(1)

