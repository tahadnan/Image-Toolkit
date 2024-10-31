import PIL
from PIL.Image import Image 
from pathlib import Path, PurePath
from typing import Union, Tuple
from constants import SUPPORTED_IMAGE_TYPES, SUPPORTED_IMAGE_TYPES_EXT
from pprint import pprint
from collections import OrderedDict

def open_image(image: Union[str, Path]) -> Tuple[PIL.Image.Image, str, Path] :
    image_path = Path(image)

    if not image_path.exists():
        raise FileNotFoundError(f"Image doesn't exist: {image_path}")
    if not image_path.is_file():
        raise ValueError(f"The given path is not a file: {image_path}")
    if image_path.suffix not in SUPPORTED_IMAGE_TYPES_EXT:
        return f"{image_path} has an invalid extension: '{image_path.suffix}'"

    return (PIL.Image.open(image_path),image_path.stem, image_path.parent, image_path.suffix.replace(".",""))

def get_image_info(image: Union[str, Path]):
    image, name , image_path, _ = open_image(image)
    Info = {
        "Image Name": name,
        "Image Path": str(image_path.resolve()),
        "Image Extension": image.format,
        "Image Size (Width,Height)": image.size,
        "Color Mode": image.mode
    }
    print("\n--- Image Information ---")
    for key, value in Info.items():
        print(f"{key}: {value}")
    print("-------------------------\n")
    return Info

def convert_image(image: Union[str, Path], target_type: str):
    image, name, image_path, _ = open_image(image)
    if target_type.lower() not in SUPPORTED_IMAGE_TYPES:
        return f"{target_type} isn't supported, check supported Image types for more info."
    else:
        saved_as = image_path / f"{name}_{target_type.upper()}.{target_type}"
        image = image.convert("RGB")
        image.save(saved_as, format=target_type)
        print("New image saved successfully:")
        get_image_info(saved_as)

def downsize_image(image: Union[str, Path], new_size : Tuple[int,int], keep_aspect_ratio: bool = True):
    image, name, image_path, ext = open_image(image)
    downsized_image = image.copy()
    saved_as = image_path / f"{name}_TO{str(new_size).replace("(","_").replace(")","").replace(", ","x")}.{ext}"
    if keep_aspect_ratio:
        downsized_image.thumbnail(new_size)
    else:
        downsized_image = downsized_image.resize(new_size)

    downsized_image.save(saved_as)
    get_image_info(saved_as)

if __name__ == "__main__":
    downsize_image("Images/code.png",(2000,2100), keep_aspect_ratio=False)
    # get_image_info("Images/code.png")
