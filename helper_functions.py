import PIL
from PIL.Image import Image 
from pathlib import Path, PurePath
from typing import Union, Tuple, Optional, Dict, Any, Literal
from constants import SUPPORTED_IMAGE_TYPES, SUPPORTED_IMAGE_TYPES_EXT, SUPPORTED_IMAGE_TYPES_DICT
from pprint import pprint
from collections import OrderedDict
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import confirm
import re

def get_PIL_formats(format: str) -> Optional[str]:
    clean_format = format.lower().lstrip('.')
    return SUPPORTED_IMAGE_TYPES_DICT.get(clean_format, None)

def open_image(image: Union[str, Path]) -> Tuple[Image, str, Path, str]:
    image_path = Path(image)

    if not image_path.exists():
        raise FileNotFoundError(f"Unable to locate image at: {image_path}")
    if not image_path.is_file():
        raise ValueError(f"The specified path does not point to a file: {image_path}")

    if image_path.suffix not in SUPPORTED_IMAGE_TYPES_EXT:
        raise ValueError(f"Unsupported file format '{image_path.suffix}' for image: {image_path}")

    return (PIL.Image.open(image_path), image_path.stem, image_path.parent, image_path.suffix.replace(".", ""))

def get_image_info_quiet(image: Union[str, Path]) -> Dict[str, Any]:
    image, name, image_path, _ = open_image(image)
    Info = {
        "File Name": name,
        "Location": str(image_path.resolve()),
        "Format": image.format,
        "Dimensions": f"{image.size[0]}x{image.size[1]} pixels",
        "Color Mode": image.mode
    }
    return Info

def get_image_info(image: Union[str, Path]) -> None:
    Info = get_image_info_quiet(image)
    print("\n[*] Image Details [*]")
    print("─" * 40)
    for key, value in Info.items():
        print(f"• {key}: {value}")
    print("─" * 40 + "\n")

def convert_image(image: Union[str, Path], target_format: str) -> Optional[str]:
    image, name, image_path, _ = open_image(image)
    clean_format = target_format.lower().lstrip('.')

    if clean_format not in SUPPORTED_IMAGE_TYPES:
        return f"Cannot convert to {target_format} - format not supported. Please check the list of supported formats."
    
    pil_format = get_PIL_formats(clean_format)
    if not pil_format:
        return f"Unable to process {target_format} - internal format mapping not found."
    
    saved_as = image_path / f"{name}_{target_format.upper()}.{target_format}"
    if pil_format == 'JPEG' and image.mode in ('RGBA', 'LA', 'P'):
        image = image.convert("RGB")
    
    image.save(saved_as, format=get_PIL_formats(target_format))
    print("[+] Image converted successfully!")
    get_image_info(saved_as)

def downsize_image(
    image: Union[str, Path], 
    new_size: Tuple[int, int], 
    keep_aspect_ratio: bool = True
) -> None:

    image, name, image_path, ext = open_image(image)
    downsized_image = image.copy()
    og_size = image.size
    requested_size = new_size
    
    if keep_aspect_ratio:
        downsized_image.thumbnail(new_size)
        final_size = downsized_image.size
        print(f"[>] Resized with aspect ratio preserved:")
        print(f"   • Requested size: {requested_size[0]}x{requested_size[1]} pixels")
        print(f"   • Actual size:    {final_size[0]}x{final_size[1]} pixels")
        print(f"   • Original size:  {og_size[0]}x{og_size[1]} pixels")
    else:
        downsized_image = downsized_image.resize(new_size)
        final_size = downsized_image.size
        print(f"[>] Resized to exact dimensions: {new_size[0]}x{new_size[1]} pixels")

    size_str = f"{final_size[0]}x{final_size[1]}"
    saved_as = image_path / f"{name}_resized_{size_str}.{ext}"

    downsized_image.save(saved_as)
    print("[+] Image resized successfully!")
    get_image_info(saved_as)

