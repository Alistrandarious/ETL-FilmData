import csv

new_user_data = []
with open("user_details.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)
    # for x in csvreader:
    #     print(x[-1])  # prints last line of the row

    # print(list(csvreader)) prints once...
    # print(list(csvreader)) but not again.
    users = list(csvreader) # This stops it from being used only once.
    print(users)
    print(users)
    # iterable_cvs = iter(csvreader)
    # next(iterable_cvs)  # becomes the new 'csvreader'. Do more next's the print the next rows.
    # for x in iterable_cvs:
    #     print(x)

    for x in users:
        transformation = []
        transformation.append(users[1])
        transformation.append(users[2])
        transformation.append(users[-1])
        new_user_data.append(transformation)

print(new_user_data)









    # Extract, Transform, Load.