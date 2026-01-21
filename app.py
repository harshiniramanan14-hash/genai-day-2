
prompt = "A home in peaceful place with garden in the front "

# Generate the image
# You can adjust `num_inference_steps` for quality vs. speed
# You can also add `guidance_scale` to control how much the image adheres to the prompt
image = pipeline(prompt, num_inference_steps=25).images[0]

# Display the generated image
plt.imshow(image)
plt.axis('off') # Hide axes ticks and labels
plt.title(f"Generated Image for: '{prompt[:50]}...'\n")
plt.show()

print("Image generation complete!")