def parse_dimensions(dimension_string: str) -> Tuple[Tuple[int, int], bool]:
    dimension_string = dimension_string.strip().lower()   
    pattern = r'^\s*(\d+)\s*[x×]\s*(\d+)\s*$'
    
    match = re.match(pattern, dimension_string)
    if not match:
        raise ValueError(
            "Please enter dimensions in WxH format (e.g., '800x600' or '1920x1080')"
        )
    
    try:
        width = int(match.group(1))
        height = int(match.group(2))
        
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers")

        return (width, height)
        
    except ValueError as e:
        raise ValueError("Please enter valid positive numbers for width and height in WxH format")

def verify_path(fp: Union[str, Path]) -> bool:
    file_path = Path(fp)
    if file_path.exists() and not file_path.is_dir():
        return True
    return False

def verify_extension(ext: str, prompt: bool = False) -> bool:
    clean_ext = ext.lower().lstrip('.')
    if prompt:     
        return ext in SUPPORTED_IMAGE_TYPES
    return f'.{clean_ext}' in SUPPORTED_IMAGE_TYPES_EXT

def prompt_help() -> None:
    print(
        '''
        [?] Image Toolkit Help [?]

        Available Commands:
        1. convert   - Transform image to another format
        2. Downsize  - Downsize image dimensions
        3. info      - View image details
        4. exit      - Close program
        5. help      - Displays this message
        6. clear     - Clear the screen

        Type any command to get started!
        '''
    )

def prompt_convert_image() -> Optional[str]:
    while True:
        input_image = prompt("[>] Enter path to image: ")
        if not verify_path(input_image):
            print("[-] Cannot find image at specified path. Please check and try again.")
            continue
        if not verify_extension(Path(input_image).suffix):
            print("[-] Unsupported image format. Please use a supported file type.")
            continue
        break
    print('''
    [i] Supported Formats:
    • PNG  - High quality with transparency
    • JPEG - Efficient compression for photos
    • GIF  - Animated images and simple graphics
    • BMP  - Uncompressed bitmap format
    • TIFF - High quality for print
    And much more...(Check the repo for more info)
    ''')
    while True:
        output_format = prompt("[>] Enter desired format: ", wrap_lines=True)
        
        if verify_extension(output_format, prompt=True):
            break
        print("[-] Invalid format selected. Please choose from the supported formats.")
    return convert_image(image=input_image, target_format=output_format)

def prompt_downsize_image() -> Optional[None]:
    while True:
        input_image = prompt("[>] Enter path to image: ")
        if not verify_path(input_image):
            print("[-] Cannot find image at specified path. Please check and try again.")
            continue
        if not verify_extension(Path(input_image).suffix):
            print("[-] Unsupported image format. Please use a supported file type.")
            continue
            
        current_size = get_image_info_quiet(input_image).get("Dimensions")
        print(f"[i] Current dimensions: {current_size}")
        
        try:
            new_dimensions = prompt("[>] Enter new dimensions (e.g., 800x600): ")
            dimensions_tuple = parse_dimensions(new_dimensions)
            force_dimension = confirm("[?] Maintain aspect ratio?", suffix=" (y/n) ")
            return downsize_image(image=input_image, new_size=dimensions_tuple, keep_aspect_ratio=force_dimension)
        except ValueError as e:
            print(f"[-] Error: {e}")
            if not confirm("[?] Try again?"):
                return None
            continue

def prompt_info() -> None:
    while True:
        input_image = prompt("[>] Enter path to image: ")
        if not verify_path(input_image):
            print("[-] Cannot find image at specified path. Please check and try again.")
            continue
        if not verify_extension(Path(input_image).suffix):
            print("[-] Unsupported image format. Please use a supported file type.")
            continue
        break
    get_image_info(input_image)

def prompt_exit():
    return confirm("Want to exit?")

if __name__ == "__main__":
    prompt_downsize_image()
