

class CSUtils():
    color_schema = [
        "Green",
        "Red"
    ]

    scan_count = 0

    def wash_hands(self):
        print(f'{self.color_schema[1]}' + "\n Your hands are dirty. Go wash them.")
        exit

    def hands_are_clean(self):
        print(f'{self.color_schema[0]}' + "\n Your hands are clean.")
        exit

    def germ_check(self):
        bathroom = input("Did you use the bathroom? (Y/N) ")
        raw_meat = input("Did you touch raw meat? (Y/N) ")

        while bathroom == "Y" or bathroom == "y" or raw_meat == "Y" or raw_meat == "y":
            self.scan_count += 1
            print("Hands scanned", self.scan_count, "times.")
            self.wash_hands()
            break

        self.hands_are_clean()
        # if bathroom == "Y" or raw_meat == "Y":
        #     wash_hands()
        # else:
        #     hands_are_clean()   

cs = CSUtils()
cs.germ_check()