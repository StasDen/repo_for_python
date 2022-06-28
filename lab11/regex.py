import re
from zipfile import ZipFile  # Importing necessary modules for working with zip files


class Regex:

    # Extracting zip
    @staticmethod
    def extract():
        zip_name = "access.log.zip"

        # Opening zip in read mode
        with ZipFile(zip_name, "r") as zip_file:
            zip_file.printdir()  # Printing optional info for file in zip(name, size etc.)

            print("Extracting all the files...")
            zip_file.extractall()  # Extracting log file
            print("Done")

    # Regex
    @staticmethod
    def regex():
        cnt: int = 0  # Counter

        # GET: 200 - 399
        get_pattern = re.compile(r'("\s[23]\d{2})\s')

        # Time: 02:19:30 - 11:09:29
        time_pattern = re.compile(r":(0[2-9]|10):([2-5]?\d|0\d|19):([0-5]?\d)")  # From 02:19:30 - 10:59:59
        _time_pattern = re.compile(r"(11):(0\d):([0-2]\d)")  # From 11:00:00 - 11:09:29

        # Opening txt file for reading
        lines = open("access.log.txt", "r").readlines()  # 'readlines()' creating a list of strings(each row - string)

        for line in lines:

            # Searching for GET pattern
            if re.search(get_pattern, line):

                # Searching for time pattern in the out
                if re.search(_time_pattern, line):
                    cnt += 1

                    print(line)

                if re.search(time_pattern, line):
                    cnt += 1

                    print(line)

        # Printing num of needed lines
        print(cnt)
