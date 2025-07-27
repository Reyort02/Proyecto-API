import json
from src.models.user import UserCreate
from src.security.password import get_password_hash

USER_DB_FILE = "src/data/users.json"

def get_users():
    try:
        with open(USER_DB_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_users(users):
    with open(USER_DB_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register_user(user: UserCreate):
    users = get_users()
    if any(u['email'] == user.email for u in users):
        return None
    hashed_password = get_password_hash(user.password)
    user_data = user.model_dump()
    user_data['password'] = hashed_password
    users.append(user_data)
    save_users(users)
    return user_data
