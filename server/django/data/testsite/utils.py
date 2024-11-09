from enum import Enum
import redis
from testsite.settings import REDIS_HOST, REDIS_PORT
from django.contrib.auth.models import User

KEY_LOGIN = "last_login"
KEY_EMAIL = "last_email"
KEY_THEME = "theme"
DEFAULT_THEME = "light"
DARK_THEME = "dark"


class Themes:
    default = 0
    themes = {0: "light", 1: "dark"} 
    @classmethod
    def get_theme_name(cls, val):
        return cls.themes.get(val, cls.themes[cls.default])


def connect() -> redis.Redis:
    return redis.StrictRedis(host=REDIS_HOST, 
                             port=REDIS_PORT, 
                             decode_responses=True)

def get_theme_from_redis(user: User) -> int:
    theme = None
    if user.is_authenticated:
        rdb = connect()
        theme = rdb.hget(user.username, KEY_THEME)
    if theme is None:
        theme = Themes.default
    return int(theme)
       
def get_theme_name(user: User):
    theme = get_theme_from_redis(user)
    return Themes.get_theme_name(theme)
        
def set_last_user(user: User):
    rdb = connect()
    rdb.set(KEY_LOGIN, user.username)
    rdb.set(KEY_EMAIL, user.email)
    
def get_last_user():
    rdb = connect()
    username = rdb.get(KEY_LOGIN)
    email = rdb.get(KEY_EMAIL)
    return username, email

def save_theme_to_user(user: User, theme: bool = False):
    rdb = connect()
    rdb.hset(user.username, KEY_THEME, int(theme))