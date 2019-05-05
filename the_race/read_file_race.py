import re
import os.path


class ReadFileRace(object):
    def __init__(self, file_path):
        if not os.path.isfile(file_path,):
            raise FileExistsError(f"File {file_path} not exist")

        self.file_path = file_path

    @property
    def to_list(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            laps = []
            for i, line in enumerate(file):
                lap = {}
                if(i != 0):
                    # import pdb; pdb.set_trace()
                    match = re.findall('[\w.:]+', line)
                    lap["time"] = match[0]
                    lap["id"] = match[1]
                    lap["name"] = match[2]
                    lap["number"] = match[3]
                    lap["lap_time"] = match[4]
                    lap["avg_speed"] = match[5]
                    laps.append(lap)
        return laps
