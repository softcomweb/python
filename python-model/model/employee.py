import uuid
from dataclasses import dataclass, field


@dataclass
class EmployeeModel:
    id: str = field(init=False)
    pk: str = field(init=False)
    sk: str = field(init=False)
    LoginAlias: str
    Firstname: str
    Lastname: str
    ManagerLoginAlias: str
    Skills: list

    def __post_init__(self):
        self.id = uuid.uuid4()
        self.pk = self.LoginAlias

    def get_id(self) -> str:
        return self.id

    def get_pk(self) -> str:
        return self.pk

    def to_object(self):
        return {
            "id": str(self.id),
            "pk": self.LoginAlias,
            "LoginAlias": self.LoginAlias,
            "Firstname": self.Firstname,
            "Lastname": self.Lastname,
            "ManagerLoginAlias": self.ManagerLoginAlias,
            "Skills": self.Skills,
        }
