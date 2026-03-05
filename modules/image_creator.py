from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def create_image(text, filename):

    width = 1280
    height = 720

    img = Image.new("RGB", (width, height), color=(20, 40, 80))
    draw = ImageDraw.Draw(img)

    # Try loading a better font
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()

    # Wrap text
    wrapped_text = textwrap.fill(text, width=28)

    bbox = draw.multiline_textbbox((0,0), wrapped_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (width - text_width) / 2
    y = (height - text_height) / 2

    draw.multiline_text(
        (x,y),
        wrapped_text,
        font=font,
        fill=(255,255,255),
        align="center"
    )

    os.makedirs("assets/images", exist_ok=True)

    path = f"assets/images/{filename}.png"

    img.save(path)

    return path