# /home/user/app/wsgi.py
# From app/ dir import app.py
from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0")
