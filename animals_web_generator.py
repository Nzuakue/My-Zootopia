from animals_attributes import get_animals_attributes


def load_template_file():
    """Loads a template file"""
    with open("animals_template.html") as f:
        return f.read()


def create_template():
    """Creates a template file"""
    with open("animals.html", "w") as f:
        f.write(load_template_file().replace("__REPLACE_ANIMALS_INFO__", get_animals_attributes()))

create_template()