

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

            
            elif mode == '2':
                print('\n')
                customer_id =  input("enter customer id: ")
             
                self.store.view_rentals(customer_id)

                print('\n')


            elif mode == '3':
                print('\n')
                customer_info = self.store.add_customer_info()
                print(f'\n\nthank you for creating your account with us, these are your account information\n\n')
                for x, y in customer_info.items():
                    print(f"{x} : {y}")
            

            elif mode == '4':
                print('\n')
                customer = self.check_id()
                customer_id = customer.id
                account_type = customer.account_type
                current_rentals = customer.current_video_rentals
                if self.check_count(account_type,current_rentals):
                    video_title = input('enter a title: ')
                    if self.check_rating(customer.account_type,video_title):

                        if self.check_availability(video_title):
                            self.rent_to_customer(customer.id,video_title)
                            print(f'your have rented: {video_title}')

            elif mode == '5':
                print('\n')
                customer = self.check_id()
                current_rentals = customer.current_video_rentals
                if len(current_rentals) == 0:
                    print('\n')
                    print('you have nothing to return')
                else:
                    print('\n')
                    print(f"\n{self.store.view_rentals(customer.id)}\nWhich one would you like to return?")
                    print('\n')
                    video_title = input('enter a title: ')
                    customer_id = customer.id
                    if video_title == '':
                        return self.run()
                    self.remove_from_customer(video_title,customer_id)
            # customer.current_video_rentals.split('/')


            elif mode == '6':
                print("see you soon")
                break

            elif mode == '7':
                self.remove_customer_info()

            elif mode == '8':
                self.store.show_all_customers()
                
            elif mode == 'r':
                Interface('code platoon').run()

            else:
                print('command not found')

    def check_rating(self,account_type,video_title):
        rating = ''
        for info in self.store.inventory:
            if info.title == video_title:
                rating = info.rating
        if account_type == 'pf' or account_type == 'sf' and rating == 'R':
            print('your account type does not allow this video')
            return False
        else:
            return True









            

    def rent_to_customer(self,customer_id,video_title):
        for info in self.store.customers:
            if info.id == customer_id:
                if len(info.current_video_rentals) == 0:
                    info.current_video_rentals = video_title
                    # print(info.current_video_rentals)
                else:
                    info.current_video_rentals = info.current_video_rentals + '/' + video_title
                    # print(info.current_video_rentals)
        self.store.update_customer_list()
         
        self.reduce_inventory(video_title )
    
    def reduce_inventory(self,video_title):
        for info in self.store.inventory:
            if info.title == video_title:
                info.copies_available = str(int(info.copies_available) - 1)
            self.store.update_inventory_list()

         



    def show(self,video_title):
        for info in self.store.inventory:
            if info.title == video_title:
                print(info.copies_available)



    def remove_from_customer(self,video_title,customer_id):
        for info in self.store.customers:
            if info.id == customer_id:
                print(info.current_video_rentals)

                videos = info.current_video_rentals.split('/') 
                print(videos)
                for item in videos:
                    if item == video_title:
                        videos.remove(item)
                         
                        break
                
                info.current_video_rentals = '/'.join(videos)
                print(info.current_video_rentals)
                self.store.update_customer_list()
                self.increase_inventory(video_title)
                print(f'you have returned {video_title}')
                break
            
            
            
          
         
             
    
    def increase_inventory(self,video_title):
        for info in self.store.inventory:
            if info.title == video_title:
                info.copies_available = str(int(info.copies_available) + 1)
                # print(info.copies_available)
                
                break
        self.store.update_inventory_list()
             
        
                



            
                


 
    def check_availability(self,video_title):
        for info in self.store.inventory:
            if info.title == video_title:
                stock = info.copies_available
                if int(stock) == 0:
                    print('sorry, this video is currently out of order')
                
                else:
                    return True
    
          

            
    
  
             
         
                 
        
                
               
                
                
                
                    
                     
                
                



          


    def remove_customer_info(self):
        customer_id = str(input('enter an id: '))
        
        self.store.delete_customer(customer_id)




    def menu(self):
        return f"\n\n\n== Welcome to {self.name} Video! ==\n1. View store video inventory\n2. View customer rented videos\n3. Add new customer\n4. Rent video\n5. Return video\n6. Exit\n7. remove a customer\n8: show all customers\nr. Refresh\n===> "


    
     
                

    def check_id(self):
        while True:
            id_of_customer = input('enter your id: ')
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
                         

























 