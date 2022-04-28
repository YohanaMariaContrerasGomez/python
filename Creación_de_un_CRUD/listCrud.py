import sys

clients = ['Pablo','Ricardo']

def create_client(client_name):
    """definimos la variable global para poder usar la variable"""
    global clients

    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already is in the client\'s list')

def list_client():
    for idx, client in enumerate(clients):
        print('{}:{}'.format(idx, client))

def update_client(client_name, update_client_name):

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = update_client_name
    else:
        print('Client is not in clients list')

def delete_client(client_name):

    if client_name in clients:
       clients.remove(client_name)
    else:
        print('Client is not in client list')

def search_client(client_name):

    for client in clients:
        if client != client_name:
            continue
        else:
            return True

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

def _get_client_name():
    client_name = None
    
    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name
    
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
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')