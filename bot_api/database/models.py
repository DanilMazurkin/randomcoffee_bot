from tortoise.models import Model
from tortoise import fields


class TelegramUser(Model):
    """Модель TelegramUser."""
    id = fields.IntField(pk=True)
    chat_id = fields.TextField()
