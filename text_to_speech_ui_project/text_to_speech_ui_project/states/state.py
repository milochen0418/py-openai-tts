import reflex as rx
import os
import datetime
from typing import TypedDict
from openai import OpenAI


from dotenv import load_dotenv
load_dotenv()  # for loading environment variables from .env file

class AudioFile(TypedDict):
    filename: str
    text: str
    timestamp: str


class TextToSpeechState(rx.State):
    files: list[AudioFile] = []
    status: str = (
        "Enter text and click convert to generate audio."
    )
    is_processing: bool = False

    @rx.event(background=True)
    async def convert_to_speech(self, form_data: dict):
        text_input = form_data.get("text_input", "").strip()
        if not text_input:
            async with self:
                self.status = (
                    "Error: Text input cannot be empty."
                )
            return
        async with self:
            self.is_processing = True
            self.status = "Converting text to speech..."
            yield
        try:
            client = OpenAI(
                api_key=os.getenv("OPENAI_API_KEY")
            )
            timestamp = datetime.datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )
            filename = f"speech_{timestamp}.mp3"
            outfile_path = rx.get_upload_dir() / filename
            response = client.audio.speech.create(
                model="tts-1",
                voice="alloy",
                input=text_input,
            )
            response.stream_to_file(outfile_path)
            async with self:
                new_file = {
                    "filename": filename,
                    "text": text_input,
                    "timestamp": datetime.datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                }
                self.files.insert(0, new_file)
                self.status = "Conversion successful!"
                self.is_processing = False
        except Exception as e:
            async with self:
                self.status = f"Error: {str(e)}"
                self.is_processing = False

    @rx.event
    def delete_file(self, filename: str):
        try:
            file_path = rx.get_upload_dir() / filename
            if file_path.exists():
                file_path.unlink()
            self.files = [
                f
                for f in self.files
                if f["filename"] != filename
            ]
        except Exception as e:
            self.status = f"Error deleting file: {str(e)}"