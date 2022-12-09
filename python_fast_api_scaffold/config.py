import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="python_fast_api_scaffold",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="python_fast_api_scaffold_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from python_fast_api_scaffold.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export python_fast_api_scaffold_KEY=value
export python_fast_api_scaffold_KEY="@int 42"
export python_fast_api_scaffold_KEY="@jinja {{ this.db.uri }}"
export python_fast_api_scaffold_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
python_fast_api_scaffold_ENV=production python_fast_api_scaffold run
```

Read more on https://dynaconf.com
"""
