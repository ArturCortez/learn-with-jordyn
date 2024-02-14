import random


def generate_weather_data(num_days: int) -> list:
    if not isinstance(num_days, int):
        raise TypeError("Number of days must be a integer.")

    weather_data = []

    for number in range(num_days):
        temp_of_day = (random.randrange(200, 400, 1) / 10)
        humidity_of_day = random.randrange(30, 90, 1)
        single_day_data = dict(day=number, temp=temp_of_day, humidity=humidity_of_day)
        weather_data.append(single_day_data)

    return weather_data


def filter_data(weather_data: list, temp_threshold: int) -> list:
    if not isinstance(weather_data, list):
        raise TypeError("Weather data must be a list")
    if not isinstance(temp_threshold, int):
        raise TypeError("Temperature Threshold must be an integer")

    list_after_threshold = []

    for day in weather_data:
        try:
            if day.get('temp', 0) > temp_threshold:
                list_after_threshold.append(day.get('temp'))
        except Exception as e:
            print(f"Exception occurred: {e}")

    if len(list_after_threshold) == 0:
        print("No values greater than threshold")

    return list_after_threshold


def calculate_average_humidity(weather_data: list) -> float:
    humidity_set = set(())  # I use set because they dont hold duplicate values. Duplicate values dont change averages
    for day in weather_data:
        try:
            humidity_set.add(day.get('humidity'))
        except Exception as e:
            print(f"Exception occurred: {e}")

    return sum(humidity_set) / len(humidity_set)  # I prefer set methods because they are more readable


def sort_by_temp(element: any):
    return element['temp']


def sort_data_by_temperature(weather_data: list) -> list:
    sorted_data = sorted(weather_data, key=sort_by_temp, reverse=True)

    return sorted_data


def take_user_input_for_temp(weather_data):
    int_temp = int(input("What is the temperature threshold?\n"))
    try:

        if int_temp > 40 or int_temp < 20:
            raise ValueError("This value is out of range")

        return int_temp

    except ValueError:
        print("wrong input, insert number for temperature threshold")
        return take_user_input_for_temp(weather_data)

    except Exception as e:
        print(f"Error: {e}")
        print("Try again")
        return take_user_input_for_temp(weather_data)


def main():
    weather_data = generate_weather_data(30)
    temp_threshold = take_user_input_for_temp(weather_data)
    filtered_data = filter_data(weather_data, temp_threshold)
    average_humidity = calculate_average_humidity(weather_data)
    sorted_data = sort_data_by_temperature(weather_data)

    # Display results
    print(f"Original Data: {weather_data}")
    print(f"Filtered Data (Temperature > {temp_threshold}): {filtered_data}")
    print(f"Average Humidity: {average_humidity:.2f}%")
    print(f"Sorted Data by Temperature: {sorted_data}")


if __name__ == "__main__":
    main()
