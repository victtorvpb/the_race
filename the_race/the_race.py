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
        self.total_time_per_pilot = {}
        for key, item in self.data_process.items():
            self.data_process[key]['total_time'] = self.calculate_total_time_pilot(item['laps'])
            self.total_time_per_pilot[key] = self.calculate_total_time_pilot(item['laps'])
        
        #sort total time
        self.total_time_per_pilot = sorted(self.total_time_per_pilot.items(), key=lambda x: x[1])
    
    def print_result(self):
        
        str_result = (
            """ 
- Position: {} \n
- Pilot Code: {} \n
- Pilot Name: {} \n
- Laps: {} \n
- Total Time: {} \n
            """
        )
        position = 1
        for key, item in self.total_time_per_pilot:
            result_lap = self.data_process[key]['laps'][0]
            print(str_result.format(position, result_lap['id'], result_lap['name'], 3, item))

            position += 1

    def get_results(self):
        self.process_data()
        self.total_time_per_pilot()
        self.print_result()

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

