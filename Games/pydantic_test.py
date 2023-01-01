from dataclasses import dataclass, field
from pydantic import BaseModel
from datetime import datetime


@dataclass()
class User():
    id: int
    name = 'John Doe'
    signup_ts: datetime | None = None
    friends: list[int] = field(default_factory=list)


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3']
}
user = User(**external_data)
user.id = 1
print(user.id)
