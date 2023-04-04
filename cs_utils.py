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
        self.scan_count += 1
        print("Hands scanned", self.scan_count, "times.")
        self.germ_check()

    def hands_are_clean(self):
        print(f'{self.color_schema[0]}' + "\nYour hands are clean.")
        self.scan_count += 1
        print("Hands scanned", self.scan_count, "times.")
        exit

    # This function checks to see if the person's hands are clean
    # It also calls the other functions
    def germ_check(self):
        bathroom = input("Did you use the bathroom? (Y/N) ")
        raw_meat = input("Did you touch raw meat? (Y/N) ")

        if bathroom == "Y" or bathroom == "y" or raw_meat == "Y" or raw_meat == "y":
            self.wash_hands()
        else:
            self.hands_are_clean()