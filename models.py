import os

from peewee import (PostgresqlDatabase, Model, IntegerField, CharField,
                    ManyToManyField)


database = PostgresqlDatabase(
    os.environ.get('POSTGRESQL_DATABASE'),
    user=os.environ.get('POSTGRESQL_USER'),
    password=os.environ.get('POSTGRESQL_PASSWORD'),
    host=os.environ.get('POSTGRESQL_HOST'),
    port=os.environ.get('POSTGRESQL_PORT'),
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
