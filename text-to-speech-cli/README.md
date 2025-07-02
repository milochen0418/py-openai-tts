# text-to-speech-cli

A simple Python command-line tool that converts `.txt` files into `.mp3` audio using [OpenAI's Text-to-Speech API](https://platform.openai.com/docs/guides/text-to-speech).

## Features

- Convert `.txt` files to `.mp3` using natural AI voices
- CLI-based: easy to automate or integrate into scripts
- Supports multiple voice styles: `alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer`
- Built with [Poetry](https://python-poetry.org/) for reproducible builds
- API key is loaded securely from `.env`

## Installation

### 1. Clone the project

```bash
git clone https://github.com/YOUR_USERNAME/text-to-speech-cli.git
cd text-to-speech-cli
```

### 2. Install dependencies with Poetry

```bash
poetry install
```

### 3. Set your OpenAI API key in `.env`

```bash
echo 'OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' > .env
```

> ⚠️ **Do not commit your `.env` file!**

## Usage

```bash
poetry run text-to-speech-cli input.txt output.mp3
```

Optional: specify a voice

```bash
poetry run text-to-speech-cli input.txt output.mp3 --voice shimmer
```

## Example

**input.txt**
```
Hello, this is a sample voice synthesis from the text-to-speech CLI project.
```

**Command**
```bash
poetry run text-to-speech-cli input.txt hello.mp3
open hello.mp3
```

## Available Voices

| Voice     | Description               |
|-----------|---------------------------|
| alloy     | Warm, clear male voice    |
| echo      | Crisp, bright male        |
| fable     | Storytelling tone         |
| onyx      | Deep, calm male voice     |
| nova      | Natural female voice      |
| shimmer   | Soft, relaxed female tone |

## API Access & Billing

- You must create an API key at [OpenAI API Keys](https://platform.openai.com/account/api-keys)
- Make sure you have active billing or credits on your account

## Project Structure

```
text-to-speech-cli/
├── .env                  # Your OpenAI API key (excluded from Git)
├── README.md
├── pyproject.toml
├── poetry.lock
├── src/
│   └── text_to_speech_cli/
│       ├── __main__.py
│       └── converter.py
├── tests/
│   └── __init__.py
```

## License

MIT License. See [LICENSE](LICENSE) for details.




## Installing Poetry

Poetry is used to manage dependencies and virtual environments for this project.

### macOS & Linux

Run the following command in your terminal:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

After installation, add Poetry to your PATH (if not already):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

You may want to add the line above to your `~/.zshrc` or `~/.bashrc` file.

### Windows

1. Download and run the official installer from:  
   [https://install.python-poetry.org](https://install.python-poetry.org)

2. Restart your terminal, then test Poetry installation:

```powershell
poetry --version
```

More details and troubleshooting tips: [https://python-poetry.org/docs/](https://python-poetry.org/docs/)
