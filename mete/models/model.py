import json
from decimal import Decimal, ROUND_HALF_UP

class Model(object):

    @classmethod
    def round_decimal(self, x):
        return Decimal.from_float(x).quantize(Decimal(".01"), rounding=ROUND_HALF_UP)

    @classmethod
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def to_JSON(self):
        return json.dumps(self.as_dict, default=lambda o: o.__dict__,
                sort_keys=True, indent=4)

