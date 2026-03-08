import os
import requests

def generate_scene(sentence, filename):
    os.makedirs("assets/images", exist_ok=True)
    img_path = os.path.join("assets", "images", f"{filename}.jpg")
    
    # Extract only the main subject (e.g., "Rose", "Desert", "Cactus")
    keywords = ["rose", "desert", "cactus", "nature", "illustration"]
    found_keywords = [k for k in keywords if k in sentence.lower()]
    search_query = "+".join(found_keywords) if found_keywords else "nature+cinematic"

    # Using a more reliable, themed image source
    url = f"https://loremflickr.com/1920/1080/{search_query}"

    try:
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            with open(img_path, 'wb') as f:
                f.write(r.content)
            return img_path
    except:
        return None