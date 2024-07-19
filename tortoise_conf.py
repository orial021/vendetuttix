TORTOISE_ORM = {
    "connections": {
        "default": "postgres://postgres:2354@localhost:5432/fastAPI"
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"], 
            "default_connection": "default",
        },
    },
}

'''TORTOISE_ORM = {
    "connections": {
        "default": "postgres://jairo:2354@localhost:5432/fastapi"
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"], 
            "default_connection": "default",
        },
    },
}'''