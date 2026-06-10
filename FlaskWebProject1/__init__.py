"""
The flask application package.
"""

import os

from flask import Flask
import mysql.connector
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()


def get_db_connection():
    required_env = {
        "MYSQL_HOST": os.environ.get("MYSQL_HOST"),
        "MYSQL_DATABASE": os.environ.get("MYSQL_DATABASE"),
        "MYSQL_USER": os.environ.get("MYSQL_USER"),
        "MYSQL_PASSWORD": os.environ.get("MYSQL_PASSWORD"),
    }
    missing = [name for name, value in required_env.items() if not value]
    if missing:
        raise RuntimeError(
            "Missing required MySQL environment variables: "
            + ", ".join(missing)
        )
    port_value = os.environ.get("MYSQL_PORT", "3306")
    return mysql.connector.connect(
        host=required_env["MYSQL_HOST"],
        port=int(port_value),
        database=required_env["MYSQL_DATABASE"],
        user=required_env["MYSQL_USER"],
        password=required_env["MYSQL_PASSWORD"],
    )
