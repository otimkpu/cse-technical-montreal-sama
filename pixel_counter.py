from PIL import Image
import json
import os

def get_files(directory):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        count_pixels(directory, filename)
        
def count_pixels(directory, filename):
    path = directory + '/' + filename
    pixels = {}
    im = Image.open(path).convert('RGB')
    for pixel in im.getdata():
        pixel = str(pixel)
        if not pixel in pixels:
            pixels[pixel] = 1
        else:
            pixels[pixel] += 1
    
    print(f'Total Pixels in {filename} are: {len(pixels)}')
    with open(f'{filename}.json', 'w', encoding='utf-8') as f:
        json.dump(pixels, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # Set the directory for the files for which pixels are to be counted.
    directory = 'Question1Images'
    get_files(directory)
