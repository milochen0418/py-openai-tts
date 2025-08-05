import reflex as rx
from text_to_speech_ui_project.states.state import TextToSpeechState
from text_to_speech_ui_project.components.audio_card import audio_card


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "bot",
                        size=32,
                        class_name="text-blue-500",
                    ),
                    class_name="p-3 bg-blue-100 rounded-full border-4 border-blue-200",
                ),
                rx.el.h1(
                    "OpenAI Text-to-Speech",
                    class_name="text-4xl font-bold text-gray-800",
                ),
                rx.el.p(
                    "Convert your text into lifelike speech with a single click.",
                    class_name="text-gray-500 text-lg",
                ),
                class_name="flex flex-col items-center text-center gap-4 mb-8",
            ),
            rx.el.div(
                rx.el.form(
                    rx.el.textarea(
                        name="text_input",
                        placeholder="Enter the text you want to convert to speech...",
                        class_name="w-full p-4 border border-gray-300 rounded-xl mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent min-h-[150px] resize-y shadow-sm",
                    ),
                    rx.el.button(
                        rx.cond(
                            TextToSpeechState.is_processing,
                            rx.spinner(class_name="mr-2"),
                            rx.icon(
                                "sparkles",
                                class_name="mr-2 h-5 w-5",
                            ),
                        ),
                        rx.cond(
                            TextToSpeechState.is_processing,
                            "Converting...",
                            "Convert to Speech",
                        ),
                        type="submit",
                        disabled=TextToSpeechState.is_processing,
                        class_name="w-full flex items-center justify-center bg-blue-500 text-white py-3 px-6 rounded-xl hover:bg-blue-600 transition-all duration-300 font-bold text-lg disabled:bg-blue-300 disabled:cursor-not-allowed shadow-lg hover:shadow-blue-500/30",
                    ),
                    on_submit=TextToSpeechState.convert_to_speech,
                    reset_on_submit=True,
                    class_name="w-full",
                ),
                rx.el.p(
                    TextToSpeechState.status,
                    class_name=rx.cond(
                        TextToSpeechState.status.contains(
                            "Error"
                        ),
                        "text-center mt-4 text-red-600 font-medium",
                        "text-center mt-4 text-gray-600",
                    ),
                ),
                class_name="w-full max-w-2xl mx-auto p-8 bg-white rounded-2xl shadow-md border border-gray-100",
            ),
            rx.el.div(
                rx.el.h2(
                    "Generated Audio Files",
                    class_name="text-2xl font-bold text-gray-700 mb-6 text-center",
                ),
                rx.cond(
                    TextToSpeechState.files.length() > 0,
                    rx.el.div(
                        rx.foreach(
                            TextToSpeechState.files,
                            audio_card,
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
                    ),
                    rx.el.div(
                        rx.icon(
                            "file-audio",
                            class_name="mx-auto h-12 w-12 text-gray-400",
                        ),
                        rx.el.p(
                            "No audio files yet.",
                            class_name="mt-2 text-sm text-gray-500",
                        ),
                        class_name="text-center p-10 border-2 border-dashed border-gray-300 rounded-2xl",
                    ),
                ),
                class_name="w-full max-w-7xl mx-auto mt-12",
            ),
            class_name="container mx-auto px-4 py-10",
        ),
        class_name="min-h-screen bg-gray-50 font-['Inter']",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(
            rel="preconnect",
            href="https://fonts.googleapis.com",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            crossorigin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)