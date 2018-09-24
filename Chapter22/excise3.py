import pickle

name = raw_input("Enter your name: ")
age = raw_input("Enter your age: ")
color = raw_input("Enter your favorite color: ")
food = raw_input("Enter your favorite food: ")

detail_list = [name, age, color, food]

pickle_file = open('pickle_file.pkl', 'w')
pickle.dump(detail_list, pickle_file)
pickle_file.close()
