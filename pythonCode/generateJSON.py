# ===================================================================
# == CSV file can NOT include table names when export from Numbers ==
# ===================================================================


import csv
import json
from operator import truediv

# Constants to make everything easier
# CSV_PATH = './mine/pythonCode/FallingPrice_Log.csv'
# JSON_PATH = './mine/pythonCode/db.json'
CSV_PATH = './pythonCode/FallingPrice_Log.csv'
JSON_PATH = './pythonCode/db.json'
# CSV_PATH = './JavaScript/YouTube/20220519_Build15JavaScriptProject_Vanilla_JavaScript_Course/javascript-basic-projects-master/29-comfy-store/mine/pythonCode/FallingPrice_Log.csv'
# JSON_PATH = './JavaScript/YouTube/20220519_Build15JavaScriptProject_Vanilla_JavaScript_Course/javascript-basic-projects-master/29-comfy-store/mine/pythonCode/db.json'


# Reads the file the same way that you did
csv_file = csv.DictReader(open(CSV_PATH, 'r'))

# Created a list and adds the rows to the list
json_list = []
i = 1

# different way to read csv file
# with open(CSV_PATH, 'r') as file:
#     csv_reader = csv.reader(file)
#     for line in csv_reader:
#         print(line['Item name'])


for row in csv_file: #=====
    # print(i, row, '\n')
    # i += 1

    product_info = {}

    # image = [
    #             {
    #             "url" : 'http://127.0.0.1:5501/mine/images/Products/1.jpg'
    #             }
    #         ]

    
    #===================== test
    if (row['Item name'] and row['Status']=='Waiting to sell'):

        if row['Image name'].startswith('Screen'):
            imageName = row['Image name'] + '.png'
        else:
            imageName = row['Image name'] + '.jpeg'

        # imageLink = 'http://127.0.0.1:5501/mine/images/Products/' + imageName
        imageLink = 'http://127.0.0.1:5501/images/Products/' + imageName   

        image = [
            {
            "url" : imageLink
            }
        ]

        fields = {
            "company" : row['Category'],
            "colors" : ["#f15025","#222"],    #======> delete this row
            # product_info["id"] : str(i).rjust(6,'0'),
            # product_info["fields"] : fields,
            "featured" : False,
            "price" : float(row['Unit price'].replace('$','').replace(',','')), # replace currency str: '$' ',' => ''
            "name" : row['Item name'],
            "description" : row['Comments'],
            "image" : image
        }



        # set single product json content
        product_info["id"] = str(i).rjust(6,'0')
        product_info["fields"] = fields
        # product_info["featured"] = True
        # product_info["price"] = row['Unit price']
        # product_info["name"] = row['Item name']
        # product_info["image"] = image

        json_list.append(product_info)

        # json_list.append(row)

    print(i, row, '\n')
    i += 1
    

    print('\n'*3)


# Writes the json output to the file
open(JSON_PATH, 'w').write("{ \"posts\" : " + json.dumps(json_list, indent=4) + "}")

print("Total records: ", len(json_list))