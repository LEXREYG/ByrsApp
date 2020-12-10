from typing import  Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    balance: int

database_users = Dict[str, UserInDB]

database_users = {
    "lunarvaezc": UserInDB(**{"username":"lunarvaezc4",
                            "password":"3152",
                            "balance":4000000}),

    "subtitular": UserInDB(**{"username":"subtitular",
                            "password":"3202",
                            "balance":4000000}),
    
    "didierpasuy": UserInDB(**{"username":"didierpasuy",
                            "password":"3184",
                            "balance":4000000}),
    
    "aleksander": UserInDB(**{"username":"aleksander",
                            "password":"3192",
                            "balance":4000000}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db
