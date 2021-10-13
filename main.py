clients = 'Pablo,Ricardo,'


def create_clients(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('that client already is in the client\'s list')


def list_clients():
    global clients

    print(clients)


def _add_comma():
    global clients

    clients +=','


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('what would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')


if __name__ == "__main__":
    _print_welcome()

    command = input()

    if command == 'C':
        client_name = input('What is the client name? ')
        create_clients(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('Invalid command ')




    #create_clients("David")
    #list_clients()
