import csv
import sys
import validators

def gen_cart_link():
    file = open(sys.argv[1], newline='')
    data = list(csv.reader(file, delimiter=','))
    file.close()
        
    first_line = data.pop(0)[0]
    
    if not validators.url(first_line):
        return
    
    url = first_line + "cart/"
    items = []
            
    for row in data:
        if len(row) == 1:
            items.append(row[0] + ":1")
        elif len(row) == 2:
            items.append(row[0] + ":" + row[1])
        
    return url + ",".join(items) + "?payment=shop_pay"
    
print(gen_cart_link())