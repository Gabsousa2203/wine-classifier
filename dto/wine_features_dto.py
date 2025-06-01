from typing import Optional
from pydantic import BaseModel


class WineFeaturesDict(BaseModel):
    fixed_acidity: Optional[float] = None
    volatile_acidity: Optional[float] = None
    citric_acid: Optional[float] = None
    residual_sugar: Optional[float] = None
    chlorides: Optional[float] = None
    free_sulfur_dioxide: Optional[float] = None
    total_sulfur_dioxide: Optional[float] = None
    density: Optional[float] = None
    pH: Optional[float] = None
    sulphates: Optional[float] = None
    alcohol: Optional[float] = None
    wine_type: str