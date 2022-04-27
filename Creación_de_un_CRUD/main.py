from ctypes import sizeof
from typing import Type


clients = 'Pablo,Ricardo,'

def create_client(client_name):
    """definimos la variable global para poder usar la variable"""
    global clients

    if client_name not in clients:
        clients += client_name
        _add_coma()
    else:
        print('Client already is in the client\'s list')

def list_client():
    global clients

    print(clients)

def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name+',', update_client_name+',')
    else:
        print('Client is not in clients list')

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name+',', '')
    else:
        print('Client is not in client list')

def _add_coma():
    global clients

    clients += ', '

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')

def _get_client_name():
    return  input('What is the client name? ')

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_client()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_client()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is updated client name: ')
        update_client(client_name, update_client_name)
        list_client()
    else:
        print('Invalid command')

    

    