import json
from rapidfuzz import fuzz


def load_data():
    with open("animals_data.json") as f:
        return json.load(f)


def get_serialized_animals(skin_type):
    """Serializes animals from a json-file into HTML.

    Args:
        skin_type (str): Skin type of the animal object

    Returns:
        Str: Serialized animals
    """
    animals_data = load_data()
    serialized_animals = ""

    for animal_data in animals_data:
        serialized_animals += serialize_animal(animal_data, skin_type)

    return serialized_animals


def serialize_animal(animal_obj, skin_type):
    """Serialize an animal object into HTML.

    Args:
        animal_obj (dict): Animal object to be serialized
        skin_type (str): Skin type of the animal object

    Returns:
        Str: Serialized animal object
    """
    output = ""
    if animal_obj.get('characteristics', {}).get('skin_type') == skin_type:
        output += "<li class=\"cards__item\">\n"
        output += f"<div class=\"card__title\">{animal_obj.get('name')}</div> \n"
        output += "<div class=\"card__text\">\n"
        output += "<ul>\n"
        output += f"<li><strong>Diet:</strong> {animal_obj.get('characteristics', {}).get('diet')}</li>\n"
        output += f"<li><strong>Skin type:</strong> {animal_obj.get('characteristics', {}).get('skin_type')}</li>\n"
        output += f"<li><strong>Location:</strong> {animal_obj.get('locations')[0]}</li>\n"
        if 'type' in animal_obj.get('characteristics', {}).keys():
            output += f"<li><strong>Type:</strong> {animal_obj.get('characteristics', {}).get('type')}</li>\n"
        output += f"<li><strong>Scientific name:</strong> {animal_obj.get('taxonomy', {}).get('scientific_name')}</li>\n"
        output += "</ul>\n"
        output += "</div>\n"
        output += "</li>\n\n"
    elif skin_type == "":
        output += "<li class=\"cards__item\">\n"
        output += f"<div class=\"card__title\">{animal_obj.get('name')}</div> \n"
        output += "<div class=\"card__text\">\n"
        output += "<ul>\n"
        output += f"<li><strong>Diet:</strong> {animal_obj.get('characteristics', {}).get('diet')}</li>\n"
        output += f"<li><strong>Skin type:</strong> {animal_obj.get('characteristics', {}).get('skin_type')}</li>\n"
        output += f"<li><strong>Location:</strong> {animal_obj.get('locations')[0]}</li>\n"
        if 'type' in animal_obj.get('characteristics', {}).keys():
            output += f"<li><strong>Type:</strong> {animal_obj.get('characteristics', {}).get('type')}</li>\n"
        output += f"<li><strong>Scientific name:</strong> {animal_obj.get('taxonomy', {}).get('scientific_name')}</li>\n"
        output += "</ul>\n"
        output += "</div>\n"
        output += "</li>\n\n"

    return output
