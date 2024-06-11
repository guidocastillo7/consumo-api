import requests
import json


#Funcion para obtener todos los productos, metodo GET
def get_products():
    response = requests.get('https://fakestoreapi.com/products')
    result = response.json()
    print(json.dumps(result, indent=4))


#Funcion para obtener un producto mediante su id, metodo GET
def get_product(id):
    response = requests.get(f'https://fakestoreapi.com/products/{id}')
    result = response.json()
    print(json.dumps(result, indent=4))


#Funcion para crear un producto, metodo POST
def create_product():
    data = {
        'title':'Laptop HP',
        'price':900,
        'description':'Personal laptop for developers.',
        'image':'https://image.com',
        'category':'electronic'
    }

    response = requests.post('https://fakestoreapi.com/products', json=data)
    result = response.json()
    print(json.dumps(result, indent=4))


#Funcion para actualizar un producto, metodo PUT
def update_product(id):
    data = {
        'title':'Fjallraven',
        'price':150,
        'description':'Your perfect pack for everyday',
        'image':'https://imagetest.com',
        'category':'clothing'
    }

    response = requests.put(f'https://fakestoreapi.com/products/{id}', json=data)
    result = response.json()
    print(json.dumps(result, indent=4))


#Funcion para eliminar un producto, metodo DELETE
def delete_product(id):
    response = requests.delete(f'https://fakestoreapi.com/products/{id}')
    result = response.json()
    print(json.dumps(result, indent=4))



#Funcion para obtener datos de un usuario, metodo GET
def get_user(id):
    response = requests.get(f'https://fakestoreapi.com/users/{id}')
    result = response.json()
    print(json.dumps(result, indent=4))


#Funcion para iniciar sesion un usuario para obtener su token, metodo POST
def login():
    data = {
        'username':'johnd',
        'password':'m38rmF$'
    }

    response = requests.post('https://fakestoreapi.com/auth/login', json=data)
    result = response.json()
    print(json.dumps(result, indent=4))



#Funcion inicial, donde eliges que operacion hacer
def init():
    print('Opcion 1: Ver todos los productos.')
    print('Opcion 2: Buscar producto por id.')
    print('Opcion 3: Crear un producto.')
    print('Opcion 4: Actualizar un producto.')
    print('Opcion 5: Eliminar un producto.')
    print('Opcion 6: Buscar un usuario por id.')
    print('Opcion 7: Iniciar sesion un usuario.')

    opcion = input('Elija la opcion: ')

    if opcion == '1':
        get_products()

    if opcion == '2':
        id = input('Ingrese el id del producto: ')
        get_product(id)

    if opcion == '3':
        create_product()

    if opcion == '4':
        id = input('Ingresa el id del producto a actualizar: ')
        update_product(id)

    if opcion == '5':
        id = input('Ingrese el id del producto a eliminar: ')
        delete_product(id)

    if opcion == '6':
        id = input('Ingresa el id del usuario: ')
        get_user(id)

    if opcion == '7':
        login()


if __name__ == '__main__':
    init()