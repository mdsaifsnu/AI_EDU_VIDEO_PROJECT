from modules.drive_fetcher import get_drive_text
from modules.script_splitter import split_script
from modules.voice_generator import generate_voice
from modules.scene_generator import generate_scene
from modules.video_creator import create_video
import os

FOLDER_ID = "1NtrUM6t4J-oVoiTBYHSYReqGP6H3rtjE"

def main():
    print("[1] Connecting to Google Drive...")
    text = get_drive_text(FOLDER_ID)
    
    if text:
        print("[2] Processing Script...")
        sentences = split_script(text)
        
        images = []
        audios = []
        for i, s in enumerate(sentences):
            img = generate_scene(s, f"img_{i}")
            audio = generate_voice(s, f"audio_{i}", "en")
            
            # Robust check: Only add if both files were created successfully
            if img and os.path.exists(img) and audio:
                images.append(img)
                audios.append(audio)
            
        print("[3] Creating Cinematic YouTube Video...")
        if images:
            create_video(images, audios)
            print("Success! Your film is ready in assets/output/.")
        else:
            print("Error: No images were generated. Check your scene_generator.")

if __name__ == "__main__":
    main()