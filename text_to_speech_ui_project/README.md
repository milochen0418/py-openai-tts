# Poetry way to run downloaded project from AI builder of reflex 
- poetry init --python ">=3.10,<4.0"
- poetry add $(cat requirements.txt)
- poetry install 
- poetry run reflex init
- poetry run reflex run 


# Setup AI Cursor for this poetry environment 
- Command for get virtual environment managed by poetry 
    - $ poetry env info --path
        - /Users/xxxx/Library/Caches/pypoetry/virtualenvs/text-to-speech-ui-project-F2boMfzV-py3.12
    - $ ls $(poetry env info --path)/bin/python 
        - /Users/xxxx/Library/Caches/pypoetry/virtualenvs/text-to-speech-ui-project-F2boMfzV-py3.12/bin/python    

- Support Go to Definition for Cursor
    - If it is not work, then you can setup project the following way 
    - poetry run bash -c 'mkdir -p .vscode && echo "{\"python.defaultInterpreterPath\": \"$(poetry env info --path)/bin/python\"}" > .vscode/settings.json'

- Run Cursor for project 
    - Install cursor command-line 
        - Cmd + Shift + P -> Open Command Palette
        - Type ```Shell Command: Install 'cursor' command in PATH``` and select it ✅
    - cursor . 
    


