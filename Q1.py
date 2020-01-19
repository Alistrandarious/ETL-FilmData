import csv

# Function that accepts csv_file_name parameter
# Returns new_user_data list


def Accept_CSV_File(file):
    new_data_for_users = []
    with open(file, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        for users in csvreader:
            transformation = []
            transformation.append(users[1])
            transformation.append(users[2])
            transformation.append(users[-1])
            new_data_for_users.append(transformation)

        return new_data_for_users


def create_new_user_data_csv(old_user_data='user_details.csv', new_file_name='new_user_data.csv'):
    new_user_data = Accept_CSV_File(old_user_data)

    with open(new_file_name, "w") as new_file:  # as above. Links to the new open writing file.
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)

create_new_user_data_csv()




