from lib.data import aggregate_weather_data, get_top_location

if __name__ == '__main__':
    data = aggregate_weather_data()
    date, top_location = get_top_location(data)
    print(f"Time: {date}\r\n"
          f"Location: {top_location["name"]}\r\n"
          f"Humidity: {top_location["humidity"]}\r\n"
          f"Coordinates: {top_location["coordinates"]}")
