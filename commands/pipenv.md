### Pipenv commands 👩🏻‍💻

Install
```shell
brew install pipenv
```

Activate
```shell
pipenv shell (generally create env and activate if not specify)
```
```shell
pipenv run
```
> Always run commands in project root dir

Deactivate 
```shell
source deactivate
# or
deactivate
```

Create env with python version
```shell
pipenv —python 3.12.2
```

Remove env
```shell
pipenv --rm
```

Install requirement
```shell
pipenv install -r requirement.txt
```
or
```shell
pipenv install . (if project has setup.py) 
```

List out all env in project
```shell
pipenv —venv
```

If pipenv shell not working — create alias
— try source deactivate or reopen vscode to detect new env 
```shell
source $(pipenv --venv)/bin/activate
```
or
```shell
source $(dirname $(pipenv run which python))/activate
```
