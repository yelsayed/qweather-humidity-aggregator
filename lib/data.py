import collections
import concurrent
import http.client
import json
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Tuple, Union

from lib.constants import BASE_PATH, BASE_URL, LOCATIONS, Location
from lib.types import WeatherResult


def fetch_weather_data(location: Location):
    conn = http.client.HTTPSConnection(BASE_URL)
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
        'Connection': 'keep-alive',
        'Origin': 'https://qweather.gov.qa',
        'Referer': 'https://qweather.gov.qa/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/131.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A '
                     'Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }
    lat, lng = location["coordinates"]
    conn.request("GET", f"{BASE_PATH}/{lat}/{lng}/", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")


def process_result(
        data: str,
        location: Location,
        results: Dict[str, List[WeatherResult]]
):
    parsed_data = json.loads(data)
    records = parsed_data["Records"]

    for record in records:
        date = record["OrigDate"]
        weather_results = results[date]
        weather_result: WeatherResult = {
            "name": location["name"],
            "coordinates": location["coordinates"],
            "humidity": record["RH"]
        }

        weather_results.append(weather_result)


def aggregate_weather_data() -> Dict[str, List[WeatherResult]]:
    """
    Aggregates all the weather data for the next 3 days into one data structure
    """
    results: Dict[str, List[WeatherResult]] = collections.defaultdict(list)
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_humidity = {
            executor.submit(fetch_weather_data, location): location for location
            in LOCATIONS
        }

        for future in concurrent.futures.as_completed(future_to_humidity):
            location = future_to_humidity[future]
            try:
                data = future.result()
                process_result(data, location, results)
            except Exception as exc:
                print('%r generated an exception: %s' % (data, exc))

    return results


def get_top_location(data: Dict[str, List[WeatherResult]]) \
        -> Tuple[str, WeatherResult]:
    """
    Gets the locations with the top humidity from the aggregrated data.
    """
    top_results: Dict[str, WeatherResult] = {}

    for date, results in data.items():
        max_humidity = -1
        top_weather_result: Union[WeatherResult, None] = None

        for weather_result in results:
            if weather_result["humidity"] > max_humidity:
                max_humidity = weather_result["humidity"]
                top_weather_result = weather_result

        top_results[date] = top_weather_result

    max_humidity = -1
    top_location_result: Union[Tuple[str, WeatherResult], None] = None

    for date, result in top_results.items():
        if result["humidity"] > max_humidity:
            top_location_result = (date, result)
            max_humidity = result["humidity"]

    return top_location_result
