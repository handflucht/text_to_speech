import argparse
from datetime import datetime
from gtts import gTTS

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="the text to convert to audio")
    parser.add_argument("--language", help="the language to use (default: de)", default="de")
    parser.add_argument("--file", help="the filename to save the audio as (default: current timestamp)", default=datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp3")
    return parser.parse_args()

def main():
    args = parse_arguments()

    tts = gTTS(text=args.text, lang=args.language)
    tts.save(args.file)

if __name__ == "__main__":
    main()