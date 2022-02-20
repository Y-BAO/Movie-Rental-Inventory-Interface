import re 
import os 
import csv
from classes.Customers import Customer
from classes.Inventory import Inventory
import random
import string

class Store:


    def __init__(self,store_name):
        self.store_name = store_name
        self.customers = Customer.load_all_customers()
        self.inventory = Inventory.load_all_inventories()
    
 
        
    def view_rentals(self,customer_id):
        for customer in self.customers:
             
            if customer.id == customer_id:
                if len(customer.current_video_rentals) == 0:
                    print(f'Hi! {customer.first_name} {customer.last_name}\nyou do not have any rentals yet, rent your first videos with {self.store_name}!!!')
                else:
                    print(f'\nHi {customer.first_name} {customer.last_name}!!\nYou have these videos: ')
                    print('\n'.join(customer.current_video_rentals.split(
                    '/'
                    )))
        return '\n'
            # print(f"id:{customer.id}, account_type:{customer.account_type}, first_name:{customer.first_name}, last_name:{customer.last_name}, current_video_rentals:{customer.current_video_rentals}")
    

    
    def show_all_inventory(self):
        Inventory.show_all_inventory(self)

    def show_all_customers(self):
        Customer.show_all_customer(self)


    def add_customer_info(self):
        customer_info = {}

       
        customer_info['id'] = self.id_generator()
        customer_info['account_type'] = input(f'enter account type\nsx:standard\npx:premium\nsf:standard_family\npf:premium_family\nchoose(sx/px/sf/pf): ')
        customer_info['first_name'] = input('enter first name: ')
        customer_info['last_name'] = input('enter last name: ')
        customer_info['current_video_rentals'] = ''
        self.add_customer(customer_info)
        return customer_info

    def id_generator(self):
        new_id = ''.join(random.sample(string.ascii_letters + string.digits,5))
        while True:
            for info in self.customers:
                if info.id != new_id:
                    return new_id



  
    def add_customer(self,customer_info):
        new_customer = Customer(**customer_info)
        self.customers.append(new_customer)
        self.save_new_customer(new_customer)
    


    def delete_customer(self,id):
        for customer in self.customers:

            if customer.id == id:
                if customer.current_video_rentals != 0:
                    print( f'please return all your videos first{self.view_rentals(id)}')
                    return 
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

    



 


























    