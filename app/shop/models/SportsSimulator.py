from shop.models.BaseModel import BaseModel


class SportsSimulator(BaseModel):
    ...

    def __str__(self):
        return f"{self.brand} {self.model} - {self.price}"
