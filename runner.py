# Write your solution here!
 
from classes.Interface import Interface

 


Interface('code platoon').run()

 


#  command description.
# 1. should list all video inventories, including 0 and more
# 2. shuold list customer's current rental videos, by searching customer id. if no videos rented, should display does not have any

# 3. should add new customer, with autp generated ID #, allow user to input F/L name, choose desired account type. (bug need to be fixed, account type entered other than listed will still add new users)

# 4. allow user to rent video. 
# - search customer by id, should display user not found if ID does not exist. 
# - should greet customer if ID found. 
# - if customer has reached account max rentals, will display max rentals reached and exit. 
# - if max rental still not reached, should allow rent
# - allow rent by name, if available, good to go, if not, show out of order

# 5. should allow return a video, search customer by id, 
# - if customer has nothing, should say nothing to return 
# - if there is, display all rented videos, let customer to pick which one to return 

# 6. exit out of the porgram 

# 7. remove a customer
# - should not allow to remove customer, if they still have rentals. 

# 8. display all current customers 

# r. refresh the page, in case something is wrong (and most likely/probly will)