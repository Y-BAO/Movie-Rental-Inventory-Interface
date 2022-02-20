 
import os
import csv
 
 
class Customer:
    
    DATA_FILE = "../data/customers.csv"

    def __init__(self,id,account_type,first_name,last_name,current_video_rentals):
        self.id = id
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals
        

 


    @classmethod
    def load_all_customers(cls):
        all_customers = []

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path,"../data/customers.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for customers in reader:
                all_customers.append(Customer(**dict(customers)))

        return all_customers

    def show_all_customer(self):
        for customer in self.customers:
            print(f"id:{customer.id}, account_type:{customer.account_type}, first_name:{customer.first_name}, last_name:{customer.last_name}, current_video_rentals:{customer.current_video_rentals}")
    


 














 


     
 




 


 
            
 

 


































            

        
   