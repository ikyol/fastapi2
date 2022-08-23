from curses import meta
from .jobs import jobs
from .accounts import users
from .base import metadata, engine

metadata.create_all(bind=engine)
