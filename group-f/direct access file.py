
# Implementation of a direct access file -Insertion and deletion of a record from a direct 
# access file

class DirectAccessFile:
    def __init__(self):
        self.records = {}

    def insert_record(self, record_id, data):
        if record_id in self.records:
            print("Record with ID {} already exists. Insertion failed.".format(record_id))
        else:
            self.records[record_id] = data
            print("Record with ID {} inserted successfully.".format(record_id))

    def delete_record(self, record_id):
        if record_id in self.records:
            del self.records[record_id]
            print("Record with ID {} deleted successfully.".format(record_id))
        else:
            print("Record with ID {} does not exist. Deletion failed.".format(record_id))

    def display_records(self):
        if not self.records:
            print("No records in the direct access file.")
        else:
            print("Records in the direct access file:")
            for record_id, data in self.records.items():
                print("ID: {}, Data: {}".format(record_id, data))


# Example usage:
if __name__ == "__main__":
    # Create a direct access file instance
    direct_access_file = DirectAccessFile()

    # Insert some records
    direct_access_file.insert_record(1, "Record 1 data")
    direct_access_file.insert_record(2, "Record 2 data")
    direct_access_file.insert_record(3, "Record 3 data")

    # Display all records
    direct_access_file.display_records()

    # Delete a record
    direct_access_file.delete_record(2)

    # Display all records after deletion
    direct_access_file.display_records()
