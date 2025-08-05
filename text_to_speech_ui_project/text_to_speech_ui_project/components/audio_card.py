import reflex as rx
from text_to_speech_ui_project.states.state import TextToSpeechState


def audio_card(file: dict[str, str]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                f'''"{file['text']}"''',
                class_name="italic text-gray-700 font-medium mb-3",
            ),
            rx.el.p(
                f"Generated on: {file['timestamp']}",
                class_name="text-sm text-gray-500 mb-4",
            ),
            class_name="flex-grow",
        ),
        rx.el.audio(
            src=rx.get_upload_url(file["filename"]),
            controls=True,
            class_name="w-full mb-4",
        ),
        rx.el.div(
            rx.el.a(
                rx.el.button(
                    rx.icon(
                        "download",
                        class_name="mr-2 h-4 w-4",
                    ),
                    "Download",
                    class_name="flex items-center bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 transition-colors duration-200 font-semibold text-sm",
                ),
                href=rx.get_upload_url(file["filename"]),
                download=file["filename"],
            ),
            rx.el.button(
                rx.icon(
                    "trash-2", class_name="mr-2 h-4 w-4"
                ),
                "Delete",
                on_click=lambda: TextToSpeechState.delete_file(
                    file["filename"]
                ),
                class_name="flex items-center bg-red-500 text-white py-2 px-4 rounded-lg hover:bg-red-600 transition-colors duration-200 font-semibold text-sm",
            ),
            class_name="flex justify-end gap-3",
        ),
        class_name="p-6 bg-white rounded-2xl shadow-sm border border-gray-200 flex flex-col",
    )