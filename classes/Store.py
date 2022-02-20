import re 
import os 
import csv
from classes.Customers import Customer
from classes.Inventory import Inventory

class Store:


    def __init__(self,store_name):
        self.store_name = store_name
        self.customers = Customer.load_all_customers()
        self.inventory = Inventory.load_all_inventories()
    
 
        
    def view_rentals(self,customer_id):
        for customer in self.customers:
             
            if customer.id == customer_id:
                if len(customer.current_video_rentals) == 0:
                    print('you do not have any')
                print('\n'.join(customer.current_video_rentals.split(
                    '/'
                )))
        return 
            # print(f"id:{customer.id}, account_type:{customer.account_type}, first_name:{customer.first_name}, last_name:{customer.last_name}, current_video_rentals:{customer.current_video_rentals}")
     
    def show_all_inventory(self):
        for video in self.inventory:
            print(f"id:{video.id}, title:{video.title}, release_year:{video.release_year}, copies_available:{video.copies_available}")

    def show_all_customers(self):
        for customer in self.customers:
            print(f"id:{customer.id}, account_type:{customer.account_type}, first_name:{customer.first_name}, last_name:{customer.last_name}, current_video_rentals:{customer.current_video_rentals}")
    





  
    def add_customer(self,customer_info):
        new_customer = Customer(**customer_info)
        self.customers.append(new_customer)
        self.save_new_customer(new_customer)
    


    def delete_customer(self,id):
        for customer in self.customers:
            if customer.id == id:
                self.customers.remove(customer)

        self.update_customer_list()
    


    @classmethod
    def save_new_customer(cls,new_customer):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path,'../data/customers.csv')
        with open(path,mode = 'a') as csv_file:
            
            writer = csv.DictWriter(csv_file,fieldnames= new_customer.__dict__.keys())
            
            
            info_dict = new_customer.__dict__

            writer.writerow(info_dict)
        




    def update_customer_list(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path,"../data/customers.csv")

        with open(path,'w') as csvfile:
            customer_csv = csv.writer(csvfile, delimiter = ',')
            customer_csv.writerow(['id','account_type','first_name','last_name','current_video_rentals'])
            for customer in self.customers:
                customer_csv.writerow([customer.id,customer.account_type,customer.first_name,customer.last_name,customer.current_video_rentals])

    def update_inventory_list(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path,"../data/inventory.csv")

        with open(path,'w') as csvfile:
            inventory_csv = csv.writer(csvfile, delimiter = ',')
            inventory_csv.writerow(['id','title','rating','release_year','copies_available'])
            for inventory in self.inventory:
                inventory_csv.writerow([inventory.id,inventory.title,inventory.rating,inventory.release_year,inventory.copies_available])

    



 


























    