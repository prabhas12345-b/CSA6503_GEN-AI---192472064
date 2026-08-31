import torch
from diffusers import StableDiffusionPipeline

print("Loading image generation model...")

model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")

prompt = input(
    "\nEnter an engineering image prompt: "
)

print("\nGenerating image...")

image = pipe(
    prompt,
    num_inference_steps=20
).images[0]

image.save("engineering_image.png")

print("\nImage generated successfully!")
print("Saved as: engineering_image.png")
