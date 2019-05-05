import datetime as dt


class TheRace(object):
    def __init__(self, list_laps):
        self.list_laps = list_laps

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
        for key, item in self.data_process.items():
            self.data_process[key]['total_time'] = self.calculate_total_time_pilot(item['laps'])

        import pdb; pdb.set_trace()

    def get_results(self):
        self.process_data()
        self.total_time_per_pilot()

    def calculate_total_time_pilot(self, list_lap_pilot):
        time_list = [dt.datetime.strptime(lap['lap_time'], "%M:%S.%f") for lap in list_lap_pilot]
        minutes_sum, seconds_sum, microseconds_sum = (0, 0, 0)

        for time in time_list:
            minutes_sum += time.minute
            seconds_sum += time.second
            microseconds_sum += time.microsecond

        total_time = dt.timedelta(
            minutes=minutes_sum,
            seconds=seconds_sum,
            microseconds=microseconds_sum
        )

        return total_time
        # Format the total time delta
        # total_time_format = dt.datetime.strptime(str(total_time), '%H:%M:%S.%f')
        # total_time_format = total_time_format.strftime('%-M:%S.%f')[:-3]
        # return total_time_format
