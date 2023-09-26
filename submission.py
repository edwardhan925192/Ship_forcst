import pandas as pd
import joblib

def get_submission(pred_path, test_path, name):
  test = pd.read_csv('test_path')
  pred = joblib.load(pred_path)
  result = pd.concat([pd.Series(pred),(test['TEST_ID'])],axis = 1)
  result.columns = (['ID','prediction'])
  result.to_csv(f'{name}.csv',index = False)
