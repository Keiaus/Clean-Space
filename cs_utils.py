import math
import torch
import sys
import datetime
import os

class CSUtils():
    color_schema = [
        "GREEN",
        "RED"
    ]

    scan_count = 0

    def wash_hands(self):
        print(f'{self.color_schema[1]}' + "\nYour hands are dirty. Go wash them.")
        exit

    def hands_are_clean(self):
        print(f'{self.color_schema[0]}' + "\nYour hands are clean.")
        exit

    def germ_check(self):
        bathroom = input("Did you use the bathroom? (Y/N) ")
        raw_meat = input("Did you touch raw meat? (Y/N) ")

        if bathroom == "Y" or bathroom == "y" or raw_meat == "Y" or raw_meat == "y":
            self.scan_count += 1
            print("Hands scanned", self.scan_count, "times.")
            self.wash_hands()

        else:
            self.hands_are_clean()

        # if bathroom == "Y" or raw_meat == "Y":
        #     wash_hands()
        # else:
        #     hands_are_clean()   

# cs = CSUtils()
# cs.germ_check()