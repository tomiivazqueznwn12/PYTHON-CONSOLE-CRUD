import sys


import csv
import os


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ["name","company", "email", "position"]

clients = []

def _inizialize_clients_from_storage():
    with open(CLIENT_TABLE, mode = "r") as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

def _save_clients_to_storage():
    temp_table_name = f'{CLIENT_TABLE}.tmp'
    with open(temp_table_name,mode= "w") as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

    os.remove(CLIENT_TABLE)
    os.rename(temp_table_name,CLIENT_TABLE)




def create_clients(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('that client already is in the client\'s list')


def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))

def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')

def delete_client_name(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break

def search_client(parameter_name):
    global clients
    for client in clients:
        if client["name"] != parameter_name:
            continue
        else:
            return True

def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client



def _print_welcome():
    print('WELCOME TO VENT.ASS')
    print('*' * 50)
    print('what would you like to do today?')
    print('[C]reate client ')
    print('[D]elete client ')
    print('[U]pdate client ')
    print('[S]earch client ')

def _get_client_field(field_name):
    field = None
    while not field:
        field = input('what is the client {}?'.format(field_name))
        return field


def _get_client_from_user():
    client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),

        }
    return client

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
    _inizialize_clients_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()

    
    if command == 'C':
        client = _get_client_from_user()
        create_clients(client)
        #list_clients()
    elif command == 'L':
        list_clients()
    
    elif command == 'D':
        client_id = int(_get_client_field("id"))
        delete_client_name(client_id)
        list_clients()
    
    elif command == 'U':
        client_id = _get_client_field('id')
        updated_client_name = _get_client_from_user()
        update_client(int(client_id), updated_client_name)
        #list_clients()

    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found:
            print('the client is in the list')
        else:
            print(('the client {} don\'t exist in our client list').format(client_name))
    else:
        print('Invalid command ')

    _save_clients_to_storage()
