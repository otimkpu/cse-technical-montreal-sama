import os
import sys
import csv
from PIL import Image

color_key = [(1, 1, 1), (0, 0, 0)]
rejected_img = []

def iterate_folder(directory):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith('.png'):
            check_colors(directory,filename)

def check_colors(directory,filename):
    corrected_path = directory + '/' + filename
    img = Image.open(corrected_path).convert('RGB')
    colors = img.getcolors()
    if colors:
        for color in colors:
            if color[1] not in color_key:
                if filename not in rejected_img:
                    rejected_img.append(filename)

def create_csv(directory_in_str, rejected_img):
    with open(directory_in_str + '_reporting.csv', 'w') as outputcsv:
        csv_output = csv.writer(outputcsv)
        csv_output.writerow(['filename'])
        for img in rejected_img:
            csv_output.writerow(img)

if __name__ == '__main__':
    directory_in_str = sys.argv[0]
    directory = 'Question2Images'
    iterate_folder(directory)
    create_csv(directory_in_str, rejected_img)
    print(rejected_img)