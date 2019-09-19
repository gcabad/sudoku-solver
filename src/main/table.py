import csv


class Table(object):

    def create_table(self):
        with open("resources/lil_table.csv", "w+", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["R     Time"])
            writer.writerow(["-" * 10])

    def append_table(self, result):
        try:
            with open("resources/lil_table.csv", "a", newline='') as file:
                with open("resources/lil_table.csv", "r") as file_reader:
                    reader = list(csv.reader(file_reader))
                    last_row = reader[len(reader) - 1][0].split(" ")
                    if last_row[0].startswith("-") or last_row[0].isalnum():
                        writer = csv.writer(file)
                        writer.writerow([result])
                    else:
                        raise IndexError
        except (FileNotFoundError, IndexError):
            self.create_table()
            self.append_table(result)

    def get_last_iteration(self):
        try:
            with open("resources/lil_table.csv", "r") as file:
                reader = list(csv.reader(file))
                last_row = str(reader[len(reader) - 1][0]).split(" ")[0]
                if last_row[0].startswith("-"):
                    raise IndexError
                return int(last_row[0]) + 1
        except FileNotFoundError:
            self.create_table()
            return self.get_last_iteration()
        except IndexError:
            self.create_table()
            return 3
