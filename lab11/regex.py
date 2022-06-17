import re
from zipfile import ZipFile  # Importing necessary modules for working with zip files


class Regex:

    # Extracting zip
    @staticmethod
    def extract():
        zip_name = "access.log.zip"

        # Opening zip in read mode
        with ZipFile(zip_name, "r") as zip_file:
            zip_file.printdir()  # Printing optional info for file in zip(name, time etc.)

            print("Extracting all the files...")
            zip_file.extractall()  # Extracting all the files
            print("Done")

    # Regex
    @staticmethod
    def regex():
        pattern_get = re.compile(r"([23]\d{2})")  # GET: 200 - 399
        pattern_time = re.compile(r"(2[0-3]|[01]?\d):([0-5]?\d):([0-5]?\d)")  # Time: 02:19:30 - 11:09:29

        # Opening txt file for reading
        lines = open("access.log.txt", "r").readlines()  # 'readlines()' method creating a list of strings

        # Main cycle
        for line in lines:

            # Searching for 1-st pattern
            if re.search(pattern_get, line):

                # Searching for 2-nd pattern in the out
                if re.search(pattern_time, line):
                    # Printing needed lines
                    print(line)
