from typing import Final, List
from PIL import Image

SUPPORTED_IMAGE_TYPES: Final[List[str]] = ['blp', 'bmp', 'dib', 'bufr', 'cur', 'pcx', 'dcx', 'dds', 'ps', 'eps', 'fit', 'fits', 'fli', 'flc', 'ftc', 'ftu', 'gbr', 'gif', 'grib', 'h5', 'hdf', 'png', 'apng', 'jp2', 'j2k', 'jpc', 'jpf', 'jpx', 'j2c', 'icns', 'ico', 'im', 'iim', 'jfif', 'jpe', 'jpg', 'jpeg', 'mpg', 'mpeg', 'tif', 'tiff', 'mpo', 'msp', 'palm', 'pcd', 'pdf', 'pxr', 'pbm', 'pgm', 'ppm', 'pnm', 'pfm', 'psd', 'qoi', 'bw', 'rgb', 'rgba', 'sgi', 'ras', 'tga', 'icb', 'vda', 'vst', 'webp', 'wmf', 'emf', 'xbm', 'xpm']
SUPPORTED_IMAGE_TYPES_EXT : Final[List[str]] =  list(Image.registered_extensions().keys())
if __name__ == "__main__":
    print(SUPPORTED_IMAGE_TYPES)

