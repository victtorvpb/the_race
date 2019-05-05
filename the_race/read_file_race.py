import os.path


class ReadFileRace(object):
    def __init__(self, file_path):
        if not os.path.isfile(file_path):
            raise FileExistsError(f"File {file_path} not exist")

        with open(file_path) as file:
            self.read_data = file.read()

    @property
    def to_list(self):
        race_data = []

        for line in self.read_data.splitlines()[1:]:
            line = line.split()
            line.remove(line[2])

            race_data.append(line)

        return race_data
