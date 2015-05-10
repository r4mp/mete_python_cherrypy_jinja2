import json

class Model(object):

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def to_JSON(self):
        return json.dumps(self.as_dict, default=lambda o: o.__dict__,
                sort_keys=True, indent=4)

