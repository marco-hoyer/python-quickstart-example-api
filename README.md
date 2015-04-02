# python-quickstart-example-api

This project is intended to be a simple example on how to implement a restful api with python flask.
It implements a kind of instance inventory, allowing to get a list of all registered instances and do CRUD on a single instance.

## Quickstart

### Prepare environment
Create a virtualenv if you don't already have one.
```
virtualenv .venv
source .venv/bin/activate
```

Install required dependencies.
 ```
pip install pip pybuilder --upgrade
pyb install_dependencies
```

### Run tests
Run all unittests in this project.
```
pyb verify
```

### Build project
Run tests and build project if successful.
```
pyb
```