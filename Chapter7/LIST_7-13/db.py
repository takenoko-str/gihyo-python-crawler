"""データベースモデル."""
import peewee
from playhouse.pool import PooledMySQLDatabase

# sakilaデータベースへのアクセス情報
db = PooledMySQLDatabase(
    'sakila',
    max_connections=8,
    stale_timeout=10,
    user='root')


class BaseModel(peewee.Model):
    """共通基底モデル."""

    class Meta:
        database = db


class Language(BaseModel):
    """languageテーブル用モデル."""

    language_id = peewee.SmallIntegerField(primary_key=True)
    name = peewee.CharField(max_length=20)
    last_update = peewee.TimestampField()

    class Meta:
        db_table = 'language'


class Film(BaseModel):
    """filmテーブル用モデル."""

    film_id = peewee.SmallIntegerField(primary_key=True)
    title = peewee.CharField(index=True)
    description = peewee.TextField(null=True)
    release_year = peewee.DateField(formats="%Y")
    # 外部キー
    language = peewee.ForeignKeyField(Language)
    length = peewee.SmallIntegerField()
    last_update = peewee.TimestampField()

    def to_dict(self):
        return {
            'film_id': self.film_id,
            'title': self.title,
            'description': self.description,
            'release_year': self.release_year,
            'language': self.language.name,
            'length': self.length,
            'last_update': self.last_update.isoformat(),
        }

    class Meta:
        db_table = 'film'
