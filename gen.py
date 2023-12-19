import csv
import sys
import validators

def gen_cart_link():
    if len(sys.argv) < 2:
        print("Please enter a filepath as an argument")
        return
    
    # open file
    file = open(sys.argv[1], newline='')
    data = list(csv.reader(file, delimiter=','))
    file.close()
        
    # get shop url
    shop_url = data.pop(0)[0]
    
    # check if valid url
    if not validators.url(shop_url):
        return
    
    url = shop_url + "cart/"
    items = []
            
    # append items to link
    for row in data:
        if len(row) == 1: # case if no quantity is defined
            items.append(row[0] + ":1")
        elif len(row) == 2: #case if a quantity is defined
            items.append(row[0] + ":" + row[1])
        
    print(url + ",".join(items) + "?payment=shop_pay")
    
gen_cart_link()