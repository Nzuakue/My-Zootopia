import json


def load_data(filepath):
    with open(filepath) as f:
        return json.load(f)


def get_animals_attributes():
    """Read animals attributes from a json-file.

    Returns:
        Str: Animals attributes
    """
    foxes_data = load_data("animals_data.json")
    fox_attributes = ""

    for fox_data in foxes_data:
        fox_attributes += "<li class=\"cards__item\">\n"
        fox_attributes += f"Name: {fox_data.get('name')}<br/> \n" if 'name' in fox_data.keys() else ""
        fox_attributes += f"Diet: {fox_data.get('characteristics', {}).get('diet')}<br/>\n" if 'diet' in fox_data.get(
            'characteristics', {}).keys() else ""
        fox_attributes += f"Location: {fox_data.get('locations')[0]}<br/>\n" if 'locations' in fox_data.keys() else ""
        fox_attributes += f"Type: {fox_data.get('characteristics', {}).get('type')}<br/>\n" if "type" in fox_data.get(
            'characteristics', {}).keys() else "\n"
        fox_attributes += "</li>\n\n"

    return fox_attributes


