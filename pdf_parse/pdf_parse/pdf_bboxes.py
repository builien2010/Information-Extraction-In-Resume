import argparse
import os
from helper import extract_chars, group_chars_into_words, convert_words_csv_to_json, populate_boxes_on_pdf, populate_boxes_on_pdf1, create_csv_file

parser = argparse.ArgumentParser()
parser.add_argument('--input_pdf', type=str, dest='input_pdf',
                    required=True, help="Path of a PDF file.")
parser.add_argument('--output_dir', type=str, dest='output_dir',
                    required=True, help="output dir path")
parser.add_argument('--csv_folder', type=str, dest='csv_folder',
                    required=True, help="output csv folder path")
parser.add_argument('--img_folder', type=str, dest='img_folder',
                    required=True, help="output img folder path")
parser.add_argument('--img_origin', type=str, dest='img_origin',
                    required=True, help="output img origin folder path")
parser.add_argument('--json_folder', type=str, dest='json_folder',
                    required=True, help="output json folder path")

args = parser.parse_args()
path_pdf = args.input_pdf 
output_dir = args.output_dir
csv_folder = args.csv_folder 
img_folder = args.img_folder
img_origin = args.img_origin
json_folder = args.json_folder


# creating output directory if does not exists
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
char_output_dir = "char_output_dir/"
words_output_dir = "words_output_dir/"
if not os.path.exists(output_dir + char_output_dir):
    os.makedirs(output_dir +char_output_dir)
if not os.path.exists(output_dir + words_output_dir):
    os.makedirs(output_dir + words_output_dir)

if not os.path.exists(output_dir + csv_folder):
    os.makedirs(output_dir + csv_folder)
if not os.path.exists(output_dir + json_folder):
    os.makedirs(output_dir + json_folder)
if not os.path.exists(output_dir + img_folder):
    os.makedirs(output_dir + img_folder) 
if not os.path.exists(output_dir + img_origin):
    os.makedirs(output_dir + img_origin)    

def main():

    files_pdf = os.listdir(path_pdf)
    
    for f in files_pdf:

        input_file = path_pdf + f
      
        filepath = input_file

        # extracting filename from filepath
        file_start_pos = filepath.rfind("/")
        filename = filepath[file_start_pos+1:]
        # extracting characters from pdf
        file_start_pos = filepath.rfind("/")
        char_filename = filepath[file_start_pos+1:]
        print("filepath: ", filepath)
        print("char_filename: ", char_filename)
        char_filepath = extract_chars(filepath, char_filename, output_dir)

        # joining characters to make words
        file_start_pos = char_filepath.rfind("/")
        word_filename = char_filepath[file_start_pos+1:]
        word_filepath = group_chars_into_words(char_filepath, word_filename, output_dir)

        # parsing result into a python list to make a JSON like structure
        result = convert_words_csv_to_json(filepath, word_filepath)
        result = convert_words_csv_to_json(input_file, word_filepath)
       
        create_csv_file(result, output_dir + csv_folder +filename)

        populate_boxes_on_pdf(filepath, word_filename, result, output_dir + img_folder)
        populate_boxes_on_pdf1(filepath, word_filename, result, output_dir + img_origin)

        file_start_pos = word_filepath.rfind("/")
        word_filename = word_filepath[file_start_pos+1:]
        f = open(output_dir + json_folder + word_filename + ".json" , "w+")
        f.write(str(result))
        f.close()


main()
