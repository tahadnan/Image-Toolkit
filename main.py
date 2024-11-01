from helper_functions import *
import argparse
import prompt

def main():
    parser = argparse.ArgumentParser(
    prog="image-toolkit",
    description="""
    A powerful toolkit for common image operations including format conversion 
    and resizing. Supports various image formats including PNG, JPEG, WEBP, 
    and many more.
    """.strip(),
    epilog="Example: image-toolkit convert image.png webp | image-toolkit downsize image.jpg 800x600"
    )

    parser.add_argument(
        "-i","--interactive",
        action="store_true",
        help="Launch interactive mode with guided prompts"
    )

    subparsers = parser.add_subparsers(
        dest='command',
        title='available commands',
        description='valid operations'
    )

    convert_parser = subparsers.add_parser(
        'convert',
        help='Convert image from one format to another',
        description='Convert images between different formats while preserving quality'
    )
    convert_parser.add_argument(
        "input_image",
        help="Path to the source image file"
    )
    convert_parser.add_argument(
        "output_format",
        help="Target format to convert to. Supported formats: png, jpg, jpeg, gif and more..."
    )


    downsize_parser = subparsers.add_parser(
        'downsize',
        help='Downsize image to specified dimensions',
        description='Downsize images while optionally preserving aspect ratio'
    )
    downsize_parser.add_argument(
        'input_image',
        help='Path to the source image file'
    )
    downsize_parser.add_argument(
        'dimensions',
        help='Target dimensions in WxH format (e.g., 800x600)'
    )
    downsize_parser.add_argument(
        "-f", "--force-dimensions",
        action="store_true",
        help="Force exact dimensions without preserving aspect ratio"
    )
    args = parser.parse_args()

    if not args.interactive and not args.command:
        parser.error('A command is required unless using interactive mode (-i)')

    if args.interactive:
        prompt.main()
    else:
        if args.command == 'convert':
            convert_image(args.input_image, args.output_format)
        elif args.command == 'downsize':
            dimensions = parse_dimensions(args.dimensions)
            downsize_image(args.input_image, dimensions, not args.force_dimensions)
        else:
            print("Invalid command")
if __name__ == "__main__":
    import sys
    main()
