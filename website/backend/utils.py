import psycopg2.extensions
import psycopg2
import json
creds = json.load(open('aws.json'))


class Connection(psycopg2.extensions.connection):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    

    def to_json(self, query):
        cursor = self.cursor()
        cursor.execute(query)
        
        return [
            {header[0]: val for header, val in zip(cursor.description, row)} 
            for row in cursor.fetchall()
        ]


def get_conn():
    return psycopg2.connect(connection_factory=Connection, **creds)


if __name__ == '__main__':
    get_conn().to_json('select * from test.source1')