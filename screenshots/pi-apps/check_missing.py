import os


get_dir = os.getcwd()
print(os.getcwd())




# open the file in read mode
with open('app.list', 'r') as file:
    # read the contents of the file into a list
    app_list = file.readlines()

# remove the '\n' character from each item in the list
app_list = [item.strip() for item in app_list]

# print the contents of the modified list
#print(app_list)



for item in app_list:
    path = f'{os.getcwd()}/{item}.png'
    check_file = os.path.isfile(path)
    if check_file == False:
        print(f"{item} is missing")
