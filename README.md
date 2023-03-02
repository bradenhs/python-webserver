# Getting Started

## Requirements

- [Python](https://www.python.org/downloads/)
- Code Editor (recommendation: [VSCode](https://code.visualstudio.com/))
- [Git](https://git-scm.com/) (alternatively you can download project as a zip from https://github.com/bradenhs/python-webserver/archive/refs/heads/main.zip)

## Download project and open in code editor

Run this (one line at a time) in your terminal:

```sh
git clone https://github.com/bradenhs/python-webserver.git
code python-webserver
```

Follow VSCode's prompt to install some extensions if you don't already have them.

## Run locally

Open a VSCode terminal to run these commands.

### Setup Python Virtual Environment

```sh
python3 -m venv venv
source venv/bin/activate
```

This allows you to have individual dependencies installed per project.

### Install project dependencies

```sh
pip install -r requirements.txt
```

Once in the virtual environment this command will install project dependencies in the `./venv` directory.

### Start server

```sh
flask --app server run
```

It will start on http://localhost:5000

### Run Python Client

```sh
python3 ./client.py
```

Make a couple sample calls to the server from a Python script.

### Open Web Client

```sh
open http://localhost:5000
```

Interact with the API via a web page.

## Helpful resources

- [Flask documentation](https://flask.palletsprojects.com/en/2.2.x/)
- [Flask deployment recommendations](https://flask.palletsprojects.com/en/2.2.x/deploying/)
- [SQLite in Python documentation](https://docs.python.org/3/library/sqlite3.html)
