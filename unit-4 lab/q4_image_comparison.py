import torch
from diffusers import StableDiffusionPipeline

print("Loading image generation model...")

model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")

prompts = [
    "A robotic arm",
    "A robotic arm in a factory",
    "A futuristic robotic arm working in a modern smart factory"
]

for i, prompt in enumerate(prompts, start=1):

    print(f"\nGenerating Image {i}...")
    print("Prompt:", prompt)

    image = pipe(
        prompt,
        num_inference_steps=20
    ).images[0]

    filename = f"comparison_image_{i}.png"

    image.save(filename)

    print("Saved:", filename)

print("\n==========================================")
print("       IMAGE COMPARISON COMPLETED")
print("==========================================")
print("Compare:")
print("1. comparison_image_1.png")
print("2. comparison_image_2.png")
print("3. comparison_image_3.png")
