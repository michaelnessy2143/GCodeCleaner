# GCodeCleaner
This code takes all the unnecessary data out of the g-code leaving only the X,Y,Z,E values.  This is for the purpose of taking the output from a slicer like Cura or PrusaSlicer and passing the output to a 6-axis 3D printer.


Description:
This script removes comments from a G-code file and extracts the X, Y, Z, and E values from each line. It produces a cleaned output file with the extracted values.

Usage:
1. Run the script and provide the path to the input G-code file.
2. Enter the path to save the cleaned output file.
 Make sure that the paths provided are not surronded by "quotes"
3. The script will remove comments and extract X, Y, Z, and E values from the input file.
4. The cleaned output file will be saved in the specified path.

Functions:
1. remove_comments(gcode_file, output_file):
    - Removes comments from the input G-code file and extracts X, Y, Z, and E values.
    - Parameters:
        - gcode_file (str): Path to the input G-code file.
        - output_file (str): Path to save the cleaned output file.
    - Returns: None

Example Usage:
1. Input:
    Enter the path to the input G-code file: /path/to/input.gcode
    Enter the path to save the cleaned output: /path/to/output.txt
   Output:
    X, Y, Z, E values extracted from '/path/to/input.gcode'. Cleaned output saved to '/path/to/output.txt'.

Note:
- The script assumes that the G-code file is in a readable format.
- The output file will contain extracted X, Y, Z, and E values in the same format as the input file, with each line representing a set of values.
- The script uses regular expressions to remove comments and extract the desired values.
- Make sure to have the necessary permissions to read the input file and write to the output file.

