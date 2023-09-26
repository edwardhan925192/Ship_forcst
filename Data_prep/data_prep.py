import pandas as pd
import tqdm as tqdm

class Data_prep:
    def __init__(self, args):
      self.num_instances = args.num_instances
      self.filename1 = args.file_path1
      self.filename2 = args.file_path2
      self.data = None  # Placeholder for the data once loaded
      self.train = None
      self.test = None
    
      if args.load:
        self.train = load_data(self.filename1)
        self.test = load_data(self.filename2)
      if args.preprocess:
        self.train = preprocess(self.train)
        self.test = preprocess(self.test)
      if args.extract_dates:
        self.train = extract_date_parts(self.train,args.datetime_col)
        self.test = extract_date_parts(self.test,args.datetime_col)       

    def forward(self):
        return self.train, self.test
    
    def load_data(df):
      df = pd.read_csv(df)
      print(f" ================= file =============== loaded!")
      return df 

    
    def preprocess(df):
      # Identify rows that meet the condition
      df = df[(df['DIST'] != 0)]      

      print(f" ================= 0 DIST DROPPED ! =============== ")
      
      # Resetting index
      df = df.reset_index(drop=True)

      return df
    
    def extract_date_parts(df, datetime_col):

      # Ensure the column is in datetime format
      df[datetime_col] = pd.to_datetime(df[datetime_col])

      # Extract year, month, and day
      df['year'] = df[datetime_col].dt.year
      df['month'] = df[datetime_col].dt.month
      df['day'] = df[datetime_col].dt.day
      df['hour'] = df[datetime_col].dt.hour      
      df['date'] = df[datetime_col]
      df = df.drop([datetime_col],axis =1)
        
      print(f" ================= Dates extracted ! =============== ")

      return df    
    
    
    def compute_moving_average(self, group_col, window_size=3):
    
        self.data = self.data.sort_values(by=[group_col, 'date'])  # Assuming you have a date column to sort by within each group
        self.data['moving_avg'] = self.data.groupby(group_col)['CI_HOUR'].transform(lambda x: x.rolling(window_size, min_periods=1).mean())
        
        print(f" ================= Moving avg calculated ! =============== ")
        
        return self.data



    
    def get_dataframe(self):
        return self.data

