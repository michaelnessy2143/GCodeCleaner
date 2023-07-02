import re

def extract_xyz_values(gcode_file, output_file):
    try:
        # Open the input file in read mode
        with open(gcode_file, 'r') as file:
            # Read all lines from the input file
            lines = file.readlines()
    except FileNotFoundError:
        # Handle the case when the input file is not found
        print(f"Error: Input file '{gcode_file}' not found.")
        return
    except IOError:
        # Handle the case when there is an error opening the input file
        print(f"Error: Unable to open input file '{gcode_file}'.")
        return

    # Initialize variables to hold the previous X, Y, Z, and E values
    previous_x = previous_y = previous_z = previous_e = None

    # Create a list to store the cleaned lines
    cleaned_lines = []
    for line in lines:
        line = line.strip()

        # Use regular expressions to match X, Y, Z, and E values
        x_match = re.search(r'X([-+]?\d+\.?\d*)', line)
        y_match = re.search(r'Y([-+]?\d+\.?\d*)', line)
        z_match = re.search(r'Z([-+]?\d+\.?\d*)', line)
        #e_match = re.search(r'E([-+]?\d+\.?\d*)', line)

        # Update the previous values if matches are found
        if x_match:
            previous_x = x_match.group(1)
        if y_match:
            previous_y = y_match.group(1)
        if z_match:
            previous_z = z_match.group(1)
        #if e_match:
            #previous_e = e_match.group(1)

        # Create a string with the extracted values, using previous values if new values are None
        extracted_values = []
        if previous_x is not None:
            extracted_values.append(f"X{previous_x}")
        if previous_y is not None:
            extracted_values.append(f"Y{previous_y}")
        if previous_z is not None:
            extracted_values.append(f"Z{previous_z}")
        #if previous_e is not None:
            #extracted_values.append(f"E{previous_e}")

        cleaned_line = " ".join(extracted_values)
        cleaned_lines.append(cleaned_line)

    try:
        # Open the output file in write mode
        with open(output_file, 'w') as file:
            # Write the cleaned lines to the output file
            file.write('\n'.join(cleaned_lines))
    except IOError:
        # Handle the case when there is an error writing to the output file
        print(f"Error: Unable to write to output file '{output_file}'.")
        return

    # Print a success message indicating the extraction of X, Y, Z, and E values
    print(f"X, Y, Z, E values extracted from '{gcode_file}'. Cleaned output saved to '{output_file}'.")


# Prompt for input and output file paths
gcode_file = input("Enter the path to the input G-code file: ")
output_file = input("Enter the path to save the cleaned output: ")

# Call the extract_xyz_values function with the provided file paths
extract_xyz_values(gcode_file, output_file)
