import openai
import os
from dotenv import load_dotenv

# 載入 .env 檔案中的 OPENAI_API_KEY
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 支援的語音樣式
VALID_VOICES = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]

def text_to_speech(input_txt_path: str, output_mp3_path: str, voice: str = "nova") -> None:
    """
    將文字檔轉換為語音 MP3

    :param input_txt_path: 要轉換的 .txt 檔案路徑
    :param output_mp3_path: 輸出的 .mp3 檔案路徑
    :param voice: 使用的語音樣式（預設：nova）
    """
    if voice not in VALID_VOICES:
        raise ValueError(f"Invalid voice: '{voice}'. Must be one of {VALID_VOICES}")

    # 讀取文字檔內容
    try:
        with open(input_txt_path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        raise RuntimeError(f"Failed to read input file: {e}")

    if not text.strip():
        raise ValueError("Input text file is empty.")

    # 呼叫 OpenAI 的 TTS API
    try:
        response = openai.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text,
        )
    except Exception as e:
        raise RuntimeError(f"OpenAI TTS request failed: {e}")

    # 將回傳的 MP3 存檔
    try:
        with open(output_mp3_path, "wb") as out_file:
            out_file.write(response.content)
    except Exception as e:
        raise RuntimeError(f"Failed to write output file: {e}")

    print(f"✅ 成功轉換！MP3 已儲存於：{output_mp3_path}")
