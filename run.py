# /run.py
import os
from dotenv import load_dotenv, find_dotenv

from src.app import create_app

load_dotenv(find_dotenv())

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

if __name__ == '__main__':
  #port = os.getenv('PORT')
  port = 5000
  # run app
  app.run(host='127.0.0.1', port=port)


