from import_data import ImportData
import os


def main():
    import_data = ImportData()
    import_data.convert_csv_to_json(f'{os.getcwd()}\\application\\data\\phe_deaths_age_london.csv')


if __name__ == "__main__":
    main()