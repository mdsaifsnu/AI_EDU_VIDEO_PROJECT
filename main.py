from modules.text_input import get_text
from modules.language_detect import detect_language
from modules.script_splitter import split_script
from modules.voice_generator import generate_voice
from modules.image_creator import create_image
from modules.video_creator import create_video

def main():

    text = get_text()

    print("\nDetecting language...")

    lang = detect_language(text)

    print("Language:", lang)

    sentences = split_script(text)

    images = []
    audios = []

    for i,s in enumerate(sentences):

        print("Processing:", s)

        img = create_image(s,f"scene{i}")
        audio = generate_voice(s,f"voice{i}",lang)

        images.append(img)
        audios.append(audio)

    create_video(images,audios)

    print("\nVideo created in assets/output/")

if __name__ == "__main__":
    main()