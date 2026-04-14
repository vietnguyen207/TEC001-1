def convert_to_uppercase(input_file):
    with open(input_file, 'r') as infile:
        content = infile.read()
    
    upper_content = content.upper()
    
    with open("output.txt", 'w') as outfile:
        outfile.write(upper_content)