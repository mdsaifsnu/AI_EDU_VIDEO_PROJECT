import os
import numpy as np
from PIL import Image
from moviepy.editor import VideoClip, AudioFileClip, concatenate_videoclips

def create_video(images, audios):
    clips = []
    screen_w, screen_h = (1280, 720) 

    for img_path, audio_path in zip(images, audios):
        if not img_path or not os.path.exists(img_path):
            continue
        
        audio_clip = AudioFileClip(audio_path)
        duration = audio_clip.duration
        
        # Load and resize to a WIDE 1920x1080 canvas
        pil_img = Image.open(img_path).convert("RGB")
        pil_img = pil_img.resize((1920, 1080), Image.Resampling.LANCZOS)
        img_array = np.array(pil_img)

        def make_frame(t):
            # Slow cinematic pan from left to right
            total_pan = 1920 - screen_w
            x_start = int((t / duration) * total_pan)
            y_start = (1080 - screen_h) // 2
            return img_array[y_start:y_start+screen_h, x_start:x_start+screen_w]

        # Build the cinematic clip
        clip = VideoClip(make_frame, duration=duration).set_fps(24).set_audio(audio_clip)
        
        # Add professional black letterbox bars
        clip = clip.margin(top=60, bottom=60, color=(0,0,0))
        clips.append(clip)

    print("   -> Rendering final cinematic film...")
    final = concatenate_videoclips(clips, method="compose")
    final.write_videofile("assets/output/youtube_film.mp4", fps=24, logger=None)