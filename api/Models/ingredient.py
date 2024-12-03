from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    cost = Column(Float, nullable=False)
    calories = Column(Integer, nullable=False)
    is_healthy = Column(Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'cost': self.cost,
            'calories': self.calories,
            'is_healthy': self.is_healthy
        }
