import sqlite3


def make_connection(func):
    def wrapper(self, *args, **kwargs):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            return func(self, cursor, *args, **kwargs)

    return wrapper


class TableData:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name
        self.counter = 0

    @make_connection
    def __len__(self, cursor):
        cursor.execute(f"SELECT count (*) from {self.table_name}")
        return cursor.fetchone()[0]

    @make_connection
    def __getitem__(self, cursor, item):
        # query_input = (item,)
        cursor.execute(
            f"SELECT * from {self.table_name} WHERE name='{item}'"
        )  # , query_input)
        result = cursor.fetchall()
        if result == []:
            raise KeyError(f"key '{item}' not found")
        return result

    @make_connection
    def __contains__(self, cursor, item):
        cursor.execute(f"SELECT * from {self.table_name} WHERE name='{item}'")
        return cursor.fetchone()

    def __iter__(self):
        return IterableDataTable(self.database_name, self.table_name, len(self))


class IterableDataTable:
    def __init__(self, database_name, table_name, length):
        self.database_name = database_name
        self.iter_table_name = table_name
        self.length = length
        self.counter = -1

    @make_connection
    def __next__(self, cursor):
        self.counter += 1
        cursor.execute(f"SELECT * from {self.iter_table_name} LIMIT {self.counter}, 1")
        if self.counter >= self.length:
            raise StopIteration
        while row := cursor.fetchone():
            data_tuple = {}
            for i, element in enumerate(row):
                data_tuple[cursor.description[i][0]] = element
            return data_tuple
