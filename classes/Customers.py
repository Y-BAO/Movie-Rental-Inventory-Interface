 
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


 














 


     
 




 
 



    # @classmethod
    # def delete_customer(cls,id):
    #     updated_customer = []
    #     with open('../data/customers.csv','r',newline = '') as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         for row in reader:
    #             if row['id'] != id:
    #                 updated_customer.append(row)

    #     keys = updated_customer[0].keys()
    #     with open('../data/customers.csv', 'w',newline = '') as csvfile:
    #         dict_writer = csv.DictWriter(csvfile,keys)
    #         dict_writer.writeheader()
    #         dict_writer.writerows(updated_customer)

        


 
            
 

 


































            

        
    # @classmethod
    # def save_all_customers(cls,all_customers):
         
    #     my_path = os.path.abspath(os.path.dirname(__file__))
    #     path = os.path.join(my_path,'../data/customers.csv')
    #     with open(path,mode = 'w') as csv_file:
            
    #         writer = csv.DictWriter(csv_file,fieldnames=['id','account_type','first_name','last_name','current_video_rentals'])
    #         writer.writeheader()

    #         for customer in all_customers:
    #             info_dict = customer.__dict__

    #             writer.writerow(info_dict)
            

    #     return all_customers
    

    # def __repr__(self):
        
    #     return f"\nid:{self.id} account_type:{self.account_type} first_name:{self.first_name} last_name:{self.last_name} current_video_rentals:{self.current_video_rentals}\n"