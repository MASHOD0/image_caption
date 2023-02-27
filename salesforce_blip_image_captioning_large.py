
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

if __name__ == '__main__':

    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

    img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg'
    raw_image = Image.open('image3.png').convert('RGB')

    # kwargs for model
    max_length = 512  # dimensionality of transformers
    num_beams = 10
    num_return_sequences = 5
    temperature = 1.0
    repetition_penalty = 1.0
    top_k = 50
    do_sample = True
    diversity_penalty = 1.5

    decoder_kwargs = {
        "max_length": max_length,
        "num_beams": num_beams,
        "num_return_sequences": num_return_sequences,
        "repetition_penalty": repetition_penalty,
        "diversity_penalty":diversity_penalty,
        "temperature": temperature,
        "top_k": top_k
    }


    # unconditional image captioning
    inputs = processor(raw_image, return_tensors="pt")

    out = model.generate(**inputs, **decoder_kwargs)
    for i in range(5):
        print(processor.decode(out[i], skip_special_tokens=True))
