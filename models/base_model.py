import uuid
from datetime import datetime
import json


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def save_to_file(self):
        """
        Serialize the object to a JSON string and save it to a file.
        """
        with open(f"{self.__class__.__name__}_{self.id}.json", 'w') as file:
            json.dump(self.to_dict(), file)

    def load_from_file(self, file_path):
        """
        Load the object from a file and deserialize it.
        """
        with open(file_path, 'r') as file:
            data = json.load(file)
            return self.__class__(**data)
