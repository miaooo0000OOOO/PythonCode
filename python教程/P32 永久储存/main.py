import pickle
data = [1,2,3,[1,2,3,[1,2,3]]]

pickle_file = open('data.pkl', 'wb')
pickle.dump(data, pickle_file)
pickle_file.close()

pickle_file = open('data.pkl', 'rb')
restoredData = pickle.load(pickle_file)
print(restoredData)
pickle_file.close()