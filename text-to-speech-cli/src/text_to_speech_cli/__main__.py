# src/text_to_speech_cli/__main__.py

from .converter import text_to_speech

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Convert .txt to .mp3")
    parser.add_argument("input_txt")
    parser.add_argument("output_mp3")
    parser.add_argument("--voice", default="nova")
    args = parser.parse_args()

    text_to_speech(args.input_txt, args.output_mp3, args.voice)

if __name__ == "__main__":
    main()
