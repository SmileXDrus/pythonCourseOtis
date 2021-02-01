import csv


def read_csv_cars():
    with open('cars.csv') as f:
        csv_reader = csv.reader(f, delimiter=',')
        lines_count = 0
        print('csv_reader:', csv_reader)
        for row in csv_reader:
            if lines_count == 0:
                print(repr(row))
                print('Columns:', ' | '.join(row))
            else:
                print(f"Values in {lines_count} line:", " | ".join(row))
                print(f"Car from {row[0]} by {row[1]} ({row[2]}) [{row[3]}] ${row[4]}")
            lines_count += 1
        print("Read", lines_count, "lines")


def read_csv_cars_to_dict():
    with open("cars.csv") as f:
        csv_reader = csv.DictReader(f)  # dict
        lines_count = 0
        print("csv_reader:", csv_reader)
        for row in csv_reader:
            # print(repr(row))
            if lines_count == 0:
                print("Columns:", " | ".join(row))
            print(f"Car from {row['year']} "
                  f"by {row['name']} "
                  f"({row['vendor']}) "
                  f"[{row['comment']}] "
                  f"${row['price']}")
            lines_count += 1

        print("Got", lines_count, "data lines")


def write_csv_dict():
    FIELD_NAME = "name"
    FIELD_DEPARTMENT = "department"
    FIELD_BM = "birth month"

    with open('employee_bithday_months.csv', 'w') as f:
        fieldnames = [
            FIELD_NAME,
            FIELD_DEPARTMENT,
            FIELD_BM,
        ]
        csv_writer = csv.DictWriter(
            f,
            fieldnames=fieldnames,
            delimiter=',',  # по умолчанию уже используется запятая
            quotechar='"',  # указывает символ, используемый для окружения полей, которые содержат разделитель delimiter
            quoting=csv.QUOTE_MINIMAL  # поля будут заключены delimiter в кавычки, только если они содержат quotechar
        )
        csv_writer.writeheader()
        csv_writer.writerow({
            FIELD_NAME: "John Smith",
            FIELD_DEPARTMENT: "IT Department",
            FIELD_BM: "March",
        })
        csv_writer.writerow({
            FIELD_NAME: "Ann White",
            FIELD_DEPARTMENT: "Accounting",
            FIELD_BM: "May",
        })
        # quote chars
        csv_writer.writerow({
            FIELD_NAME: "Ann Black",
            FIELD_DEPARTMENT: "Accounting, Management",
            FIELD_BM: "",
        })


# read_csv_cars()
# print(100*'-')
# read_csv_cars_to_dict()
write_csv_dict()
