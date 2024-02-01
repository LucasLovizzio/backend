def user_schema(user) -> dict:
    return {"id": str(user["_id"]),             # el nombre de la clave unica que crea mongo db es "_id"
            "username": user["username"],
            "email": user["email"]}

def users_schema(users) -> list:
    return [user_schema(user) for user in users]

