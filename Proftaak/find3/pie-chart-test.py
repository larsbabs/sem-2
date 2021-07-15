import matplotlib.pyplot as plt
import requests
import threading
  
# Opening JSON file
#f = open(r'C:\Users\larsi\Documents\github\Proftaak\find3\test.json',)
  
# returns JSON object as 
# a dictionary
#data = json.load(f)
def whole_program():
    threading.Timer(180.0, whole_program).start()
    data_pre = requests.get('https://api.pte2.nl/locations/')

    data = data_pre.json()
    plt.rcParams["figure.figsize"] = (20,5)
    # create random data
    def create_percent_list():
        count = 0
        per_cent_list = []
        name_list = []
        while True:
            per_cent_list.append(data['locations'][count]['per_cent'])
            name_list.append(data['locations'][count]['location'])
            count += 1
            if count == len(data['locations']):
                break
        return per_cent_list, name_list


    print(create_percent_list())

    values=create_percent_list()[0]
    names = create_percent_list()[1]
    
    # Create a pieplot
    plt.pie(values, labels=names, labeldistance=1.1, autopct='%.0f%%' ,wedgeprops = { 'linewidth' : 2, 'edgecolor' : 'white' })
    plt.savefig('var/www/html/my_plot.png')
whole_program()