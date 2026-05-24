class CSVDataMapper:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_test_data(self):
        records = []
        with open(self.file_path, "r") as f:
            for line in f:
                # Broken: split-based line parsing that fails on quotes/escapes
                parts = line.strip().split(",")
                username = parts[0]
                role = parts[1]
                id_ = parts[2]
                records.append({
                    "username": username,
                    "role": role,
                    "id": id_
                })
        return records
