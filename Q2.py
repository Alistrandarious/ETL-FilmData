import csv  # Imported CSV so I could .read, write in new files. Basically helps me do all python code.



def Accept_New_Film():

    new_film_data = []
    desired_type = ['movie']
    not_letters = ['\\N']
    with open('imdbtitles.csv', newline='') as oldfilms:
        oldfilmsreader = csv.reader(oldfilms, delimiter=",")
        for x in oldfilmsreader:
            if x[0] in desired_type and int(x[4]) >= 2010:
                if x[6] in not_letters:
                    x[6] = x[6].replace("\\N", "")
                transformation = [x[0], x[1], x[4], x[6]]
                if x[6] != '':
                    hours = str((int(x[6])//60))
                    minutes = str(int(x[6]) % int(60))
                    transformation.append(hours + "h " + minutes + "m")
                new_film_data.append(transformation)

    return new_film_data


def create_new_film_data_csv(new_imdb_database='new_film_data.csv'):
    new_film_data = Accept_New_Film()

    with open(new_imdb_database, "w") as new_file:  # as above. Links to the new open writing file.
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_film_data)


create_new_film_data_csv()


