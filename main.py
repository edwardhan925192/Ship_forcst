import argparse
from Data_prep.data_prep import Data_prep


def main(args):
    processor = Data_prep(args)
    return processor


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data Preprocessing')

    parser.add_argument('--num_instances', type=int, default=2, help='Number of shifted instances required.')
    parser.add_argument('--file_path', type=str, required=True, help='Path to the data file.')

    # Boolean flags for conditional execution of functions
    parser.add_argument('--load', action='store_true', help='Flag to load data.')
    parser.add_argument('--preprocess', action='store_true', help='Flag to preprocess data.')
    parser.add_argument('--extract_dates', action='store_true', help='Flag to extract date parts.')
    parser.add_argument('--previous_delays', action='store_true', help='Flag to calculate previous delays.')

    parser.add_argument('--datetime_col', type=str, default="datetime_column_name", help='Name of the datetime column if extracting dates.')

    args = parser.parse_args()

    # Execute main and capture the returned processor
    processor_result = main(args)

    # Print some properties or information about the processor
    # For demonstration, let's just print a message to confirm completion
    print("Processing complete!")
