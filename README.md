# image caption
## Problem Statement
- Create an AI tool that creates captions based on the image provided by the user. Should also have the option to generate multiple captions based on the image.
- Provide an interface where the user can come and upload images and get AI generated captions.
## Solution
### Pre-Processing
- Used the [Blip processor](https://huggingface.co/docs/transformers/v4.26.1/en/model_doc/blip#transformers.BlipProcessor), for processing the image.
### Models
#### 1. Train a  model on the Fliker8k dataset
- Train a image captioning model using CNN and Transformer architecture on the Fliker8k dataset.
- [Fliker8k](https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip) dataset contains 8092 images and 5 captions for each image.
- Disadvantages:
    - The dataset is small and the model will not be able to generalize well.
    - The model will not be able to generate captions for images that are not present in the dataset.
    
#### 2. The `nlpconnect/vit-gpt2-image-captioning` model
- Use the `nlpconnect/vit-gpt2-image-captioning` model to generate captions for the images.
- [nlpconnect/vit-gpt2-image-captioning](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning) model is one of the most downloaded model on the huggingface model hub. It has over 1.1 million downloads.
- [the script used in generating the results](nlpconnect-vit-gpt-2-captioning.py)

##### Results of the `nlpconnect/vit-gpt2-image-captioning` model
- `temprature` adjustments : (https://docs.google.com/spreadsheets/d/1yz25PL-s2VbGVhij0wr9SMotuXexYrgGU-svi4aFIic/edit?usp=sharing)
- experimentation with `top_k` parameter: (https://docs.google.com/spreadsheets/d/1Wfhxj-4AX5WQpGO2v_0B9e0NspoHOsERJw229llngbY/edit?usp=sharing)
- results of the full test of selected `temprature` and `top_k` values:(https://docs.google.com/spreadsheets/d/1Gb1XxMa3S2hSjamPjVTGfNRNz83Ff67HWuOXzQstEIU/edit?usp=sharing)
![image](https://user-images.githubusercontent.com/63853764/221746440-deb4823f-bdb0-4275-8938-343d1da2b53c.png)
- The generated sentences were not good enough.

#### 3. The ` Salesforce Blip image captioning large` model
- **BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation** is a pre-trained model for image captioning.
- The model is trained on the [MS COCO](https://cocodataset.org/#home) dataset.
- The model is trained on the `large` version of the [ViT](https://arxiv.org/abs/2010.11929) architecture.
- This model is selected for the Implementation as the captions generated from this are good
- [Script used for experimentation ](salesforce_blip_image_captioning_large.py)

### Model evaluation
- Simple intuition was used here to evaluate the outputs of various models as the difference between the accuracy of the models was clearly visible.
![image](https://user-images.githubusercontent.com/63853764/221748485-4c1a2481-679a-48e2-b69a-8c4ca3454864.png)
- For example, for the above image the following are sentences generated by `nlpconnect/vit-gpt2-image-captioning` and ` Salesforce Blip image captioning large` models
    - `nlpconnect/vit-gpt2-image-captioning`: a woman in brown outfit holding a white horse behind it in dark cloudy sky
    - ` Salesforce Blip image captioning large` : there are two horses that are standing next to each other in a field
   
### Interface
#### 1.CLI
- A Simple command line application that can be run by running [`runner.py`](/runner.py)
- Prompts the user for location of the folder and number of captions to generate.
- Generates the captions and calculates the time taken to generate the results.
- Suitable for batch generation of captions as it can take multiple images at once
- Selected for implementation
#### 2.GUI
- A web application implemented using frameworks like flask.
- Prompts the user to upload the files, generates and displays the captions on the web interface.
- Requires UI Design and file handling.

### Implementation
#### Data Files
```
📦listed_image_caption
 ┃ 
 ┗ 📂inputs
   ┣ 📜Image1.png
   ┣ 📜Image2.png
   ┗ 📜Image3.png
 
 ```
 #### Code files
 ```
📦listed_image_caption
 ┃
 ┣ 📜Model.py
 ┣ 📜nlpconnect-vit-gpt-2-captioning.py
 ┣ 📜runner.py
 ┗ 📜salesforce_blip_image_captioning_large.py
 ```
 ##### `Model.py`
 Implements the `predict()` which takes the image and number of sequences as input and generates the captions.
 ##### `runner.py`
 Implements the interface of the application.
 ##### `nlpconnect-vit-gpt-2-captioning.py`
 Experiments with the nlpconnect-vit-gpt-2-captioning model.
 ##### `salesforce_blip_image_captioning_large.py`
 Experiments with the salesforce_blip_image_captioning_large model
 

## Improvements and Conclusion
- Create a GUI user interface using flask or tkinter, this will make the application more user friendly.
- The model can be improved by using a larger dataset and training it for a longer period of time.
- The runtimes can be improved by using a GPU.
- Using metrics like BLEU score for model evaluation.
