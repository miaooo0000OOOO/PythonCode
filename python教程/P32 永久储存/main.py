import pickle
import os
data = [1,2,3,[1,2,3,[1,2,3]]]
path = os.path.dirname(__file__) + '\\'

pickle_file = open(path + 'data.pkl', 'wb')
pickle.dump(data, pickle_file)
pickle_file.close()

pickle_file = open(path + 'data.pkl', 'rb')
restoredData = pickle.load(pickle_file)
print(restoredData)
pickle_file.close()