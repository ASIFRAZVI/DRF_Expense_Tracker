from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

def get_db_settings():
    db_type = os.getenv("DB_TYPE")

    if db_type == "development":
        return {
            'default': {
                'ENGINE': os.getenv("DEV_DB_ENGINE"),
                'NAME': os.getenv("DEV_DB_NAME"),
                'USER': os.getenv("DEV_DB_USER"),
                'PASSWORD': os.getenv("DEV_DB_PASSWORD"),
                'HOST': os.getenv("DEV_DB_HOST"),
                'PORT': os.getenv("DEV_DB_PORT"),
            }
        }
    elif db_type == "production":
        return {
            'default': {
                'ENGINE': os.getenv("PROD_DB_ENGINE"),
                'NAME': os.getenv("PROD_DB_NAME"),
                'USER': os.getenv("PROD_DB_USER"),
                'PASSWORD': os.getenv("PROD_DB_PASSWORD"),
                'HOST': os.getenv("PROD_DB_HOST"),
                'PORT': os.getenv("PROD_DB_PORT"),
            }
        }
    else:
        return {}