 
import os
import csv
 

class Inventory:

    DATA_FILE = "../data/inventory.csv"

    def __init__(self,id,title,rating,release_year,copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = copies_available
    
    @classmethod
    def load_all_inventories(cls):
        all_inventory = []

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path,"../data/inventory.csv")

        with open(path,mode = 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for inventory in reader:
                all_inventory.append(Inventory(**dict(inventory)))

        return all_inventory

    @classmethod
    def show_all_inventory(cls):
        with open('/Users/yilinbao/Desktop/assessment-2/data/customers.csv','r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for line in csv_reader:
                print(line)