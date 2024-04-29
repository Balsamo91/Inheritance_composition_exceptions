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
            return self.read_csv()
        elif self.source.endswith('.json'):
            return self.read_json()
        elif self.source.endswith('.pickle'):
            return self.read_pickle()
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
            # sys.exit(1)
    
    def read_csv(self):
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
        
    def read_json(self):
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
        
    def read_pickle(self):
        try:
            with open(self.source, 'rb') as picklefile:
                data2 = pickle.load(picklefile)
                print("\nOriginal Pickle content:\n")
                self.print_pickle_table(data2)
                return data2
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

                # Update the value in the specified cell of the CSV data
                data[row][column] = value

            return data

        # Print an error message if there's an issue with the changes
        except ValueError or IndexError:
            print("\nInvalid change, please retry!")
            return None
    
    def save_file(self, data_to_save):
        if self.destination.endswith('.csv'):
            self.save_csv(data_to_save)
        elif self.destination.endswith('.json'):
            self.save_json(data_to_save)
        elif self.destination.endswith('.pickle'):
            self.save_pickle(data_to_save)
        else:
            print("Unsupported destination file type.")

    def save_csv(self, data_csv):
        try:
            with open(self.destination, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data_csv)
                print("\nModified CSV content saved successfully.\n")
                for row in data_csv:
                    print(f",".join(map(str, row)))
                print("")
        except IOError:
            print(f"Error writing to file: {self.destination}")
    
    def save_json(self, data_json):
        try:
            with open(self.destination, 'w') as jsonfile:
                json.dump(data_json, jsonfile, indent=4)
                print("\nModified JSON content saved successfully.\n")
                self.print_json_table(data_json)
                print("")
        except IOError:
            print(f"Error writing to file: {self.destination}")

    def save_pickle(self, data_pickle):
        try:
            with open(self.destination, 'wb') as picklefile:
                pickle.dump(data_pickle, picklefile)
                print("\nModified Pickle content saved successfully.\n")
                self.print_pickle_table(data_pickle)
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
    changes = sys.argv[3:]

    # Check if changes are provided
    if not changes:
        print("No changes provided!")
        sys.exit(1)

    reader = Main(source_file, destination_file, changes)

    data = reader.read_file()

    modified_data = reader.apply_changes(data)

    reader.save_file(modified_data)



