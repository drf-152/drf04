# drf04

git clone https://github.com/drf-152/drf04.git

cd drf04

mkvirtualenv drf04-venv

setvirtualenvproject

pip install -r requirements.txt

./manage.py runserver

http://127.0.0.1:8000/admin/
login - admin
password - password

curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/v1/feed/
