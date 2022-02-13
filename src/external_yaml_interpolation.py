from yaml_utilities import *
import argparse


def main(variable_file_path, process_directory, save_directory_location):
    # Gets all the yaml files from the given directory
    replacement_paths_and_names = get_all_yaml_files_in_directory(process_directory)

    # Loops over all the yaml file paths, processes them with the variable swap outs and compiles them within the
    # specified folder name
    for path_and_name in replacement_paths_and_names:

        # Runs the swapping process on the yaml file
        temp_file = yaml_variable_process(variable_file_path, path_and_name[0])

        # Checks if the compiled directory already exists or not, if not it creates it
        if not os.path.exists(save_directory_location):
            os.makedirs(save_directory_location)

        # Creates the new processed file inside the compiled directory
        with open(os.path.join(save_directory_location, path_and_name[1]), 'w') as file:
            yaml.dump(temp_file, file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--variable-file-path', type=str, required=True, help='The variables yaml file path that is going to be used for swapping values out.')
    parser.add_argument('-p', '--process-directory', type=str, required=True, help='The directory path that will be used to iterate over and process all the yaml files inside.')
    parser.add_argument('-s', '--save-directory-location', type=str, required=True, help='The path of the directory you want to save all the compiled yaml files into (this will be created if it does not exist).')

    # Parse the argument
    args = parser.parse_args()

    # Tells the script to run out main function now we have processed the arguments
    main(args.variable_file_path, args.process_directory, args.save_directory_location)