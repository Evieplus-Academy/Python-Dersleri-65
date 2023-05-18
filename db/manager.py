import os
import json
import glob


class Manager:
    def __init__(self, model_class):
        self.model_class = model_class

    def get(self, **kwargs):
        for key, value in kwargs.items():
            if key == "pk":
                storage_file = os.path.join(self._check_storage_folder(), f"{value}.json")
                if os.path.exists(storage_file):
                    with open(storage_file, "r") as file_object:
                        data = json.load(file_object)
                        instance = self.model_class(**data)
                        return instance

    def all(self):
        storage_files = glob.glob(os.path.join(self._check_storage_folder(), "*.json"))
        instances = []
        for storage_file in storage_files:
            with open(storage_file, "r") as file_object:
                data = json.load(file_object)
                instances.append(self.model_class(**data))
        return instances

    def _check_storage_folder(self):
        storage_folder = os.path.join("dbo", self.model_class.__name__.lower() + "s")
        os.makedirs(storage_folder, exist_ok=True)
        return storage_folder
