import datetime as dt


class TheRace(object):
    def __init__(self, list_laps):
        self.list_laps = list_laps
        self.the_best_lap = None

    def process_data(self):
        data = {}
        for lap in self.list_laps:
            if lap.get("id") in data.keys():
                data[lap.get("id")]["laps"].append(lap)
            else:
                data[lap.get("id")] = {"laps": [lap]}

        self.data_process = data
        return self.data_process

    def total_time_per_pilot(self):
        self.total_time_per_pilot = {}
        for key, item in self.data_process.items():
            self.data_process[key]["total_time"], self.data_process[key][
                "best_lap"
            ] = self.calculate_total_time_pilot(item["laps"])
            self.total_time_per_pilot[key] = self.data_process[key]["total_time"]

        # sort total time
        self.total_time_per_pilot = sorted(
            self.total_time_per_pilot.items(), key=lambda x: x[1]
        )

    def print_result(self, data_result):
        print(f"The best lap: {self.the_best_lap.time()}")

        str_result = """ 
- Position: {} \n
- Pilot Code: {} \n
- Pilot Name: {} \n
- Laps: {} \n
- The best lap: {} \n
- Avg speed: {:10.4f} \n
- Time after the winner: {} \n
- Total Time: {} \n
            """
        position = 1
        first_total_time = self.total_time_per_pilot[0][1]
        for key, item in self.total_time_per_pilot:

            result = data_result[key]

            print(
                str_result.format(
                    position,
                    result["code"],
                    result["name"],
                    result["number_laps"],
                    result["best_lap"].time(),
                    result["avg_speed"],
                    item - first_total_time,
                    item,
                )
            )

            position += 1

    def execute(self):
        self.process_data()
        self.total_time_per_pilot()
        data_result = self.format_data_result()
        self.print_result(data_result)

    def calculate_total_time_pilot(self, list_lap_pilot):
        time_list = [
            dt.datetime.strptime(lap["lap_time"], "%M:%S.%f") for lap in list_lap_pilot
        ]

        minutes_sum, seconds_sum, microseconds_sum = (0, 0, 0)

        for time in time_list:
            minutes_sum += time.minute
            seconds_sum += time.second
            microseconds_sum += time.microsecond

        total_time = dt.timedelta(
            minutes=minutes_sum, seconds=seconds_sum, microseconds=microseconds_sum
        )

        if not self.the_best_lap:
            self.the_best_lap = sorted(time_list)[0]
        elif self.the_best_lap > sorted(time_list)[0]:
            self.the_best_lap = sorted(time_list)[0]

        return total_time, sorted(time_list)[0]

    def format_data_result(self):
        data_result = {}

        for key, item in self.data_process.items():
            dict_result = {}
            dict_result["code"] = item.get("laps")[0]["id"]
            dict_result["name"] = item.get("laps")[0]["name"]
            dict_result["number_laps"] = len(item.get("laps"))
            dict_result["best_lap"] = item.get("best_lap")
            dict_result["avg_speed"] = self.avg_velocity(item.get("laps"))
            data_result[key] = dict_result
        
        return data_result

    def avg_velocity(self, laps):
        sum_velocity = 0

        for lap in laps:
            sum_velocity += float(lap["avg_speed"])

        return sum_velocity / len(laps)