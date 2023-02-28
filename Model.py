from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

def predict(image,  num_return_sequences):
    """
    A function to predict the sequences using the number of sequences and the image
    :param image:
    :param num_return_sequnces:
    :return list of predictions:
    """
    results = [] # output list

    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

    raw_image = Image.open(image).convert('RGB')

    max_length = 512  # dimensionality of transformer
    num_beams =  num_return_sequences*2  # number of beams is taken as 2 * number of sequences
    # num_beam_groups = num_return_sequnces
    num_return_sequences = num_return_sequences
    temperature = 1.0
    repetition_penalty = 1.0
    top_k = 50
    do_sample = False
    output_scores = True
    # diversity_penalty = 1.5

    # arguments for the generator model
    decoder_kwargs = {
        "max_length": max_length,
        "num_beams": num_beams,
        "num_return_sequences": num_return_sequences,
        "output_scores": output_scores,
        "repetition_penalty": repetition_penalty,
        "top_k": top_k,
        "temperature": temperature,
        # "diversity_penalty": diversity_penalty,
        "do_sample": do_sample,
        # "num_beam_groups": num_beam_groups
    }

    # unconditional image captioning
    inputs = processor(raw_image, return_tensors="pt")

    out = model.generate(**inputs, **decoder_kwargs)
    for i in range(num_return_sequences):
        result = processor.decode(out[i], skip_special_tokens=True)
        print(result)
        results.append(result)

    return results


