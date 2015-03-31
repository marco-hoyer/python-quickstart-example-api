# python-quickstart-example-api

This project is intended as a simple example on how to implement a restful api with python flask.

## Quickstart

### Prepare environment
Create a virtualenv if you don't already have one and install required dependencies.
```
virtualenv .venv
source .venv/bin/activate
pip install pip pybuilder --upgrade
pyb install_dependencies
```

### Run tests
Run all unittests in this project.
```
source .venv/bin/activate
pyb verify
```

### Build project
Run tests and build project if successful.
```
source .venv/bin/activate
pyb
```