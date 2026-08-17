# Chapter 42: GIS and PostGIS

Tina4 stores geographic points in PostGIS, queries distance in metres, and serializes map-ready GeoJSON. Coordinates are always `(longitude, latitude)`.

```python
from tina4_python.orm import ORM, IntegerField, StringField
from tina4_python.orm import PointField, Point, feature_collection

class ChargePoint(ORM):
    id = IntegerField(primary_key=True, auto_increment=True)
    name = StringField()
    location = PointField()

site = ChargePoint({"name": "V&A Waterfront", "location": Point(18.4241, -33.9249)})
site.save()

nearby = (ChargePoint.query()
    .within_distance("location", (18.42, -33.92), 5_000)
    .select_distance("location", (18.42, -33.92))
    .order_by_distance("location", (18.42, -33.92))
    .get())

collection = feature_collection([site])
```

`PointField()` creates a `geography(Point,4326)` column and a GiST index. Radius and returned distance are metres. Unsupported databases fail clearly instead of pretending a text column is spatial.

`Point.parse()` accepts a coordinate pair, WKT/EWKT, GeoJSON, or WKB/EWKB without guessing coordinate order.
