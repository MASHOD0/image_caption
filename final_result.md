## Final Results
#### Number of sequences: 1
```
store the files in the inputs folder
enter the number of return sequences:1
filename : Image1.png
there is a man that is running with a soccer ball in his hand
filename : Image2.png
there are two horses that are standing next to each other in a field
filename : Image3.png
this is an image of a group of people who are looking at the camera
execution time: -55.94046330451965
```
#### Number of sequences: 2
```
enter the number of return sequences:2
filename : Image1.png
there is a man that is running with a soccer ball in his hand
there is a man that is running with a soccer ball on the field
filename : Image2.png
there are two horses that are standing next to each other in a field
there are two horses that are standing next to each other in the field
filename : Image3.png
this is an image of a group of people who are looking at each other
this is an image of a group of people who are looking at the camera
execution time: 82.42946815490723
```
#### Number of sequences: 3
```
store the files in the inputs folder
enter the number of return sequences:3
filename : Image1.png
there is a man that is running with a soccer ball in his hand
there is a man that is running with a soccer ball on the field
there is a male soccer player running with a soccer ball in his hand
filename : Image2.png
there are two horses that are standing next to each other in a field
there are two horses that are standing next to each other in the field
there are two horses that are standing next to each other on a field
filename : Image3.png
this is an image of a group of people who are looking at each other
this is an image of a group of four people who are looking at each other
this is an image of a group of people who are looking at the camera, with the caption of
execution time: 86.40368580818176
```
#### Number of sequences: 4
```
store the files in the inputs folder
enter the number of return sequences:4
filename : Image1.png
this is a picture of a soccer player running with a soccer ball in his hand
there is a man that is running with a soccer ball in his hand
this is a picture of a soccer player running with the ball in his hand
this is a picture of a soccer player running with a soccer ball in front of him
filename : Image2.png
there are two horses that are standing next to each other in a field
there are two horses that are standing next to each other in the field
there are two horses that are standing next to each other on a field
there are two horses that are standing next to each other in the grass
filename : Image3.png
this is an image of a group of people who are looking at each other
this is an image of a group of four people who are looking at each other
this is an image of a group of people who are looking at the camera
this is an image of a group of four people who are looking at the same time of the day
execution time: 89.17089343070984
```
#### Number of sequences: 5
```
store the files in the inputs folder
enter the number of return sequences:5
filename : Image1.png
this is a picture of a soccer player running with a soccer ball in his hand
there is a man that is running with a soccer ball in his hand
this is a picture of a soccer player running with the ball in his hand
this is a picture of a soccer player running with a soccer ball in front of him
there is a man that is running with a soccer ball in front of him
filename : Image2.png
there are two horses that are standing next to each other in a field
there are two horses that are standing next to each other in the middle of a field
there are two horses that are standing next to each other in the middle of the field
there are two horses that are standing next to each other in the field
there are two horses that are standing next to each other on a field
filename : Image3.png
this is an image of a group of people who are looking at each other
this is an image of a group of four people who are looking at each other
this is an image of a group of people who are looking at the camera
this is an image of a group of four people who are looking at the same time of the day
this is an image of a group of four people who are looking at the same time of day
execution time: 97.09602332115173
```

### Implementation
- Use the `salesforce blip image captioning large model` to generate captions for the images.
- Use the `num_return_sequences` parameter to generate multiple captions for the same image.
- Use the `repetition_penalty` parameter to penalize the model for repeating the same words.
- Use the `diversity_penalty` parameter to penalize the model for generating similar captions.
- set the `num_beams` parameter to twice the number of return sequences to generate more diverse captions.
- Create a simple cli interface to take the number of sequences as input and generate captions for the images in the `inputs/` folder.

###### Specifications of the machine
- Processor: AMD Ryzen 5 PRO 5650U with Radeon Graphics      2.30 GHz
- RAM: 16.0 GB (14.8 GB usable)
- System type: 64-bit operating system, x64-based processor
- OS: Windows 10 Pro
