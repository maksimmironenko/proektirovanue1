
from firma.Client import Client


class ClientSerializer:
    def __init__(self, client):
        self.id = client.get_id()
        self.firstname = client.get_firstname()
        self.surname = client.get_surname()
        self.fathersname = client.get_fathersname()
        self.phone_number = client.get_phone_number()
        self.pasport = client.get_pasport()
        self.balance = client.get_balance()
        self.email = client.get_email()

    @staticmethod
    def from_pg_sql(sql_response):
        return Client(
            id=sql_response[0],
            email=sql_response[1],
            phone_number=sql_response[2],
            firstname=sql_response[3],
            surname=sql_response[4],
            fathersname=sql_response[5],
            pasport=sql_response[6],
            balance=sql_response[7],
        )
