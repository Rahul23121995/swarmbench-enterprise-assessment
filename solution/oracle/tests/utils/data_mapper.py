import csv

class CSVDataMapper:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_test_data(self):
        records = []
        with open(self.file_path, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue  # skip empty lines
                # Expected columns: username, role, id
                username, role, id_ = row
                records.append({
                    "username": username,
                    "role": role,
                    "id": id_
                })
        return records
