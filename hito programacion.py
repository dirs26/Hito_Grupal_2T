import csv

with open("data_lake.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Las columnas son: {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[1]} con el correo {row[0]} tiene el DNI: {row[2]} y a sacado un {row[3]}.')
            line_count += 1
    print(f'Se han procesado {line_count} lineas.')
