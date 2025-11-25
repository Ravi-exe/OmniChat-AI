

from transformers import AutoProcessor, BlipForConditionalGeneration
from pil import image

model_name="Salesforce/blip-image-captioning-base"


model = BlipForConditionalGeneration.from_pretrained(model_name)

process = AutoProcessor.from_pretrained(model_name)

# Load your image, DON'T FORGET TO WRITE YOUR IMAGE NAME
img_path = "YOUR IMAGE NAME.jpeg"
# convert it into an RGB format 
image = Image.open(img_path).convert('RGB')
.
# You do not need a question for image captioning
text = "the image of"
inputs = process(images=image, text=text, return_tensors="pt")

# Generate a caption for the image
outputs = model.generate(**inputs, max_length=50)

# Decode the generated tokens to text
caption = process.decode(outputs[0], skip_special_tokens=True)
# Print the caption4556
print(caption) 
