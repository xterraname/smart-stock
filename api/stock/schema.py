from ninja import Schema

class Point(Schema):
    x: float
    y: float

class WerehouseOut(Schema):
    name: str
    location: Point
