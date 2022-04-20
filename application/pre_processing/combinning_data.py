from datetime import datetime


class Combine:

    @staticmethod
    def deaths_and_downloads(data_frame_deaths, data_frame_downloads):
        values = []
        for i in range(len(data_frame_downloads)):
            value = 0
            for j in range(len(data_frame_deaths)):
                start_date = datetime.strptime(data_frame_downloads['Week starting'][i], '%d/%m/%Y')
                end_date = datetime.strptime(data_frame_downloads['Week ending'][i], '%d/%m/%Y')
                death_date = datetime.strptime(data_frame_deaths['date'][j], '%d/%m/%Y')
                if start_date <= death_date <= end_date:
                    # print(f"week start: {start_date}")
                    # print(f"week end: {end_date}")
                    # print(f"death date: {data_frame_deaths['date'][j]}")
                    value += data_frame_deaths['new_deaths_total'][j]
                    # print(value)
            values.append(value)

        return values
