import argparse
import pandas as pd 
from Data_prep.data_prep import Data_prep


def main(args):
    processor = Data_prep(args)
    processed_dataframe = processor.get_dataframe()
    processed_dataframe = processed_dataframe.drop(['SAMPLE_ID','ID','date'],axis = 1)
    processed_dataframe.to_csv('processed_df.csv',index = False) 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data Preprocessing')

    parser.add_argument('--num_instances', type=int, default=2, help='Number of shifted instances required.')
    parser.add_argument('--f_num_instances', type=int, default=2, help='Number of shifted instances required.')
    parser.add_argument('--delay_group', type=str, default='ARI_CO', help='Number of shifted instances required.')
    parser.add_argument('--f_delay_group', type=str, default='ARI_CO', help='Number of shifted instances required.')
    parser.add_argument('--avg_group', type=str, default='ARI_PO', help='Number of shifted instances required.')
    parser.add_argument('--avg_window', type=int, default=3, help='Number of shifted instances required.')
    parser.add_argument('--file_path', type=str, required=True, help='Path to the data file.')

    # Boolean flags for conditional execution of functions
    parser.add_argument('--load', action='store_true', help='Flag to load data.')
    parser.add_argument('--preprocess', action='store_true', help='Flag to preprocess data.')
    parser.add_argument('--extract_dates', action='store_true', help='Flag to extract date parts.')
    parser.add_argument('--previous_delays', action='store_true', help='Flag to calculate previous delays.')
    parser.add_argument('--future_delays', action='store_true', help='Flag to calculate future delays.') 
    parser.add_argument('--moving_avg', action='store_true', help='Flag to calculate moving_avg.')

    parser.add_argument('--datetime_col', type=str, default="datetime_column_name", help='Name of the datetime column if extracting dates.')

    args = parser.parse_args()

    # Execute main and capture the returned processor
    processor_result = main(args)

    # Print some properties or information about the processor
    # For demonstration, let's just print a message to confirm completion
    print("Processing complete!")
