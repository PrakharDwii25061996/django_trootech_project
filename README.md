
## Steps to setup project for Windows 11

1. Create and activate virtualenv
```
python -m venv venv
./venv/Scripts/Activaate
```

2. Install project requirements
```
pip install -r requirements.txt
```

3. Run the migrate commands
```
python manage.py makemigrations
python manage.py migrate
```

4. Run the local server
```
python manage.py runserver
```

5. Run the test cases
```
python manage.py test playlist.tests.test_playlists
```

