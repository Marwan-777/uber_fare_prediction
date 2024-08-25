import sys
import pickle
import os


run_id = sys.argv[1]
print('Opening the run files ...')
location = '../development/mlruns/1/' + run_id +'/artifacts/models_pickle'
model_loc = os.listdir(location)[0]
print('Reading the model ...')
with open(location + '/' + model_loc, "rb") as f_in:
    model = pickle.load(f_in)
print('Writing the model ...')
with open('./production_model.bin', 'wb') as f_out:
    pickle.dump(model, f_out)
    

