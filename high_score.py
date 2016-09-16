import csv
import datetime

class Highscore():

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.date = None

    def generate_date(self):
        now = datetime.datetime.now()
        self.date = "Date: {}-{}-{}".format(now.year, now.month, now.day)

    def print_score_to_csv(cls, file_name):
        with open(file_name, "a") as file:
            row = "Name : {} - Score: {} - {}".format(cls.name, cls.score, cls.date)
            file.write(row + "\n")

    @staticmethod
    def print_score_out(file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()
        table = [element.replace("\n", "").split(";") for element in lines]
        result = [i for i in lines]
        print(table)
