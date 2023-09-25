import pandas as pd
from tqdm import tqdm

def preprocess(df):
    # Identify rows that meet the condition
    rows_to_remove = df[(df['DIST'] == 0)].index

    # Dropping rows that have 0 distances
    df = df.drop(rows_to_remove, axis=0)

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
    df = df.drop([datetime_col],axis = 1)

    return df

def previous_delays(df, num_instances=2):    
    # Convert year, month, day columns to a single datetime column for easier date manipulations
    df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])

    # The function that will be applied to each group
    def process_group(group):
        group = group.sort_values(by=['datetime'])
        
        # Shift the CI_HOUR column by the specified number of instances
        shifted_values = group['CI_HOUR'].shift(num_instances)
        group['CI_HOUR_shifted'] = shifted_values

        return group

    # Group by 'ARI_CO' and apply the processing function
    df = df.groupby('ARI_CO').apply(process_group).reset_index(drop=True)

    # Drop the auxiliary datetime column
    df = df.drop(columns=['datetime'])
    
    return df
