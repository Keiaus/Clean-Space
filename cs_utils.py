import torch
import math

class CSUtils():
    def __init__(self) -> None:
        def germ_check(self):
            color_schema = list("Green", "Red")
            scan_count = 0
            bathroom = input("Did you use the bathroom?: ")
            raw_meat = input("Did you touch raw meat?: ")
            if bathroom == "Yes" or "yes" or raw_meat == "Yes" or "yes":
                wash_hands()
            else:
                hands_are_clean()   
        def wash_hands(self, color_schema):
            self.color_schema = color_schema
            print(f'{color_schema(0)}' + "\n Your hands are dirty. Go wash them.")
            exit
        def hands_are_clean(self, color_schema):
            self.color_schema = color_schema
            print(f'{color_schema(1)}' + "\n Your hands are clean.")
            exit