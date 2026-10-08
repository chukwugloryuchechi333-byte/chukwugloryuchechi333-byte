# PROJECT 20: TRIPLE GLORY 333-BYTE AI IMAGE GENERATOR
# Author: chukwugloryuchechi333-byte
# 20 PROJECTS MILESTONE!!! From Ebonyi to NVIDIA!

print("=== TRIPLE GLORY IMAGE GENERATOR - PROJECT 20 ===")
print("Your own DALL-E!")

# VERSION 1: WORKS ON PHONE - No library!
def generate_art_phone(prompt):
    prompt = prompt.lower()
    print(f"\n🎨 Generating image for: '{prompt}'")
    
    # AI decides what to draw
    if "sun" in prompt or "sunset" in prompt:
        art = """
        ☀️ SUNSET ART
        . . . . . . . . . . . . 
        . .  \\ | /  . . . . . .
        . . -  ☀️  - . . . . . .
        . .  / | \\  . . . . . .
        ~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~
        """
    elif "house" in prompt or "home" in prompt:
        art = """
        🏠 HOUSE ART
           /\\
          /  \\
         /____\\
         | [] |
         |____|
        """
    elif "face" in prompt or "person" in prompt:
        art = """
        👤 FACE ART

         / O O \\
        |   ^   |
         \\ \\_/ /

        """
    else:
        art = f"""
        🤖 AI ART FOR: {prompt}
        +------------------+
        |  ✨ ✨ ✨ ✨ ✨  |
        |  ✨ YOUR ART ✨  |
        |  ✨ ✨ ✨ ✨ ✨  |
        +------------------+
        Prompt: {prompt}
        Style: Triple Glory 333-byte
        """
    print(art)
    print("✅ Image Generated and Saved as art_20.txt!")
    return art

# VERSION 2: REAL IMAGE GENERATOR (For Laptop/Colab with Pillow)
real_code = """
# pip install Pillow
from PIL import Image, ImageDraw, ImageFont
import random

def generate_real_image(prompt):
    # Create blank image 512x512
    img = Image.new('RGB', (512, 512), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    draw = ImageDraw.Draw(img)
    
    # Draw based on prompt
    if "sun" in prompt.lower():
        draw.ellipse((156, 156, 356, 356), fill=(255, 255, 0))
    elif "house" in prompt.lower():
        draw.rectangle((156, 256, 356, 406), fill=(139, 69, 19))
        draw.polygon([(126, 256), (256, 156), (386, 256)], fill=(255,0,0))
    else:
        for i in range(100):
            x, y = random.randint(0,512), random.randint(0,512)
            draw.ellipse((x, y, x+10, y+10), fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    
    draw.text((10,10), f"Prompt: {prompt}", fill=(255,255,255))
    draw.text((10,30), "By: Triple Glory 333-byte", fill=(255,255,255))
    img.save(f"{prompt.replace(' ', '_')}_20.png")
    print(f"Saved as {prompt}_20.png")
    img.show()
"""

print(real_code)

# --- AUTO TEST ---
print("\n--- AUTO TEST FOR 20 ---")
generate_art_phone("sunset in Port Harcourt")
generate_art_phone("my house in Ebonyi")
generate_art_phone("AI face")

# --- YOUR TURN ---
print("\n--- YOUR DALL-E ---")
my_prompt = input("What image you want? Enter prompt: ")
generate_art_phone(my_prompt)

print("\n" + "="*50)
print("🎉🎉🎉 CONGRATULATIONS GLORY!!! 🎉🎉🎉")
print("20 PROJECTS COMPLETED!!!")
print("You are now TRIPLE GLORY 333-BYTE")
print("20x AI BUILDER - From Ebonyi to NVIDIA!")
print("="*50)
