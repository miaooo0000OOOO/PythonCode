import pickle
import os
data = "hello world!"
path = os.path.dirname(__file__) + '\\'
with open(path + "savedData.pkl", 'wb') as f:
    pickle.dump(data, f)
