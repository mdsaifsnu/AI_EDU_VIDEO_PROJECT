from moviepy.editor import *

def create_video(images, audios):

    clips = []

    for img, audio in zip(images, audios):

        audio_clip = AudioFileClip(audio)

        duration = audio_clip.duration

        image_clip = (
            ImageClip(img)
            .set_duration(duration)
            .resize(height=720)
            .set_position("center")
        )

        # add small zoom animation
        image_clip = image_clip.fx(vfx.zoom_in, 1.05)

        video = image_clip.set_audio(audio_clip)

        clips.append(video)

    final = concatenate_videoclips(clips, method="compose")

    final.write_videofile(
        "assets/output/final_video.mp4",
        fps=24,
        codec="libx264"
    )