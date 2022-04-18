def userEntity(item) -> dict:
    return {**item, "id": str(item["id"])}


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
