# listed_image_caption
worksample for listed.inc
## Problem Statement
- Create an AI tool that creates captions based on the image provided by the user. Should also have the option to generate multiple captions based on the image.
- Provide an interface where the user can come and upload images and get AI generated captions.
## Approach
### Finalized approach
- Use the `salesforce blip image captioning large model` to generate captions for the images.
- Use the `num_return_sequences` parameter to generate multiple captions for the same image.
- Use the `repetition_penalty` parameter to penalize the model for repeating the same words.
- Use the `diversity_penalty` parameter to penalize the model for generating similar captions.
- set the `num_beams` parameter to twice the number of return sequences to generate more diverse captions.
- Create a simple cli interface to take the number of sequences as input and generate captions for the images in the `inputs\` folder.
### Initial approach
#### 1. Train a  model on the Fliker8k dataset
- Train a image captioning model using CNN and Transformer architecture on the Fliker8k dataset.
- [Fliker8k](https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip) dataset contains 8092 images and 5 captions for each image.
- Disadvantages:
    - The dataset is small and the model will not be able to generalize well.
    - The model will not be able to generate captions for images that are not present in the dataset.
#### 2. Use the `nlpconnect/vit-gpt2-image-captioning` model
- Use the `nlpconnect/vit-gpt2-image-captioning` model to generate captions for the images.
- [nlpconnect/vit-gpt2-image-captioning](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning) model is one of the most downloaded model on the huggingface model hub. It has over 1.1 million downloads.
- Tried optimizing the parameters for the model but the expected accuracy was not attained here are some the experiments conducted 
#### Results of the `vit-gpt2-image-captioning` model
- `temprature` adjustments : (https://docs.google.com/spreadsheets/d/1yz25PL-s2VbGVhij0wr9SMotuXexYrgGU-svi4aFIic/edit?usp=sharing)
- experimentation with `top_k` parameter: (https://docs.google.com/spreadsheets/d/1Wfhxj-4AX5WQpGO2v_0B9e0NspoHOsERJw229llngbY/edit?usp=sharing)
- results of the full test of selected `temprature` and `top_k` values:(https://docs.google.com/spreadsheets/d/1Gb1XxMa3S2hSjamPjVTGfNRNz83Ff67HWuOXzQstEIU/edit?usp=sharing)

#### Outcomes
- This served as the basis to choose the parameters for the `salesforce blip image captioning large model`


## Salesforce Blip image captioning large
- **BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation** is a pre-trained model for image captioning.
- The model is trained on the [MS COCO](https://cocodataset.org/#home) dataset.
- The model is trained on the `large` version of the [ViT](https://arxiv.org/abs/2010.11929) architecture.

### experimentation with repetition penalty on the `salesforce blip image captioning large model`:
kwargs
```
max_length = 512  # initial 16
num_beams = 10  # initial 4
num_beam_groups = 4
num_return_sequences = 3
temperature = 1.0
repetition_penalty = 1.0
top_k = 50
# max_new_tokens = 20
bad_words_ids = [[8580]]
do_sample = True
output_scores = True
diversity_penalty = 0.001
```
output 
```
of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of 
of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of 
of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of 
```
kwargs
```
max_length = 512  # initial 16
num_beams = 10  # initial 4
num_beam_groups = 4
num_return_sequences = 3
temperature = 1.0
repetition_penalty = 1.0
top_k = 50
# max_new_tokens = 20
bad_words_ids = [[8580]]
do_sample = True
output_scores = True
diversity_penalty = 1.0

```
output
```
there are two horses that are standing next to each other in a field
there are two horses that are standing next to each other in the middle of a field
there are two horses that are standing next to each other in the middle of the field
```
kwargs
```max_length = 512  
    num_beams = 10  
    num_beam_groups = 4
    num_return_sequences = 3
    temperature = 1.0
    repetition_penalty = 1.0
    top_k = 50
    # max_new_tokens = 20
    bad_words_ids = [[8580]]
    do_sample = True
    output_scores = True
    diversity_penalty = 4.5
```
output
```
there are two horses that are standing next to each other in a field
there are two horses that are standing next to each other in the middle of a field
there are two horses that are standing next to each other in the middle of the field
```


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
###### Specifications of the machine
- Laptop
- Lenovo thinkpad t14 gen 2
- Processor: AMD Ryzen 5 PRO 5650U with Radeon Graphics      2.30 GHz
- RAM: 16.0 GB (14.8 GB usable)
- System type: 64-bit operating system, x64-based processor
- OS: Windows 10 Pro

## Improvements and Conclusion
- The model can be improved by using a larger dataset and training it for a longer period of time.
- The model can be improved by using a larger model.
- The runtimes can be improved by using a GPU.