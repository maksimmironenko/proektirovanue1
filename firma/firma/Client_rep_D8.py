
from firma.Client import Client
from root.database import connection
from common_utils.serializers import ClientSerializer

class Client_rep_DB(Client):

    def __init__(self, *args, **kwargs):
        super(Client_rep_DB, self).__init__(*args, **kwargs)

    @staticmethod
    def get_all():
        with connection.cursor() as cur:
            cur.execute("""
            SELECT * FROM
            client;
            """)
            return cur.fetchall()

    @staticmethod
    def get_count():
        return len(Client_rep_DB.get_all())

    @staticmethod
    def get(id):
        if not isinstance(id, int):
            raise ValueError('id должен быть int.')
        with connection.cursor() as cur:
            cur.execute(f"SELECT * FROM client c WHERE c.id = {id};")
            obj = ClientSerializer.from_pg_sql(cur.fetchone())
        return obj

    @staticmethod
    def add(client):
        with connection.cursor() as cur:
            cur.execute(f"""
            INSERT INTO client 
            (firstname, surname, phone_number, pasport, balance, email, fathersname) 
            VALUES(
                '{client.get_firstname()}', 
                '{client.get_surname()}',
                '{client.get_phone_number()}',
                '{client.get_pasport()}',
                 {client.get_balance() if client.get_balance() is not None else 'null'},
                '{client.get_email()}',
                {"'" if client.get_fathersname() else ''}{client.get_fathersname() if client.get_fathersname() else 'null'}{"'" if client.get_fathersname() else ''}
            )
            """)
            connection.commit()

    @staticmethod
    def delete(id):
        with connection.cursor() as cur:
            cur.execute(f"""
                DELETE FROM client c
                WHERE c.id = {id}; 
            """)
            connection.commit()

    @staticmethod
    def change(id, client):
        with connection.cursor() as cur:
            cur.execute(
                f"""
                    UPDATE client c
                    SET 
                        firstname='{client.get_firstname()}', 
                        surname='{client.get_surname()}', 
                        phone_number='{client.get_phone_number()}', 
                        pasport='{client.get_pasport()}', 
                        balance={client.get_balance() if client.get_balance() is not None else 'null'}, 
                        email='{client.get_email()}', 
                        fathersname={"'" if client.get_fathersname() else ''}{client.get_fathersname() if client.get_fathersname() else 'null'}{"'" if client.get_fathersname() else ''}
                    WHERE c.id = {id};
                """
            )
