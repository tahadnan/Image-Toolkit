# Image Toolkit 🖼️

A powerful command-line tool for common image operations, built with Python. Supports batch processing, format conversion, and image resizing while maintaining quality.

## Features

- **Format Conversion**: Convert images between multiple formats (PNG, JPEG, GIF, WEBP, etc.)
- **Image Downsizing**: Downsize images with optional aspect ratio preservation
- **Information Display**: View detailed image metadata and properties
- **Dual Interface**:
  - Interactive CLI with guided prompts
  - Command-line arguments for scripting and automation

## Supported Formats

- PNG (with APNG support)
- JPEG/JPG
- GIF
- WEBP
- TIFF
- BMP
- And many more...

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tahadnan/Image-Toolkit.git
cd image-toolkit
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode

Launch the interactive interface with guided prompts:

```bash
python main.py -i
```

Available commands in interactive mode:
- `convert`: Transform image format
- `downsize`: downsize image dimensions
- `info`: View image details
- `help`: Display help message
- `clear`: Clear screen
- `exit`: Close program

### Command Line Mode

#### Convert Image Format
```bash
python main.py convert input_image.jpg png
```

#### downsize Image
```bash
# Preserve aspect ratio
python main.py downsize input_image.jpg 800x600

# Force exact dimensions
python main.py downsize input_image.jpg 800x600 -f
```

## Examples

1. Convert PNG to JPEG:
```bash
python main.py convert image.png jpg
```

2. downsize image to 1920x1080 (maintaining aspect ratio):
```bash
python main.py downsize image.jpg 1920x1080
```

3. Get image information :
```bash
python main.py image.gif
```

## Command Line Arguments

```
usage: image-toolkit [-h] [-i] {info,convert,downsize} ...

options:
  -h, --help         show this help message and exit
  -i, --interactive  Launch interactive mode with guided prompts

available commands:
  valid operations

  {info,convert,downsize}   
    info            Displays the given image info
    convert         Convert image from one format to another
    downsize        Downsize image to specified dimensions
```

## Dependencies

- Pillow (PIL Fork) - Image processing
- prompt_toolkit - Interactive CLI interface
- wcwidth - Terminal width calculations

## Error Handling

The toolkit includes comprehensive error handling for:
- Invalid file paths
- Unsupported formats
- Invalid dimensions
- File permission issues

## Status Indicators

The program uses the following status indicators in CLI:
- `[+]` Success messages
- `[-]` Error/warning messages
- `[*]` Information display
- `[>]` Operations/actions
- `[?]` Help/questions
- `[i]` Informational content

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

Licensed under the MIT license

