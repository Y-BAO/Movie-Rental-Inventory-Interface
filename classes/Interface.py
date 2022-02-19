

from classes.Store import Store



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
                self.store.show_all_customers()
                print('\n')

            if mode == '3':
                self.add_customer_info()




            if mode == '6':
                print("see you soon")
                break

            if mode == '7':
                self.remove_customer_info()





    def menu(self):
        return f"== Welcome to {self.name} Video! ==\n1. View store video inventory\n2. View customer rented videos\n3. Add new customer\n4. Rent video\n5. Return video\n6. Exit\n===>"


    def add_customer_info(self):
        customer_info = {}
        customer_info['id'] = input('enter an id')
        customer_info['account_type'] = input('enter account type')
        customer_info['first_name'] = input('enter first name')
        customer_info['last_name'] = input('enter last name')
        customer_info['current_video_rentals'] = 'none'
        self.store.add_customer(customer_info)

        