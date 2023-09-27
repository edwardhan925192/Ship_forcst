import pandas as pd
import joblib

def get_submission(pred_path, test_path, name):    

  test = pd.read_csv(test_path)
  pred = joblib.load(pred_path)

  #initializing 
  test['CI_HOUR'] = 0
  
  # Create a mask for rows that do not have 'skip' in column B
  mask = test['DIST'] != 0

  # Use the mask to filter the rows and assign values from values_list
  test.loc[mask, 'CI_HOUR'] = pred
  
  result = test[['ID','CI_HOUR']]
  result.columns = (['ID','prediction'])
  result.to_csv(f'{name}.csv',index = False)
