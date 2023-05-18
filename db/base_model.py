import os
import json
from db.base_model_meta import BaseModelMeta
from db.types.char_field import CharField
from db.types.integer_field import IntegerField
from db.manager import Manager


class BaseModel(metaclass=BaseModelMeta):
    def __init__(self, _id=None, **kwargs):
        if _id is None:
            self._id = None
        else:
            self._id = _id

        for key, value in kwargs.items():
            field = getattr(self.__class__, key)
            if isinstance(field, CharField):
                if not isinstance(value, str):
                    raise ValueError(f"Value '{value}' for field '{key}' must be 'str'.")
                if len(value) > field.max_length:
                    raise ValueError(f"Value '{value}' for field '{key}' exceeds the maximum length of {field.max_length}.")
            elif isinstance(field, IntegerField):
                if not isinstance(value, int):
                    raise ValueError(f"Value '{value}' for field '{key}' must be 'int'.")
            setattr(self, key, value)

    def save(self):
        if self._id is None:
            self._id = self.__class__._id_counter
            self.__class__._id_counter += 1

        storage_file = os.path.join(self.objects._check_storage_folder(),
                                    f"{self._id}.json")

        with open(storage_file, "w") as file_object:
            json.dump(self._model_to_dict(), file_object)

    def __str__(self):
        return f"<{self.__class__.__name__}>"

    def _model_to_dict(self):
        model_dict = {}
        for key, value in self.__dict__.items():
            model_dict[key] = value
        return model_dict
