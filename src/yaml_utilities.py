import yaml
import os
import re


# This function pulls out all the paths for the yaml files in a directory
def get_all_yaml_files_in_directory(directory):
    only_files = []
    for x in os.listdir(directory):
        if x.endswith(".yml"):
            only_files.append(tuple([os.path.join(directory, x), x]))
    return only_files


# This function iterates over a yaml file and a supplied lookup value with a delimiter to find the value,
# even for nested elements
def yaml_parameter_lookup(yaml_file, lookup_value, sub_level_delimiter):
    # Splits the lookup segments out
    lookup_segments = lookup_value.split(sub_level_delimiter)

    # Loops over any nested level and pulls the primary value out of the yaml file supplied
    try:
        temp_value = None
        for segment in lookup_segments:
            if temp_value is None:
                temp_value = yaml_file[segment]
            else:
                temp_value = temp_value[segment]
        return temp_value
    except:
        print('the lookup value: "' + lookup_value + '" cannot be found.')
        raise


# This function takes in the variables yaml file and loops over the replacement file, switching out variables with
# their values
def yaml_variable_process(variables_file_path, replacement_path):
    rx = r'\$\{\{([^}^{]+)\}\}'

    # Processes the variables yaml file on itself prior to using it to switch out global values
    variables_lines = yaml_variable_process_self(variables_file_path)

    # Joins all the lines of text and pulls out a yaml variables object from the results
    temp_variables_text = ''.join(variables_lines)
    variables = yaml.safe_load(temp_variables_text)

    # Processes itself first before we do the full replacements
    lines = yaml_variable_process_self(replacement_path)

    # Loop over the yaml file and replace it with our variables
    processed_lines = []
    for line in lines:
        processed_lines.append(re.sub(rx, lambda m: str(yaml_parameter_lookup(variables, m.group()[3:-2], '.')), line))

    # Joins all the processed lines up so its in a single text format again
    temp_text_file = ''.join(processed_lines)

    # Loads it as a yaml file and returns it
    return yaml.safe_load(temp_text_file)


# This function takes in a file path and swaps out the variables within its self
def yaml_variable_process_self(file_path):
    rx = r'\$\{\{\{([^}^{]+)\}\}\}'

    with open(file_path, 'r') as stream:
        variables = yaml.safe_load(stream)

        # Open the yaml file as text
    with open(file_path) as file:
        lines = file.readlines()

    # Loop over the yaml file and replace it with our variables
    processed_lines = []
    for line in lines:
        processed_lines.append(re.sub(rx, lambda m: str(yaml_parameter_lookup(variables, m.group()[4:-3], '.')), line))

    # returns the new processed text array
    return processed_lines
