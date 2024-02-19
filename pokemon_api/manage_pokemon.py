"""
This code will ask for user input and send the information to the script that will make the request.
"""
from api_manager import get_pokemon_data


def print_pokemon_data(pokemon):
    print(f"\n\tname: {pokemon['name'].title()}\n")

    print(f"\tType:")
    for element in pokemon['types']:
        print(f"\t\t{element.get('type').get('name')}")
    print("\tAbilities:")
    for element in pokemon['abilities']:
        print(f"\t\t{element.get('ability').get('name')}")

    print("\tStats:")
    for element in pokemon['stats']:
        print(f"\t\t{element.get('stat').get('name')}: {element.get('base_stat')}")


def get_pokemon_name() -> str:
    while True:
        pokemon_name = input("Which pokemon you want to find? ").lower()
        if isinstance(pokemon_name, str):

            try:
                pokemon = get_pokemon_data(pokemon_name)
                if pokemon is None:
                    raise TypeError("Name of the Pokemon return empty. \n")
                print_pokemon_data(pokemon)
                answer = input("Look for another Pokemon? (y/n)")
                if not (answer.isalpha() and answer.lower() == "y"):
                    return "User decided to terminate the program"

            except TypeError as te:
                print(f"Type error: {te}")
                answer = input("Try it again? (y/n)")
                if not (answer.isalpha() and answer.lower() == "y"):
                    return "User decided to terminate the program"
            except Exception as e:
                print(f"Exception Happened: {e}")
                return "Unexpected error occurred"

        print("Please, type name again")


if __name__ == "__main__":
    get_pokemon_name()
