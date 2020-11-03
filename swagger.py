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

    def delete_user (email):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'jwtacc': '%s'%token
            }
        user_id=methods.get_user_id(email)
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
    
    def create_country (code, name):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'jwtacc': '%s'%token
            }
        data = "{\"code\":\"%s\",\"name\":\"%s\", \"archived\" : false}"% (code, name)
        print(data)
        response = requests.request('POST', url = f'{apiurl}/countries', headers=headers, data=data).json()
        print(response)
        created_country = json.loads(json.dumps(response))['name']
        print(f'Country {created_country} successfully created')

    def get_country_id(code):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'jwtacc': '%s'%token
            }
        response = requests.request('GET',url = f'{apiurl}/countries?fields=id&query=%7B%22code%22%3A%22{code}%22%7D', headers=headers, data = {}).json()
        country_id=json.loads(json.dumps(response))['rows'][0]['id']
        print(f'Country ID is {country_id}')
        return country_id

    def delete_country (code):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'jwtacc': '%s'%token
            }
        country_id=methods.get_country_id(code)
        response = requests.request('DELETE',url = f'{apiurl}/countries/{country_id}', headers=headers, data = {}).json()
        print(response)
        deleted_country = json.loads(json.dumps(response))['code']
        print(f'Country {deleted_country} successfully deleted')

    def create_consolidated_supplier (asdb,name,isLocal,plant,analyst,consolidator,shipfreq,transittime,role,contactname,email,phone,lang,legaladdress,physicaladdress,country,shipaddress,timezone):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'jwtacc': '%s'%token
            }
        data = "{\"asdb\":\"%s\",\"name\":\"%s\", \"isConsolidator\":false, \"isLocal\":%s,\"plants\":[{\"plant\":\"%s\",\"analyst\":\"%s\",\"consolidator\":\"%s\",\"shippingFrequency\":\"%s\",\"transitTime\":%s}],\"archived\":false,\"contacts\":[{\"role\":\"%s\",\"name\":\"%s\",\"email\":\"%s\",\"phone\":\"%s\"}],\"language\":\"%s\",\"legalAddress\":\"%s\",\"physicalAddress\":\"%s\",\"physicalCountry\":\"%s\",\"shippingAddress\":\"%s\",\"timezone\":\"%s\"}"% (asdb,name,isLocal,plant,analyst,consolidator,shipfreq,transittime,role,contactname,email,phone,lang,legaladdress,physicaladdress,country,shipaddress,timezone)
        print(data)
        response = requests.request('POST', url = f'{apiurl}/suppliers', headers=headers, data=data).json()
        print(response)
        created_supplier = json.loads(json.dumps(response))['asdb']
        print(f'Supplier {created_supplier} successfully created')

    def create_direct_supplier (asdb,name,isLocal,plant,analyst,shipfreq,transittime,role,contactname,email,phone,lang,legaladdress,physicaladdress,country,shipaddress,timezone):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'jwtacc': '%s'%token
            }
        data = "{\"asdb\":\"%s\",\"name\":\"%s\", \"isConsolidator\":false, \"isLocal\":%s,\"plants\":[{\"plant\":\"%s\",\"analyst\":\"%s\",\"consolidator\":null,\"shippingFrequency\":\"%s\",\"transitTime\":%s}],\"archived\":false,\"contacts\":[{\"role\":\"%s\",\"name\":\"%s\",\"email\":\"%s\",\"phone\":\"%s\"}],\"language\":\"%s\",\"legalAddress\":\"%s\",\"physicalAddress\":\"%s\",\"physicalCountry\":\"%s\",\"shippingAddress\":\"%s\",\"timezone\":\"%s\"}"% (asdb,name,isLocal,plant,analyst,shipfreq,transittime,role,contactname,email,phone,lang,legaladdress,physicaladdress,country,shipaddress,timezone)
        print(data)
        response = requests.request('POST', url = f'{apiurl}/suppliers', headers=headers, data=data).json()
        print(response)
        created_supplier = json.loads(json.dumps(response))['asdb']
        print(f'Supplier {created_supplier} successfully created')

    def create_consolidator (asdb,name,isLocal,plant,analyst,shipfreq,transittime,rectransittime,role,contactname,email,phone,lang,legaladdress,physicaladdress,country,shipaddress,timezone):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'jwtacc': '%s'%token
            }
        data = "{\"asdb\":\"%s\",\"name\":\"%s\", \"isConsolidator\":true, \"isLocal\":%s,\"plants\":[{\"plant\":\"%s\",\"analyst\":\"%s\",\"consolidator\":null,\"shippingFrequency\":\"%s\",\"transitTime\":%s,\"receivingTransitTime\":%s}],\"archived\":false,\"contacts\":[{\"role\":\"%s\",\"name\":\"%s\",\"email\":\"%s\",\"phone\":\"%s\"}],\"language\":\"%s\",\"legalAddress\":\"%s\",\"physicalAddress\":\"%s\",\"physicalCountry\":\"%s\",\"shippingAddress\":\"%s\",\"timezone\":\"%s\"}"% (asdb,name,isLocal,plant,analyst,shipfreq,transittime,rectransittime,role,contactname,email,phone,lang,legaladdress,physicaladdress,country,shipaddress,timezone)
        print(data)
        response = requests.request('POST', url = f'{apiurl}/suppliers', headers=headers, data=data).json()
        print(response)
        created_supplier = json.loads(json.dumps(response))['asdb']
        print(f'Supplier {created_supplier} successfully created')

    def delete_supplier (asdb):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'jwtacc': '%s'%token
            }
        response = requests.request('DELETE',url = f'{apiurl}/suppliers/{asdb}', headers=headers, data = {}).json()
        print(response)
        deleted_supplier = json.loads(json.dumps(response))['asdb']
        print(f'Supplier {deleted_supplier} successfully deleted')

    def create_part (partnumber,nameru,nameen,uom,weight,plant,violdate,looseonvioldate,willmake,thresqty,startusedate,pack,packqty):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'jwtacc': '%s'%token
            }
        data = "{\"number\":\"%s\",\"_name\":{\"ru\":\"%s\",\"en\":\"%s\"},\"UOM\":\"%s\",\"weight\":%s,\"plants\":[{\"plant\":\"%s\",\"firstDateThresholdViolation\":\"%s\",\"looseOnFirstDateThresholdViolation\":%s,\"willMake\":%s,\"thresholdQty\":%s,\"startToUseDay\":\"%s\",\"pack\":\"%s\",\"packQty\":%s}]}"% (partnumber,nameru,nameen,uom,weight,plant,violdate,looseonvioldate,willmake,thresqty,startusedate,pack,packqty)
        print(data)
        response = requests.request('POST', url = f'{apiurl}/parts', headers=headers, data=data.encode('utf-8')).json()
        print(response)
        created_part = json.loads(json.dumps(response))['number']
        print(f'Part {created_part} successfully created')

    def get_part_id(number):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'jwtacc': '%s'%token
            }
        response = requests.request('GET',url = f'{apiurl}/parts?fields=id&query=%7B%22number%22%3A%22{number}%22%7D', headers=headers, data = {}).json()
        part_id=json.loads(json.dumps(response))['rows'][0]['id']
        print(f'Part ID is {part_id}')
        return part_id

    def delete_part (number):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'jwtacc': '%s'%token
            }
        part_id=methods.get_part_id(number)
        response = requests.request('DELETE',url = f'{apiurl}/parts/{part_id}', headers=headers, data = {}).json()
        print(response)
        deleted_part = json.loads(json.dumps(response))['number']
        print(f'Part {deleted_part} successfully deleted')

    def create_partSupplier (partnumber,asdb,plant,lastASN,lastQty,lastDate,totalQty,multiplicity,minOrderQty):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'jwtacc': '%s'%token
            }
        data = "{\"number\":\"%s\",\"supplierAsdb\":\"%s\",\"plants\":[{\"plant\":\"%s\",\"lastAsn\":\"%s\",\"lastQty\":\"%s\",\"lastDate\":\"%s\",\"totalQty\":%s,\"multiplicity\":%s,\"minOrderQty\":%s}]}"% (partnumber,asdb,plant,lastASN,lastQty,lastDate,totalQty,multiplicity,minOrderQty)
        print(data)
        response = requests.request('POST', url = f'{apiurl}/partsSuppliers', headers=headers, data=data.encode('utf-8')).json()
        print(response)
        created_partSupplier = json.loads(json.dumps(response))['number']
        print(f'PartSupplier record for {created_partSupplier} successfully created')
    
    def get_partSupplier_id(number):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'jwtacc': '%s'%token
            }
        response = requests.request('GET',url = f'{apiurl}/partsSuppliers?fields=id&query=%7B%22number%22%3A%22{number}%22%7D', headers=headers, data = {}).json()
        partSupplier_id=json.loads(json.dumps(response))['rows'][0]['id']
        print(f'PartSupplier record ID is {partSupplier_id}')
        return partSupplier_id

    def delete_partSupplier (number):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'jwtacc': '%s'%token
            }
        partSupplier_id=methods.get_partSupplier_id(number)
        response = requests.request('DELETE',url = f'{apiurl}/partsSuppliers/{partSupplier_id}', headers=headers, data = {}).json()
        print(response)
        deleted_partSupplier = json.loads(json.dumps(response))['number']
        print(f'PartSupplier record for {deleted_partSupplier} successfully deleted')
    
    def create_orders (startDay,endDay,plant,supplier,part1,part2,part3):
        apiurl = "https://api-250.aurus-sp.app/api"
        token = methods.get_token()
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'jwtacc': '%s'%token
            }
        data = "{\"startDay\":\"%s\",\"endDay\":\"%s\",\"plant\":\"%s\",\"supplier\":\"%s\",\"parts\":[\"%s\",\"%s\",\"%s\"]}"% (startDay,endDay,plant,supplier,part1,part2,part3)
        print(data)
        response = requests.request('POST', url = f'{apiurl}/orders-fake/create-many', headers=headers, data=data.encode('utf-8')).json()
        print(response)
        print('Orders successfully created')
