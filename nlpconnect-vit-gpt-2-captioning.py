from transformers import ViTImageProcessor, AutoTokenizer, VisionEncoderDecoderModel
import torch
from PIL import Image
import csv

def predict_step(image_paths):
    """
    Takes the image path as input and generates the output sequences
    :param image_paths:
    :return list of predictions:
    """

    images = []
    for image_path in image_paths:
        i_image = Image.open(image_path)
        if i_image.mode != "RGB":
            i_image = i_image.convert(mode="RGB")

        images.append(i_image)

    pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    output_ids = model.generate(pixel_values, **gen_kwargs)
    # print(output_ids)

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    return preds


if __name__ == '__main__':

    model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    device = torch.device("cpu")
    model.to(device)

    # csv parameters
    feilds = ['serial_number', 'max_length', 'num_beams', 'num_return_sequences', 'temperature', 'repetition_penalty', 'top_k', 'bad_words_ids', 'do_sample', 'image', 'sentence1', 'sentence2', 'sentence3']
    filename = 'full_test_1.csv'
    count = 0

    # initial parameters
    max_length = 512  #dimensionality of transformers
    num_beams = 4
    num_return_sequences = 3
    temperature = 1.0
    repetition_penalty = 0.0
    top_k = 50
    # max_new_tokens = 20
    bad_words_ids = [[8580]]
    do_sample = True

    with open(filename, 'w') as csvfile:

        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(feilds)

        for i in range(6):
            # updated parameters
            repetition_penalty += 0.5
            for k in range(6):
                top_k += 10
                for l in range(6):
                    temperature += 0.5
                    # kwargs for generating the output
                    gen_kwargs = {
                        "max_length": max_length,
                        "num_beams": num_beams,
                        "num_return_sequences": num_return_sequences,
                        "temperature": temperature,
                        "repetition_penalty": repetition_penalty,
                        "top_k": top_k,
                        "do_sample": do_sample
                        }

                    print(f'params: {gen_kwargs}')

                    for j in range(1, 4):
                        preds = predict_step([f'image{j}.png'])
                        print(f'image : image{j}.png')
                        # writing output to csv file
                        csvwriter.writerow([count, max_length, num_beams, num_return_sequences, temperature,
                                            repetition_penalty, top_k, bad_words_ids, do_sample, f'image{j}.png',
                                            preds[0], preds[1], preds[2]])
                        count += 1
                        print(gen_kwargs)
                        print(preds)

                temperature = 1.0

            top_k = 50

        repetition_penalty = 0.0
