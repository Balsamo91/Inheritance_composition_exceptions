# Importing Modules
import sys
import os
import csv
import json
import pickle


class Main:
    def __init__(self, source, destination, changes):
        self.source = source
        self.destination = destination
        self.changes = changes

    def read_file(self):
        if not os.path.isfile(self.source):
            print(f"\nSource file not found or is not a file: {self.source}")
            with open(self.source, "w")as file:
                file.close()
                pass
            self.list_files_in_directory()  # List files in the same directory
            sys.exit(1)  # Exit the program
        else:
            if os.path.getsize(self.source) == 0:
                print(f"\nSource file is empty: {self.source}\n")
                sys.exit(1)  # Exit the program

        if self.source.endswith('.csv'):
            return Csv(self.source, self.destination, self.changes).read_file()
        elif self.source.endswith('.json'):
            return Json(self.source, self.destination, self.changes).read_file()
        elif self.source.endswith('.pickle'):
            return Pickle(self.source, self.destination, self.changes).read_file()
        else:
            print('Unsupported file type.')
            return None

    def list_files_in_directory(self):
        try:
            files = [f for f in os.listdir(os.path.dirname(self.source)) if os.path.isfile(os.path.join(os.path.dirname(self.source), f))]
            print("\nFiles in the directory:\n")
            print("\n".join(files))
        except FileNotFoundError:
            print("\nDirectory not found.")

    def apply_changes(self, data):
        # Method to apply changes to the data
        if data is None:
            print("\nCannot apply changes. Data not available.")
            return None

        try:
            for change in self.changes:
                # Split each change into its components: column, row, and value
                column, row, value = map(str.strip, change.split(","))

                # Convert column and row to integers
                column = int(column)
                row = int(row)

                # Update the value in the specified cell of the data
                data[row][column] = value

            return data

        # Print an error message if there's an issue with the changes
        except (ValueError, IndexError):
            print("\nInvalid change, please retry!")
            return None

    def save_file(self, data_to_save):
        if self.destination.endswith('.csv'):
            Csv(self.source, self.destination, self.changes).save_file(data_to_save)
        elif self.destination.endswith('.json'):
            Json(self.source, self.destination, self.changes).save_file(data_to_save)
        elif self.destination.endswith('.pickle'):
            Pickle(self.source, self.destination, self.changes).save_file(data_to_save)
        else:
            print("Unsupported destination file type.")


class Csv(Main):
    def __init__(self, source, destination, changes):
        super().__init__(source, destination, changes)

    def read_file(self):
        try:
            with open(self.source, 'r', newline='') as csvfile:
                reader = list(csv.reader(csvfile))
                print("\nOriginal CSV file:\n")
                for row in reader:
                    print(",".join(row))
                return reader
        except FileNotFoundError:
            print(f"File not found: {self.source}")
            return None

    def save_file(self, data_to_save):
        try:
            with open(self.destination, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data_to_save)
                print("\nModified CSV content saved successfully.\n")
                for row in data_to_save:
                    print(f",".join(map(str, row)))
                print("")
        except IOError:
            print(f"Error writing to file: {self.destination}")


class Json(Main):
    def __init__(self, source, destination, changes):
        super().__init__(source, destination, changes)

    def read_file(self):
        try:
            with open(self.source, 'r') as jsonfile:
                data = json.load(jsonfile)
                print("\nOriginal JSON content:\n")
                self.print_json_table(data)
                return data
        except FileNotFoundError:
            print(f"File not found: {self.source}")
            return None
        except json.JSONDecodeError:
            print("Error decoding JSON.")
            return None

    def print_json_table(self, data):
        if not data:
            print("Cannot apply changes. Data not available.")
            return

        for row in data:
            print(','.join(str(cell) for cell in row))

    def save_file(self, data_to_save):
        try:
            with open(self.destination, 'w') as jsonfile:
                json.dump(data_to_save, jsonfile, indent=4)
                print("\nModified JSON content saved successfully.\n")
                self.print_json_table(data_to_save)
                print("")
        except IOError:
            print(f"Error writing to file: {self.destination}")


class Pickle(Main):
    def __init__(self, source, destination, changes):
        super().__init__(source, destination, changes)

    def read_file(self):
        try:
            with open(self.source, 'rb') as picklefile:
                data = pickle.load(picklefile)
                print("\nOriginal Pickle content:\n")
                self.print_pickle_table(data)
                return data
        except FileNotFoundError:
            print(f"File not found: {self.source}")
            return None
        except pickle.UnpicklingError:
            print("Error unpickling data.")
            return None

    def print_pickle_table(self, data):
        if not data:
            print("Cannnot apply changes. Data not available.")
            return

        # If data is a list of lists, print it as a table
        for row in data:
            print(','.join(str(cell) for cell in row))

    def save_file(self, data_to_save):
        try:
            with open(self.destination, 'wb') as picklefile:
                pickle.dump(data_to_save, picklefile)
                print("\nModified Pickle content saved successfully.\n")
                self.print_pickle_table(data_to_save)
                print("")
        except IOError:
            print(f"Error writing to file: {self.destination}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 reader.py source_file destination_file change1 change2 change3 change4 (Support up to 4 changes at the time)")
        sys.exit(1)

    # Get the source_file, destination_file, and changes from CMD
    source_file = sys.argv[1]
    destination_file = sys.argv[2]
    changes = sys.argv


    reader = Main(source_file, destination_file, changes)

    data = reader.read_file()

    modified_data = reader.apply_changes(data)

    if modified_data is not None:
        reader.save_file(modified_data)