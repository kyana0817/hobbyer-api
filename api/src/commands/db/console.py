import subprocess
from config.enviroment import (
  DATABASE_USERNAME,
  DATABASE_PASSWORD,
  DATABASE_URL,
  DATABASE_NAME
)

client = 'mysql -h {host} -u{username} -p{password} {db_name}'

def exec(*args, **kwargs):
  subprocess.run(client.format(
    host=DATABASE_URL,
    username=DATABASE_USERNAME,
    password=DATABASE_PASSWORD,
    db_name=DATABASE_NAME
  ), shell=True)