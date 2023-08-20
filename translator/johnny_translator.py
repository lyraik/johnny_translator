#!/usr/bin/env python3
"""
jhonny_translator_python.py

Description:
    This script transforms assembler code into Johnny Decimal format.
    It also provides an option to output the formatted assembler code which makes 
    it easier to compare it to the jhonny code.
    Be aware that comments on Label get added to the line before the label!
Usage:
    ./jhonny_translator_python.py <inputfile>
    ./jhonny_translator_python.py -a <inputfile>
    ./jhonny_translator_python.py -h

Options:
    -a, --assembler: Output formatted assembler code
    -h, --help: Show help message and exit

Author:
    Simon Karrer

Last Modified:
    20.08.2023

#Bugs
- If the code starts with a loop without a comment the variable addresses/mappings are off by one in the assambler code
- some issues with file creation

License:
    GNU General Public License v3.0
"""
import argparse
import math
import os


def read_content(input_file_path=None, content_string=None):
    if input_file_path:
        with open(input_file_path, 'r') as f:
            return f.readlines()
    elif content_string is not None:  # Explicitly check for None
        return content_string.strip().split('\n')
    else:
        raise TypeError("Either input_file_path or content_string must be provided.")



def transform_assembler_content(input_file_path=None, content_string=None):
    if input_file_path:
        with open(input_file_path, 'r') as f:
            lines = f.readlines()
    elif content_string:
        lines = content_string.strip().split('\n')
    else:
        raise ValueError("Either input_file_path or content_string must be provided.")

    label_to_line = {}
    label_line_offset = 0  # Initialize the offset for label line numbers
    variables = []
    new_lines = []
    comments = {}
    next_var_line = 10
    first_command_encountered = False

    for i, line in enumerate(lines):
        line = line.strip()
        comment = ""
        if ';' in line:
            line, comment = line.split(';', 1)
        line = line.strip()
        if not line and not first_command_encountered:  # Skip empty lines
            continue
        if line and not line.startswith("#define") and not line.endswith(":"):
            first_command_encountered = True

        if line.endswith(':'):
            label = line[:-1]
            label_to_line[label] = len(new_lines) + label_line_offset  # Adjust label line number
            if comment:  # If there is a comment, associate it with the label
                comments[len(new_lines)] = comment.strip()
            new_lines.append('')  # Add an empty line to hold the label's comment
            label_line_offset += 1  # Increment the label line offset
        elif line.startswith("#define"):
            variables.append(line)
        else:
            new_lines.append(line)
            if comment:  # If there is a comment, associate it with the line
                comments[len(new_lines) - 1] = comment.strip()

    for i, line in enumerate(new_lines):
        if "JUMP" in line:
            label = line.split()[-1]
            line_number = label_to_line.get(label, -1) #removed -1
            if line_number != -1 :
                new_lines[i] = f"JUMP {line_number}"


    if variables:
        code_length = len(new_lines)
        next_var_line = math.ceil(code_length / 10) * 10
        while len(new_lines) < next_var_line:
            new_lines.append('0')
        for var in variables:
            new_lines.append(var)

    transformed_content = '\n'.join(
        f"{line} ;{comments.get(i, '')}" if i in comments else line
        for i, line in enumerate(new_lines)
    )


    return transformed_content

def assembler_to_decimal(transformed_content, output_filename):
    COMMANDS = {
        "TAKE": "01",
        "ADD": "02",
        "SUB": "03",
        "SAVE": "04",
        "JUMP": "05",
        "TST": "06",
        "INC": "07",
        "DEC": "08",
        "NULL": "09",
        "HLT": "10"
    }
    decimal_values = []
    lines = transformed_content.strip().split('\n')
    line_offset = 1
    if lines[0].strip().startswith(';'):
        lines.pop(0)

    variable_map = {}

    # Count the number of empty lines (lines with just comments)
    empty_line_count = sum(1 for line in transformed_content.strip().split('\n') if line.strip() == '')

    for line_number, line in enumerate(lines):
        adjusted_line_number = line_number + line_offset
        line = line.split(';')[0].strip()
        if line.startswith("#define"):
            _, var_name, _ = line.split()
            variable_map[var_name] = str(adjusted_line_number).zfill(3)
            print(f"Variable {var_name} mapped to address {variable_map[var_name]}")

    for line in lines:
        line = line.split(';')[0].strip()
        
        if line == '0' or line == '':
            decimal_values.append('00000')
            continue

        if line == "HLT":
            decimal_values.append("10000")
            continue

        if line.startswith("#define"):
            _, _, var_value = line.split()
            decimal_value = "00" + var_value.zfill(3)
            decimal_values.append(decimal_value)
            continue

        try:
            command, address = line.split()
        except ValueError:
            print(f"Error: Invalid line '{line}'")
            continue

        # Update the address if it's a variable
        address = variable_map.get(address, address)

        if command not in COMMANDS:
            print(f"Error: Unknown command '{command}'")
            continue

        decimal_value = COMMANDS[command] + address.zfill(3)

        decimal_values.append(decimal_value)

    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_filepath = os.path.join(output_folder, output_filename)
    with open(output_filepath, 'w') as f:
        extra_line_added = False

        for value in decimal_values:
            if not extra_line_added and value.startswith("00"):
                f.write('00000\n')
                extra_line_added = True

            f.write(value + '\n')

def main():
    parser = argparse.ArgumentParser(description="Transform assembler code to Johnny Decimal format.")
    parser.add_argument("inputfile", type=str, help="The input assembler file.")
    parser.add_argument("-a", "--assembler", action="store_true", help="Output formatted assembler code.")

    args = parser.parse_args()

    input_file = args.inputfile
    output_file = input_file.replace(".asm", ".ram")
    assembler_output_file = "ram_" + input_file

    formatted_assembler_code = transform_assembler_content(input_file)

    if args.assembler:
        with open(assembler_output_file, 'w') as f:
            f.write(formatted_assembler_code)

    assembler_to_decimal(formatted_assembler_code, output_file)

if __name__ == "__main__":
    main()
