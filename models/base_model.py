from dataclasses import asdict


class BaseModel:
    """
    Base model for all project models.
    Provides common utility methods.
    """

    def to_dict(self):
        return asdict(self)

    def __str__(self):
        return str(self.to_dict())