# FastAPI Project Template

The base to start an openapi project featuring: SQLModel, Typer, FastAPI, JWT Token Auth, Interactive Shell, Management Commands. 

See also

-  [Python-Project-Template](https://github.com/rochacbruno/python-project-template/) for a lean, low dependency Python app.
-  [Flask-Project-Template](https://github.com/rochacbruno/flask-project-template/) for a full feature Flask project including database, API, admin interface, etc.


### HOW TO USE THIS TEMPLATE

> **DO NOT FORK** this is meant to be used from **[Use this template](https://github.com/rochacbruno/fastapi-project-template/generate)** feature.

1. Click on **[Use this template](https://github.com/rochacbruno/fastapi-project-template/generate)**
3. Give a name to your project  
   (e.g. `my_awesome_project` recommendation is to use all lowercase and underscores separation for repo names.)
3. Wait until the first run of CI finishes  
   (Github Actions will process the template and commit to your new repo)
4. If you want [codecov](https://about.codecov.io/sign-up/) Reports and Automatic Release to [PyPI](https://pypi.org)  
  On the new repository `settings->secrets` add your `PIPY_API_TOKEN` and `CODECOV_TOKEN` (get the tokens on respective websites)
4. Read the file [CONTRIBUTING.md](CONTRIBUTING.md)
5. Then clone your new project and happy coding!

> **NOTE**: **WAIT** until first CI run on github actions before cloning your new project.

### What is included on this template?

- 🖼️ The base to start an openapi project featuring: SQLModel, Typer, FastAPI, VueJS.
- 📦 A basic [setup.py](setup.py) file to provide installation, packaging and distribution for your project.  
  Template uses setuptools because it's the de-facto standard for Python packages, you can run `make switch-to-poetry` later if you want.
- 🤖 A [Makefile](Makefile) with the most useful commands to install, test, lint, format and release your project.
- 📃 Documentation structure using [mkdocs](http://www.mkdocs.org)
- 💬 Auto generation of change log using **gitchangelog** to keep a HISTORY.md file automatically based on your commit history on every release.
- 🐋 A simple [Containerfile](Containerfile) to build a container image for your project.  
  `Containerfile` is a more open standard for building container images than Dockerfile, you can use buildah or docker with this file.
- 🧪 Testing structure using [pytest](https://docs.pytest.org/en/latest/)
- ✅ Code linting using [flake8](https://flake8.pycqa.org/en/latest/)
- 📊 Code coverage reports using [codecov](https://about.codecov.io/sign-up/)
- 🛳️ Automatic release to [PyPI](https://pypi.org) using [twine](https://twine.readthedocs.io/en/latest/) and github actions.
- 🎯 Entry points to execute your program using `python -m <python_fast_api_scaffold>` or `$ python_fast_api_scaffold` with basic CLI argument parsing.
- 🔄 Continuous integration using [Github Actions](.github/workflows/) with jobs to lint, test and release your project on Linux, Mac and Windows environments.

> Curious about architectural decisions on this template? read [ABOUT_THIS_TEMPLATE.md](ABOUT_THIS_TEMPLATE.md)  
> If you want to contribute to this template please open an [issue](https://github.com/rochacbruno/fastapi-project-template/issues) or fork and send a PULL REQUEST.

[❤️ Sponsor this project](https://github.com/sponsors/rochacbruno/)

<!--  DELETE THE LINES ABOVE THIS AND WRITE YOUR PROJECT README BELOW -->

---
# python_fast_api_scaffold

[![codecov](https://codecov.io/gh/pruthvi2103/python_fast_api_scaffold/branch/main/graph/badge.svg?token=python_fast_api_scaffold_token_here)](https://codecov.io/gh/pruthvi2103/python_fast_api_scaffold)
[![CI](https://github.com/pruthvi2103/python_fast_api_scaffold/actions/workflows/main.yml/badge.svg)](https://github.com/pruthvi2103/python_fast_api_scaffold/actions/workflows/main.yml)

Awesome python_fast_api_scaffold created by pruthvi2103

## Install

from source
```bash
git clone https://github.com/pruthvi2103/python_fast_api_scaffold python_fast_api_scaffold
cd python_fast_api_scaffold
make install
```

from pypi

```bash
pip install python_fast_api_scaffold
```

## Executing

```bash
$ python_fast_api_scaffold run --port 8080
```

or

```bash
python -m python_fast_api_scaffold run --port 8080
```

or

```bash
$ uvicorn python_fast_api_scaffold:app
```

## CLI

```bash
❯ python_fast_api_scaffold --help
Usage: python_fast_api_scaffold [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  create-user  Create user
  run          Run the API server.
  shell        Opens an interactive shell with objects auto imported
```

### Creating a user

```bash
❯ python_fast_api_scaffold create-user --help
Usage: python_fast_api_scaffold create-user [OPTIONS] USERNAME PASSWORD

  Create user

Arguments:
  USERNAME  [required]
  PASSWORD  [required]

Options:
  --superuser / --no-superuser  [default: no-superuser]
  --help 
```

**IMPORTANT** To create an admin user on the first run:

```bash
python_fast_api_scaffold create-user admin admin --superuser
```

### The Shell

You can enter an interactive shell with all the objects imported.

```bash
❯ python_fast_api_scaffold shell       
Auto imports: ['app', 'settings', 'User', 'engine', 'cli', 'create_user', 'select', 'session', 'Content']

In [1]: session.query(Content).all()
Out[1]: [Content(text='string', title='string', created_time='2021-09-14T19:25:00.050441', user_id=1, slug='string', id=1, published=False, tags='string')]

In [2]: user = session.get(User, 1)

In [3]: user.contents
Out[3]: [Content(text='string', title='string', created_time='2021-09-14T19:25:00.050441', user_id=1, slug='string', id=1, published=False, tags='string')]
```

## API

Run with `python_fast_api_scaffold run` and access http://127.0.0.1:8000/docs

![](https://raw.githubusercontent.com/rochacbruno/fastapi-project-template/master/docs/api.png)


**For some api calls you must authenticate** using the user created with `python_fast_api_scaffold create-user`.

## Testing

``` bash
❯ make test
Black All done! ✨ 🍰 ✨
13 files would be left unchanged.
Isort All done! ✨ 🍰 ✨
6 files would be left unchanged.
Success: no issues found in 13 source files
================================ test session starts ===========================
platform linux -- Python 3.9.6, pytest-6.2.5, py-1.10.0, pluggy-1.0.0 -- 
/fastapi-project-template/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /fastapi-project-template
plugins: cov-2.12.1
collected 10 items                                                                                                                               

tests/test_app.py::test_using_testing_db PASSED                           [ 10%]
tests/test_app.py::test_index PASSED                                      [ 20%]
tests/test_cli.py::test_help PASSED                                       [ 30%]
tests/test_cli.py::test_cmds_help[run-args0---port] PASSED                [ 40%]
tests/test_cli.py::test_cmds_help[create-user-args1-create-user] PASSED   [ 50%]
tests/test_cli.py::test_cmds[create-user-args0-created admin2 user] PASSED[ 60%]
tests/test_content_api.py::test_content_create PASSED                     [ 70%]
tests/test_content_api.py::test_content_list PASSED                       [ 80%]
tests/test_user_api.py::test_user_list PASSED                             [ 90%]
tests/test_user_api.py::test_user_create PASSED                           [100%]

----------- coverage: platform linux, python 3.9.6-final-0 -----------
Name                              Stmts   Miss  Cover
-----------------------------------------------------
python_fast_api_scaffold/__init__.py              4      0   100%
python_fast_api_scaffold/app.py                  16      1    94%
python_fast_api_scaffold/cli.py                  21      0   100%
python_fast_api_scaffold/config.py                5      0   100%
python_fast_api_scaffold/db.py                   10      0   100%
python_fast_api_scaffold/models/__init__.py       0      0   100%
python_fast_api_scaffold/models/content.py       47      1    98%
python_fast_api_scaffold/routes/__init__.py      11      0   100%
python_fast_api_scaffold/routes/content.py       52     25    52%
python_fast_api_scaffold/routes/security.py      15      1    93%
python_fast_api_scaffold/routes/user.py          52     26    50%
python_fast_api_scaffold/security.py            103     12    88%
-----------------------------------------------------
TOTAL                               336     66    80%


========================== 10 passed in 2.34s ==================================

```

## Linting and Formatting

```bash
make lint  # checks for linting errors
make fmt   # formats the code
```


## Configuration

This project uses [Dynaconf](https://dynaconf.com) to manage configuration.

```py
from python_fast_api_scaffold.config import settings
```

## Acessing variables

```py
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Defining variables

### On files

settings.toml

```toml
[development]
dynaconf_merge = true

[development.db]
echo = true
```

> `dynaconf_merge` is a boolean that tells if the settings should be merged with the default settings defined in python_fast_api_scaffold/default.toml.

### As environment variables
```bash
export python_fast_api_scaffold_KEY=value
export python_fast_api_scaffold_KEY="@int 42"
export python_fast_api_scaffold_KEY="@jinja {{ this.db.uri }}"
export python_fast_api_scaffold_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Secrets

There is a file `.secrets.toml` where your sensitive variables are stored,
that file must be ignored by git. (add that to .gitignore)

Or store your secrets in environment variables or a vault service, Dynaconf
can read those variables.

### Switching environments

```bash
python_fast_api_scaffold_ENV=production python_fast_api_scaffold run
```

Read more on https://dynaconf.com

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
