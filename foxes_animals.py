import json


def load_data(filepath):
    with open(filepath) as f:
        return json.load(f)


def print_animals_attributes():
    """Read animal name, diet, location and type from json-file and print them if it exists"""
    animals_data = load_data("animals_data.json")

    for index in range(len(animals_data)):
        animal = animals_data[index]
        print(f"Name: {animal["name"]}") if animal["name"] != "" else None
        print(f"Diet: {animal["characteristics"]["diet"]}") if animal["characteristics"]["diet"] != "" else None
        print(f"Location: {animal["locations"][0]}") if animal["locations"][0] != "" else None
        print(f"Type: {animal["characteristics"]["type"]}") if animal["characteristics"]["type"] != "" else None
        print("")


def main():
    print_animals_attributes()


if __name__ == "__main__":
    main()
