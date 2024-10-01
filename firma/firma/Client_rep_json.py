
import json

from common_utils.serializers import ClientSerializer
from root.settings import BASE_DIR
from firma.Client import Client


class Client_rep_json(Client):

    def __init__(self, *args, **kwargs):
        super(Client_rep_json, self).__init__(*args, **kwargs)

    @classmethod
    def read(cls, skip=0, count=None):
        clients = []
        data, _ = Client_rep_json.__get_data_from_file()
        for entry in data:
            clients.append(Client(**entry))
        return clients[skip:][:count]

    @classmethod
    def save(cls, clients):
        serializer_class = ClientSerializer
        data, ids = Client_rep_json.__get_data_from_file()
        for client in clients:
            serialized_data = serializer_class(client).__dict__
            if serialized_data['id'] in ids:
                data[ids.index(serialized_data['id'])] = serialized_data
            else:
                data.append(serialized_data)
        Client_rep_json.__write_data_to_file(data)

    @classmethod
    def get(cls, id):
        data, _ = Client_rep_json.__get_data_from_file()
        for entry in data:
            if entry['id'] == id:
                return Client(**entry)
        return None

    @classmethod
    def delete(cls, id):
        data, ids = Client_rep_json.__get_data_from_file()
        data.remove(data[ids.index(id)])
        Client_rep_json.__write_data_to_file(data)

    @classmethod
    def add(
            cls,
            email,
            phone_number,
            firstname,
            surname,
            fathersname,
            pasport,
            balance=None
    ):
        data, ids = Client_rep_json.__get_data_from_file()
        ids.sort()

        id = 0
        if ids:
            id = ids[-1]
        id+=1

        data.append(
            {
                'id': id,
                'email': email,
                'phone_number': phone_number,
                'firstname': firstname,
                'surname': surname,
                'fathersname': fathersname,
                'pasport': pasport,
                'balance': balance,
            }
        )
        Client_rep_json.__write_data_to_file(data)

    @classmethod
    def get_count(cls):
        return len(Client_rep_json.read())

    @staticmethod
    def __get_data_from_file():
        path_to_file = BASE_DIR / 'db_json.json'
        with open(path_to_file) as file:
            try:
                data = json.loads(file.read())
                ids = [entry['id'] for entry in data]
            except json.decoder.JSONDecodeError:
                data = []
                ids = []

        return data, ids

    @staticmethod
    def __write_data_to_file(data):
        path_to_file = BASE_DIR / 'db_json.json'
        with open(path_to_file, mode='w') as file:
            file.write(json.dumps(data))
