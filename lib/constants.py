from typing import List

from lib.types import Location

BASE_URL = "www.qmet.com.qa"
BASE_PATH = "/metservices/api/Nwp/GetWrf4"


LOCATIONS: List[Location] = [
    {
        "name": "الشحانية",
        "coordinates": (25.382377, 51.234991)
    },
    {
        "name": "العوينة",
        "coordinates": (25.464237, 50.924628)
    },
    {
        "name": "دخان",
        "coordinates": (25.429515, 50.779059)
    },
    {
        "name": "أم باب",
        "coordinates": (25.211036, 50.806525)
    },
    {
        "name": "مسيعيد",
        "coordinates": (24.997143, 51.561835)
    },
    {
        "name": "الخور",
        "coordinates": (25.714432, 51.506903)
    },
    {
        "name": "الظاهرة",
        "coordinates": (25.885055, 51.545355)
    },
    {
        "name": "الغويرية",
        "coordinates": (25.850456, 51.251471)
    },
    {
        "name": "الزبارة",
        "coordinates": (25.978917, 51.048224)
    }
]
