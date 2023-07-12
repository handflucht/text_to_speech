# Text-to-Speech Converter

This is a simple Python script that converts text to speech using the Google Text-to-Speech API.

## Usage

To use this script, run the following command in your terminal:
```bash
python main.py "Hallo Welt!"
```

This will generate an MP3 file with the text "Hello, world!" spoken in the default language (German). You can specify a different language using the `--language` option, and you can specify a filename using the `--file` option.

## Dependencies

This script requires the following Python packages:

- `argparse`
- `datetime`
- `gtts`

You can install these packages using `pip`. For example:
```bash
pip install -r requirements.txt
```