from peewee import (PostgresqlDatabase, Model, IntegerField, CharField,
                    ManyToManyField)

from settings import (POSTGRESQL_DATABASE, POSTGRESQL_USER, POSTGRESQL_PASSWORD,
                      POSTGRESQL_HOST, POSTGRESQL_PORT)


database = PostgresqlDatabase(
    POSTGRESQL_DATABASE,
    POSTGRESQL_USER,
    POSTGRESQL_PASSWORD,
    POSTGRESQL_HOST,
    POSTGRESQL_PORT,
)


class BaseModel(Model):
    class Meta:
        database = database


class TelegramModel(BaseModel):
    telegram_id = IntegerField(unique=True)


class KofaModel(BaseModel):
    kofa_id = CharField(unique=True)


class Program(KofaModel):
    title = CharField()
    url = CharField()


class Chat(TelegramModel):
    programs = ManyToManyField(Program, backref='chats')


migrated_models = [Program, Chat]
