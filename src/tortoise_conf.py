TORTOISE_ORM = {
    "connections": {
        "default": "postgres://postgres:Italo1234*@localhost:5432/fastApi"
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"], 
            "default_connection": "default",
        },
    },
}