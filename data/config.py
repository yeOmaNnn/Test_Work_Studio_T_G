from decouple import config



DATABASE_NAME = config("DATABASE_NAME", default="minesweeper_db")
DATABASE_USER_NAME = config("DATABASE_USER_NAME", default="postgres")
DATABASE_USER_PASSWORD = config("DATABASE_USER_PASSWORD", default="")
DATABASE_HOST = config("DATABASE_HOST", default="localhost")
DATABASE_PORT = config("DATABASE_PORT", default=6432, cast=int)

if len(DATABASE_USER_PASSWORD) > 0:
    DATABASE_USER_DATA = f"{DATABASE_USER_NAME}:{DATABASE_USER_PASSWORD}"
else:
    DATABASE_USER_DATA = f"{DATABASE_USER_NAME}"

if DATABASE_PORT > 0:
    DATABASE_PORT_AND_HOST = f"{DATABASE_HOST}:{DATABASE_PORT}"
else:
    DATABASE_PORT_AND_HOST = f"{DATABASE_HOST}"

DATABASE_URL = f"postgresql+asyncpg://{DATABASE_USER_DATA}@{DATABASE_PORT_AND_HOST}/{DATABASE_NAME}"
