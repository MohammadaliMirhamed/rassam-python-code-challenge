from classes.database.vendor.DatabaseInterface import DatabaseInterface
import psycopg2
import psycopg2.extras

"""postgres database class."""
class PostgresDB(DatabaseInterface):

    def __init__(self, db_config: dict) -> None:
        # connect to the database
        self.conn = psycopg2.connect(
            dbname=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port']
        )
        # create a cursor
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def execute_query(self, query, type) -> dict:
        # execute the query
        self.cur.execute(query)
        if type == "read":
            # get columns
            columns = list(self.cur.description)
            # fetch result
            result = self.cur.fetchall()
            # make dict
            results = []
            for row in result:
                row_dict = {}
                for i, col in enumerate(columns):
                    row_dict[col.name] = row[i]
                results.append(row_dict)
            # fetch the results
            return results
        elif type == "write":
            # commit the changes
            self.conn.commit()
            # return the results
            return {"status": "success"}

    def close(self) -> None:
        # close the cursor
        self.cur.close()
        # close the connection
        self.conn.close()
