from db import BaseModel, CharField, IntegerField


class Person(BaseModel):
    name = CharField(max_length=30)
    age = IntegerField()

    def __str__(self):
        return f"{self.name} {self.age}"


class Post(BaseModel):
    title = ""
    content = ""

