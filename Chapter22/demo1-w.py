import pickle

my_list = ['Fred', 73, 'Hello there', 81.9876e-13]

pickle_file = open('my_pickled_list.pkl', 'w')
pickle.dump(my_list, pickle_file)
pickle_file.close()