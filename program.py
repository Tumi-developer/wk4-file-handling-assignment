def process_file(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify the content (convert to uppercase in this example)
        modified_content = content.upper()
        
        # Write to the output file
        with open(output_file, 'w') as file:
            file.write(modified_content)
            
        print(f"Successfully processed {input_file} and wrote to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    input_filename = "input.txt"
    output_filename = "output.txt"
    process_file(input_filename, output_filename)
