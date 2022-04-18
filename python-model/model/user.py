import uuid
from dataclasses import dataclass, field


@dataclass
class User:
    id: str = field(init=False)
    firstname: str
    lastname: str
    email: str
    password: str
    add: str
    pos: str

    def set_id(self):
        self.id = uuid.uuid4()

    def get_id(self) -> str:
        return self.id

    def to_obj(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "address": self.add,
            "pos": self.pos,
        }
