import pickle
import csv
import json
import os
import sys

class BaseFileHandler:
    def __init__(self, source, destination, changes):
        self.source = source
        self.destination = destination
        self.changes = changes

    def read_file(self):
        pass

    def print_table(self, data):
        pass

    def apply_changes(self, data):
        pass

    def save_file(self, data_to_save):
        pass


class CSVFileHandler(BaseFileHandler):
    def read_file(self):
        try:
            with open(self.source, 'r', newline='') as csvfile:
                reader = list(csv.reader(csvfile))
                print("\nOriginal CSV file:\n")
                self.print_table(reader)
                return reader
        except FileNotFoundError:
            print(f"File not found: {self.source}")
            return None

    def print_table(self, data):
        if not data:
            print("Cannot apply changes. Data not available.")
            return

        for row in data:
            print(','.join(str(cell) for cell in row))

    def apply_changes(self, data):
        if data is None:
            print("\nCannot apply changes. Data not available.")
            return None

        try:
            for change in self.changes:
                column, row, value = map(str.strip, change.split(","))
                column = int(column)
                row = int(row)
                data[row][column] = value

            return data

        except (ValueError, IndexError):
            print("\nInvalid change, please retry!")
            return None

    def save_file(self, data_to_save):
        try:
            with open(self.destination, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data_to_save)
                print("\nModified CSV content saved successfully.\n")
                self.print_table(data_to_save)
                print("")
        except IOError:
            print(f"Error writing to file: {self.destination}")

class JSONFileHandler(BaseFileHandler):
    def read_file(self):
        try:
            with open(self.source, 'r') as jsonfile:
                data = json.load(jsonfile)
                print("\nOriginal JSON content:\n")
                self.print_table(data)
                return data
        except FileNotFoundError:
            print(f"File not found: {self.source}")
            return None
        except json.JSONDecodeError:
            print("Error decoding JSON.")
            return None

    def print_table(self, data):
        if not data:
            print("Cannot apply changes. Data not available.")
            return

        for row in data:
            print(','.join(str(cell) for cell in row))

    def apply_changes(self, data):
        if data is None:
            print("\nCannot apply changes. Data not available.")
            return None

        try:
            for change in self.changes:
                column, row, value = map(str.strip, change.split(","))
                column = int(column)
                row = int(row)
                data[row][column] = value

            return data

        except (ValueError, IndexError):
            print("\nInvalid change, please retry!")
            return None

    def save_file(self, data_to_save):
        try:
            with open(self.destination, 'w') as jsonfile:
                json.dump(data_to_save, jsonfile, indent=4)
                print("\nModified JSON content saved successfully.\n")
                self.print_table(data_to_save)
                print("")
        except IOError:
            print(f"Error writing to file: {self.destination}")

class PickleFileHandler(BaseFileHandler):
    def read_file(self):
        try:
            with open(self.source, 'rb') as picklefile:
                data = pickle.load(picklefile)
                print("\nOriginal Pickle content:\n")
                self.print_table(data)
                return data
        except FileNotFoundError:
            print(f"File not found: {self.source}")
            return None
        except pickle.UnpicklingError:
            print("Error unpickling data.")
            return None

    def print_table(self, data):
        if not data:
            print("Cannot apply changes. Data not available.")
            return

        for row in data:
            print(','.join(str(cell) for cell in row))

    def apply_changes(self, data):
        if data is None:
            print("\nCannot apply changes. Data not available.")
            return None

        try:
            for change in self.changes:
                column, row, value = map(str.strip, change.split(","))
                column = int(column)
                row = int(row)
                data[row][column] = value

            return data

        except (ValueError, IndexError):
            print("\nInvalid change, please retry!")
            return None

    def save_file(self, data_to_save):
        try:
            with open(self.destination, 'wb') as picklefile:
                pickle.dump(data_to_save, picklefile)
                print("\nModified Pickle content saved successfully.\n")
                self.print_table(data_to_save)
                print("")
        except IOError:
            print(f"Error writing to file: {self.destination}")

class Main:
    def __init__(self, source, destination, changes):
        self.source = source
        self.destination = destination
        self.changes = changes

    def get_file_handler(self):
        if self.source.endswith('.csv'):
            return CSVFileHandler(self.source, self.destination, self.changes)
        elif self.source.endswith('.json'):
            return JSONFileHandler(self.source, self.destination, self.changes)
        elif self.source.endswith('.pickle'):
            return PickleFileHandler(self.source, self.destination, self.changes)
        else:
            print('Unsupported file type.')
            return None

    def process_file(self):
        file_handler = self.get_file_handler()
        if file_handler is not None:
            data = file_handler.read_file()
            if data is not None:
                modified_data = file_handler.apply_changes(data)
                if modified_data is not None:
                    file_handler.save_file(modified_data)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 reader.py source_file destination_file change1 change2 change3 change4 (Support up to 4 changes at the time)")
        sys.exit(1)

    source_file = sys.argv[1]
    destination_file = sys.argv[2]
    changes = sys.argv[3:]

    if not changes:
        print("No changes provided!")
        sys.exit(1)

    reader = Main(source_file, destination_file, changes)
   
