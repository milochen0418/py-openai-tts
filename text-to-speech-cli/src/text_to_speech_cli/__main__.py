# src/text_to_speech_cli/__main__.py

from .converter import text_to_speech

AVAILABLE_VOICES = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Convert .txt to .mp3 using OpenAI TTS API")
    parser.add_argument("input_txt", help="Path to input .txt file")
    parser.add_argument("output_mp3", help="Path to output .mp3 file")
    parser.add_argument(
        "--voice",
        default="nova",
        help=(
            "Voice style to use (default: nova). "
            f"Available voices: {', '.join(AVAILABLE_VOICES)}"
        )
    )
    parser.add_argument(
        "--quality",
        choices=["standard", "hd"],
        default="standard",
        help="Audio quality model: 'standard' = tts-1, 'hd' = tts-1-hd"
    )
    
    args = parser.parse_args()

    # Call the text_to_speech function with parsed arguments
    if not args.input_txt.endswith('.txt'):
        raise ValueError("Input file must be a .txt file")
    if not args.output_mp3.endswith('.mp3'):
        raise ValueError("Output file must be a .mp3 file")
    if args.voice not in ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]:
        raise ValueError(f"Invalid voice: '{args.voice}'. Must be one of ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']")
    if args.quality not in ["standard", "hd"]:
        raise ValueError(f"Invalid quality: '{args.quality}'. Must be 'standard' or 'hd'")
    # Call the text_to_speech function
    text_to_speech(
        input_txt_path=args.input_txt,
        output_mp3_path=args.output_mp3,
        voice=args.voice,
        quality=args.quality
    )
if __name__ == "__main__":
    main()
