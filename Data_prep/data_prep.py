import pandas as pd
import tqdm as tqdm

class Data_prep:
    def __init__(self, args):
      self.num_instances = args.num_instances
      self.filename = args.file_path
      self.data = None  # Placeholder for the data once loaded

      if args.load:
        self.load_data()
      if args.preprocess:
        self.preprocess()
      if args.extract_dates:
        self.extract_date_parts(args.datetime_col)
      if args.previous_delays:
        self.previous_delays(args.num_instances)



    
    def load_data(self):
      self.data = pd.read_csv(self.filename)
      print(f" ================= {self.filename}=============== loaded!")



    
    def preprocess(self):
      # Identify rows that meet the condition
      rows_to_remove = self.data[(self.data['DIST'] == 0)].index

      # Dropping rows that have 0 distances
      self.data = self.data.drop(rows_to_remove, axis=0)

      print(f" ================= 0 DIST DROPPED ! =============== ")
      
      # Resetting index
      self.data = self.data.reset_index(drop=True)

      return self.data



    
    def extract_date_parts(self, datetime_col):

      # Ensure the column is in datetime format
      self.data[datetime_col] = pd.to_datetime(self.data[datetime_col])

      # Extract year, month, and day
      self.data['year'] = self.data[datetime_col].dt.year
      self.data['month'] = self.data[datetime_col].dt.month
      self.data['day'] = self.data[datetime_col].dt.day
      self.data['hour'] = self.data[datetime_col].dt.hour
      self.data = self.data.drop([datetime_col],axis = 1)

      print(f" ================= Dates extracted ! =============== ")

      return self.data


    
    def previous_delays(self, num_instances=2):    
        # Convert year, month, day columns to a single datetime column for easier date manipulations
        self.data['datetime'] = pd.to_datetime(self.data[['year', 'month', 'day', 'hour']])
    
        # The function that will be applied to each group
        def process_group(group):
          group = group.sort_values(by=['datetime'])
          
          # Create num_instances number of shifted columns
          for i in range(1, num_instances + 1):
              shifted_values = group['CI_HOUR'].shift(i)
              group[f'CI_HOUR_shifted{i}'] = shifted_values
    
          return group
    
    
        # Group by 'ARI_CO' and apply the processing function
        self.data = self.data.groupby('ARI_CO').apply(process_group).reset_index(drop=True)
    
        # Drop the auxiliary datetime column
        self.data = self.data.drop(columns=['datetime'])

        print(f" ================= Delays calculated ! =============== ")
        
        return self.data

    
