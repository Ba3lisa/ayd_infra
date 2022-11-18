from django.urls import include, path
from app.bot.views import BotWebhook

url_patterns = [
    path('', BotWebhook.as_view(), name='bot_webhook'),
]

