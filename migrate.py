from models import database, migrated_models


def create_tables():
    with database:
        database.create_tables(migrated_models)


if __name__ == '__main__':
    create_tables()
