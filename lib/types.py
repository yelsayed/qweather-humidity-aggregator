from typing import TypedDict, Tuple, Dict, List


class Location(TypedDict):
    name: str
    coordinates: Tuple[float, float]


class WeatherResult(TypedDict):
    name: str
    coordinates: Tuple[float, float]
    humidity: float
