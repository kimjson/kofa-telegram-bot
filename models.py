from peewee import SqliteDatabase, Model, IntegerField, CharField

database = SqliteDatabase('kofa_telegram_bot.db')


class BaseModel(Model):
    class Meta:
        database = database


class TelegramModel(BaseModel):
    telegram_id = IntegerField(unique=True)


class KofaModel(BaseModel):
    kofa_id = CharField(unique=True)


class Chat(TelegramModel):
    pass


class Program(KofaModel):
    title = CharField()
    link = CharField()


migrated_models = [
    Chat,
    Program,
]
