import pandas as pd
import joblib

def submission(pred_path, test_path, name):

  test = pd.read_csv(test_path)
  pred = joblib.load(pred_path)

  result = pd.concat([test['ID'],pd.Series(pred)],axis = 1)
  result.columns = (['ID','수요량'])
  result.to_csv(f'{name}.csv',index = False)

def direct_submission(pred, test_path, name):    

  test = pd.read_csv(test_path)  
  
  result = pd.concat([test['ID'],pd.Series(pred)],axis = 1) 
  result.columns = (['ID','수요량'])
  result.to_csv(f'{name}.csv',index = False)

def ensemble(path1,path2,name):

  df1 = pd.read_csv('path1')
  df2 = pd.read_csv('path2')

  mean_수요량 = (df1['수요량'] + df2['수요량']) / 2
  result = pd.concat([df1['ID'],pd.Series(mean_수요량)],axis = 1)
  result.to_csv(f'{name}.csv',index = False)

def ensemble_three(path1,path2,path3,name):

  df1 = pd.read_csv('path1')
  df2 = pd.read_csv('path2')
  df3 = pd.read_csv('path3')

  mean_수요량 = (df1['수요량'] + df2['수요량'] + df3['수요량']) / 3
  result = pd.concat([df1['ID'],pd.Series(mean_수요량)],axis = 1)
  result.to_csv(f'{name}.csv',index = False)

def add_mean_column(train_df, test_df, group_col, target_col):        
    
  mean_values = train_df.groupby(group_col)[target_col].mean().reset_index()  
  
  merged_train = train_df.merge(mean_values, on=group_col, how='left', suffixes=('', '_mean'))
  merged_test = test_df.merge(mean_values, on=group_col, how='left', suffixes=('', '_mean'))
  
  return merged_train, merged_test

# Usage:
# merged_train, merged_test = add_mean_column(train, test, '쇼핑몰 구분', '수요량')

def gen_items(train,test):
  words = ["한과", "과일", "홍삼", "스팸", "버섯", "새우", "샤인", "견과류", "곶감", "한우", "올리브유", "굴비"]
  
  pattern = "|".join(words)
  
  # Extract the words into a new column
  train['extracted_words'] = train['선물 유형'].str.findall(pattern).apply(','.join)
  test['extracted_words'] = test['선물 유형'].str.findall(pattern).apply(','.join)

  return train, test 
