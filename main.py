import sys

clients = ['pablo','ricardo']


def create_clients(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name)
    else:
        print('that client already is in the client\'s list')


def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print(("{} : {}").format(idx, client))

def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        print('that client isn´t in the list')

def delete_client_name(client_name):
    global clients

    if client_name in clients:
        clients = clients.remove(client_name)
    else:
        print('clients is not in client list')

def search_client(parameter_name):
    global clients
    for i in clients:
        if i != parameter_name:
            continue
        else:
            return True



def _print_welcome():
    print('WELCOME TO VENT.ASS')
    print('*' * 50)
    print('what would you like to do today?')
    print('[C]reate client ')
    print('[D]elete client ')
    print('[U]pdate client ')
    print('[S]earch client ')

def _get_client_name():
    client_name= None
    while not client_name:
        client_name = input('What is the client name?: ')
        if client_name == 'exit':
            client_name = None
            break
        
    if not client_name:
        sys.exit()
    return client_name

if __name__ == "__main__":
    _print_welcome()

    command = input()
    command = command.upper()

    
    if command == 'C':
        client_name = _get_client_name()
        create_clients(client_name)
        list_clients()
    
    elif command == 'D':
        client_name = _get_client_name()
        delete_client_name(client_name)
        list_clients()
    
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name ')
        update_client(client_name, updated_client_name)
        list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('the client is in the list')
        else:
            print(('the client {} don\'t exist in our client list').format(client_name))
    else:
        print('Invalid command ')
