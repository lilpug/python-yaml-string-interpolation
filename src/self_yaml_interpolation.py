from lib.yaml_utilities import *
import argparse


def main(yaml_file_path, save_path):
    # Returns all the file text in an array in its processed state
    processed_lines = yaml_variable_process_self(yaml_file_path)

    # Joins all the processed lines up so its in a single text format again
    temp_text_file = ''.join(processed_lines)

    # Loads it as a yaml file, so it does all the processing and formatting
    temp_file = yaml.safe_load(temp_text_file)

    # Saves the new processed file
    with open(save_path, 'w') as file:
        yaml.dump(temp_file, file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-y', '--yaml-file-path', type=str, required=True, help='The yaml file path which will be processed on itself.')
    parser.add_argument('-s', '--save-path', type=str, required=True, help='The path where you want the processed yaml file to be saved.')

    # Parse the argument
    args = parser.parse_args()

    # Tells the script to run out main function now we have processed the arguments
    main(args.yaml_file_path, args.save_path)
