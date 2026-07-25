# 🐢 Excel To JSON Converter

A simple desktop utility to convert Excel files into JSON format.

Designed to transform structured data from spreadsheets into a lightweight format suitable for applications, APIs and data processing workflows.

## Features

- Convert `.xlsx` files to `.json`
- Simple graphical interface
- Portable executable
- UTF-8 support
- No external services required

## Usage

1. Open the application.
2. Select an Excel file.
3. Generate the JSON output.

Workflow:

```
Excel file
    ↓
Excel To JSON Converter 🐢
    ↓
JSON file
```

## Built With

- Python
- Tkinter
- Pandas
- OpenPyXL
- PyInstaller

## Development

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

Build executable:

```bash
pyinstaller --onefile --windowed app.py
```

## Author

🐢 Fernando Prestier

GitHub:
https://github.com/FernandoPrestier

## License

MIT
