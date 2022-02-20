# from asyncore import read
# import csv
from operator import indexOf
import re
import string
import random


# all_customers = []
# with open('/Users/yilinbao/Desktop/assessment-2/data/customers.csv','r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         all_customers.append(line)

# print(all_customers)


 








    # filednames = ['id','account_type','first_name','last_name','current_video_rentals']

    # csv_writer = csvDictWriter()
 

# arr = ['a','b','c','d','e']
# for i in arr:
#     if i == 'a':
#         print(i)

new_id = ''.join(random.sample(string.ascii_letters + string.digits,5))
print(new_id)