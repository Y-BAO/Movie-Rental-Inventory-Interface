

from classes.Store import Store
import re



class Interface:

    def __init__(self,store_name):
        self.store = Store(store_name)
        self.name = store_name
    
    def run(self):
        
        while True:

            mode = input(self.menu())

            if mode == '1':
                
                print('\n')
                
                self.store.show_all_inventory()
                print('\n')

            
            if mode == '2':
                print('\n')
                customer_id =  input("enter customer id: ")
             
                self.store.view_rentals(customer_id)

                print('\n')

            if mode == '3':
                self.add_customer_info()
            

            if mode == '4':
               
                customer = self.check_id()
                account_type = customer.account_type
                current_rentals = customer.current_video_rentals
                if self.check_count(account_type,current_rentals):
                    video_title = input('enter a title: ')
                    if self.check_availability(video_title):
                        self.rent_to_customer(customer.id,video_title)

            if mode == '6':
                print("see you soon")
                break

            if mode == '7':
                self.remove_customer_info()

            if mode == '8':
                self.store.show_all_customers()

                


    def rent_to_customer(self,customer_id,video_title):
        for info in self.store.customers:
            if info.id == customer_id:
                if len(info.current_video_rentals) == 0:
                    info.current_video_rentals = video_title
                    print(info.current_video_rentals)
                else:
                    info.current_video_rentals = info.current_video_rentals + '/' + video_title
                    print(info.current_video_rentals)
        self.store.update_customer_list()
        self.reduce_inventory(video_title)
    
    def reduce_inventory(self,video_title):
        for info in self.store.inventory:
            if info.title == video_title:
                info.copies_available = str(int(info.copies_available) - 1)
                print(info.copies_available)
                self.store.update_inventory_list()
       

    def check_availability(self,video_title):
        for info in self.store.inventory:
            if info.title == video_title:
                stock = info.copies_available
                if int(stock) == 0:
                    print('out of order')
                else:
                    return True
    
     


            
    
    # def reduce_in_rental(video_tile):
    #     pass

    

             
         
                 
        
                
               
               
                # user_current_videos = customer.current_video_rentals
                # user_current_video_count = self.count(user_current_videos)
               

                
                
                    
                     
                
                



          


    def remove_customer_info(self):
        customer_id = str(input('enter an id'))
        self.store.delete_customer(customer_id)

    def menu(self):
        return f"\n\n\n== Welcome to {self.name} Video! ==\n1. View store video inventory\n2. View customer rented videos\n3. Add new customer\n4. Rent video\n5. Return video\n6. Exit\n7. remove a customer\n8: show all customers\n===> "


    def add_customer_info(self):
        customer_info = {}

       
        customer_info['id'] = input('enter an id: ')
        customer_info['account_type'] = input('enter account type: ')
        customer_info['first_name'] = input('enter first name: ')
        customer_info['last_name'] = input('enter last name: ')
        customer_info['current_video_rentals'] = ''
        self.store.add_customer(customer_info)

        
     
                

    def check_id(self):
        while True:
            id_of_customer = input('enter your id')
            for customer in self.store.customers:
                if customer.id == id_of_customer:
                    print(f'welcom customer {customer.first_name} {customer.last_name}')
                    return customer
                     
                        



            print('user not found')

    
    def count(self,input):
        arr = input.split('/')
        return len(arr)



    ref = [
            {'account_type':'sx','max_rental':1,'rating_limit':None},
            {'account_type':'px','max_rental':3,'rating_limit':None},
            {'account_type':'sf','max_rental':1,'rating_limit':'R'},
            {'account_type':'pf','max_rental':3,'rating_limit':'R'}
                ]

    def check_count(self, account_type,current_rentals):
        
        if len(current_rentals) == 0:
            rental_count = 0
        else:
            rental_count = self.count(current_rentals)


        
        for info in self.ref:
            if info['account_type'] == account_type:
                if rental_count >= info['max_rental']:
                    print('you have reached max rentals')
                else:
                    return True    
                         


























#  current_rentals = '\n'.join(customer.current_video_rentals.split('/'))
#                 print(f'your rentals: {current_rentals}')