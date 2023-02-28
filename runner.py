"""
The command line interface for using the model.
"""
from Model import predict
import os
import time

path = r"C:\Users\mashh\Documents\git\listed_image_caption\inputs"  # sets path of the input folder
image_file_format = ['.png', '.jpg', '.jpeg']

if __name__ == '__main__':

    print("store the files in the inputs folder")
    alt_path = input("enter the path for the input folder(leave empty if path already provided): ")

    if alt_path != '':
        path = alt_path

    num_return_sequences = int(input("enter the number of return sequences: "))

    start = time.time()

    for (root, dirs, file) in os.walk(path):
        for f in file:

            if '.png' or '.jpg' or '.jpeg' in f:

                image = os.path.join(root, f)
                print(f'filename : {f}')
                results = predict(image, num_return_sequences)

    end = time.time()

    print(f'execution time: {end - start}')
