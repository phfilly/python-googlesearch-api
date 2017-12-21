import psycopg2
import environment


def connect():
    connection_string = "host={host} port={port} dbname={db} user={user} password={password}"
    connection = psycopg2.connect(
        connection_string.format(
            host=environment.DW_HOST,
            port=environment.DW_PORT,
            db=environment.DW_DB,
            user=environment.DW_USER,
            password=environment.DW_PASS
        )
    )
    return connection
