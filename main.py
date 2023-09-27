import argparse
import joblib
import pandas as pd 
from custom_stat import apply_group_stats_to_test
from Data_prep.data_prep import Data_prep
from r_model.r_model import R_model


def main(args):
    processor = Data_prep(args)
    train, test = processor.forward()
    
    if args.lists:
        # Skip the first list
        for lst in args.lists[1:]:
            train, test = apply_group_stats_to_test(train, test, lst)         

    test = test.drop(['SAMPLE_ID', 'date'], axis=1)
    train = train.drop(['SAMPLE_ID', 'date'], axis=1)

    model = R_model(train,test,args)
    pred = model.run_model()

    test.to_csv('df_test.csv', index=False)
    train.to_csv('df_train.csv', index=False)
    joblib.dump(pred,'result.joblib')
    
    return train, test, pred
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data Preprocessing')

    parser.add_argument('--lists', nargs='*', action='append', help='Multiple lists to be passed. Pass each list as a separate set of arguments.')
    parser.add_argument('--file_path1', type=str, required=True, help='Path to the data file.')
    parser.add_argument('--file_path2', type=str, required=True, help='Path to the data file.')

    # Boolean flags for conditional execution of functions
    parser.add_argument('--load', action='store_true', help='Flag to load data.')
    parser.add_argument('--preprocess', action='store_true', help='Flag to preprocess data.')
    parser.add_argument('--extract_dates', action='store_true', help='Flag to extract date parts.')    
    parser.add_argument('--moving_avg', action='store_true', help='Flag to calculate moving_avg.')

    parser.add_argument('--datetime_col', type=str, default="datetime_column_name", help='Name of the datetime column if extracting dates.')

    parser.add_argument('--model_name', type=str, default="autogluon", help='models')
    parser.add_argument('--auto_time', type=int, default= 4, help='autogluon time')

    args = parser.parse_args()

    # Execute main and capture the returned processor
    train,test,pred = main(args)
    
    print("Processing complete!")
