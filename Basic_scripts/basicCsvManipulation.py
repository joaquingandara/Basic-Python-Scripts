import csv 

with open("students.csv") as csv_file: #with hace el open y close
    reader = csv.DictReader(csv_file)
    header_row = next(reader) #Obtenemos la linea actual y avanzamos el iterador.
    #print(f"Column names are {','.join(header_row)}") # joinea todos los elementos usando "," como separador

    for row in reader: 
        print(f"Student {row['name']} is from the Faculty of {row['faculty']}, "
            f"{row['department']} dept.")