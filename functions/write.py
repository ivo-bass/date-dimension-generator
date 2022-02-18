import json


def write_to_json(calendar) -> None:
    with open("output.json", "w") as file:
        for date_instance in calendar.dates:
            item = date_instance.generate_dict()
            line = json.dumps(item)
            file.write(line + "\n")
