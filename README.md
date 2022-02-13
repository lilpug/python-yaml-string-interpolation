# Python Yaml String Interpolation Library

This library allows you to compile yaml files so string interpolation can be done.

## Requirements

This library requires the pyyaml package, you can install it like so.

```
pip install pyyaml
```

## Library Commands

In the src folder, the library has two main modules which can be used, these are as followed:-

- external_yaml_interpolation
- self_yaml_interpolation

### external_yaml_interpolation

The external_yaml_interpolation module runs both a self version on all yaml files invovled and it also uses the variable yaml file to replace any global variables in the supplied directory.

#### Syntax

```
-v/--variable-file-path (The variables yaml file path that is going to be used for swapping values out.)

-p/--process-directory (The directory path that will be used to iterate over and process all the yaml files inside.)

-s/--save-directory-location (The path of the directory you want to save all the compiled yaml files into (this will be created if it does not exist).)

```

#### Command Example

```
python .\external_yaml_interpolation.py -v ..\example-structure\variables.yml -p ..\example-structure\random-resource\ -s ..\example-structure\compiled\random-resource
```


### self_yaml_interpolation

The self_yaml_interpolation module runs only replaces variables on the single file supplied.

#### Syntax

```
-y/--yaml-file-path (The yaml file path which will be processed on itself.)

-s/--save-path (The path where you want the processed yaml file to be saved.)

```

#### Command Example

```
python .\self_yaml_interpolation.py -y ..\example-structure\random-resource\random-database.yml -s ..\example-structure\random-resource\random-database-new.yml
```


## How To Define Template Variables

Below is an explanation on how to define the two different types of variables using this library.

### Local Variable Usages

Local variables relating to the same file can be used, see the below snippet examples for how to do it.

#### Base Level Syntax

```
${{{variable_name_here}}}
```

#### Nested Level Syntax

```
${{{base.level_2_example.level_3_example}}}
```

#### An Example Usage

file-to-be-processed.yml:
```yaml
primary_variable_example: "this will be used to replace anything referencing it."
base_level:
	level_1_name: "this will also be replaced when referenced."
	
single_level_usage_example: "${{{primary_variable_example}}} (we can also add anything before and after it if we want)"
nested_level_usage_example: "${{{base_level.level_1_name}}} (we can also add anything before and after it if we want)"	
```


### Global Template Variable Usages

Global variables can be used by referencing an external yaml file, this can be seen with the below snippet examples.


#### Global Level Syntax

```
${{variable_name_here}}
```

#### Nested Global Level Syntax

```
${{base.level_2_example.level_3_example}}
```

#### An Example Usage

variables.yml:
```yaml
primary_variable_example: "this will be used to replace anything referencing it."
base_level:
	level_1_name: "this will also be replaced when referenced."
```

file-to-be-processed.yml:
```yaml	
single_level_usage_example: "${{primary_variable_example}} (we can also add anything before and after it if we want)"
nested_level_usage_example: "${{base_level.level_1_name}} (we can also add anything before and after it if we want)"	
```