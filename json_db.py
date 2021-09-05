import json


class jsonDB:

    def __init__(self) -> None:
        self.json_file = "db.json"

        with open(self.json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

            try:
                _ = data["tasks"]
            except KeyError:
                data["tasks"] = []
        with open(self.json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_item(self, table_name, item):
        with open(self.json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            data[table_name].append(item)
        with open(self.json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_all(self, table_name):
        with open(self.json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            all = data["tasks"]

        return all
