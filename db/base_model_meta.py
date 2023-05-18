from db.manager import Manager


class BaseModelMeta(type):
    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        if name != 'BaseModel':
            new_class._id_counter = 1
            new_class.objects = Manager(new_class)
        return new_class
