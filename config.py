from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import (
    AliasChoices,
    AmqpDsn,
    BaseModel,
    Field,
    ImportString,
    PostgresDsn,
    RedisDsn,
)


class Settings(BaseModel):
    db_url: str
    db_test_url: str
    redis_url: RedisDsn
    model_config = SettingsConfigDict(env_file=('.env', '.env.prod'), env_file_encoding='utf-8')


print(Settings())
