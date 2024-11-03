from typing import Final, List, Dict, Tuple, Any
from PIL import Image
from os import PathLike

ImagePath: TypeAlias = PathLike[str]
ImageDimensions: TypeAlias = Tuple[int, int]
ImageInfo: TypeAlias = Dict[str, Any]

SUPPORTED_IMAGE_TYPES: Final[List[str]] = ['blp', 'bmp', 'dib', 'bufr', 'cur', 'pcx', 'dcx', 'dds', 'ps', 'eps', 'fit', 'fits', 'fli', 'flc', 'ftc', 'ftu', 'gbr', 'gif', 'grib', 'h5', 'hdf', 'png', 'apng', 'jp2', 'j2k', 'jpc', 'jpf', 'jpx', 'j2c', 'icns', 'ico', 'im', 'iim', 'jfif', 'jpe', 'jpg', 'jpeg', 'mpg', 'mpeg', 'tif', 'tiff', 'mpo', 'msp', 'palm', 'pcd', 'pdf', 'pxr', 'pbm', 'pgm', 'ppm', 'pnm', 'pfm', 'psd', 'qoi', 'bw', 'rgb', 'rgba', 'sgi', 'ras', 'tga', 'icb', 'vda', 'vst', 'webp', 'wmf', 'emf', 'xbm', 'xpm']
SUPPORTED_IMAGE_TYPES_EXT : Final[List[str]] =  list(Image.registered_extensions().keys())

SUPPORTED_IMAGE_TYPES_DICT: Final[Dict[str, str]] = {
    'apng': 'PNG',
    'blp': 'BLP',
    'bmp': 'BMP',
    'bufr': 'BUFR',
    'bw': 'SGI',
    'cur': 'CUR',
    'dcx': 'DCX',
    'dds': 'DDS',
    'dib': 'DIB',
    'emf': 'WMF',
    'eps': 'EPS',
    'fit': 'FITS',
    'fits': 'FITS',
    'flc': 'FLI',
    'fli': 'FLI',
    'ftc': 'FTEX',
    'ftu': 'FTEX',
    'gbr': 'GBR',
    'gif': 'GIF',
    'grib': 'GRIB',
    'h5': 'HDF5',
    'hdf': 'HDF5',
    'icb': 'TGA',
    'icns': 'ICNS',
    'ico': 'ICO',
    'iim': 'IPTC',
    'im': 'IM',
    'j2c': 'JPEG2000',
    'j2k': 'JPEG2000',
    'jfif': 'JPEG',
    'jp2': 'JPEG2000',
    'jpc': 'JPEG2000',
    'jpe': 'JPEG',
    'jpeg': 'JPEG',
    'jpf': 'JPEG2000',
    'jpg': 'JPEG',
    'jpx': 'JPEG2000',
    'mpeg': 'MPEG',
    'mpg': 'MPEG',
    'mpo': 'MPO',
    'msp': 'MSP',
    'palm': 'PALM',
    'pbm': 'PPM',
    'pcd': 'PCD',
    'pcx': 'PCX',
    'pdf': 'PDF',
    'pfm': 'PPM',
    'pgm': 'PPM',
    'png': 'PNG',
    'pnm': 'PPM',
    'ppm': 'PPM',
    'ps': 'EPS',
    'psd': 'PSD',
    'pxr': 'PIXAR',
    'qoi': 'QOI',
    'ras': 'SUN',
    'rgb': 'SGI',
    'rgba': 'SGI',
    'sgi': 'SGI',
    'tga': 'TGA',
    'tif': 'TIFF',
    'tiff': 'TIFF',
    'vda': 'TGA',
    'vst': 'TGA',
    'webp': 'WEBP',
    'wmf': 'WMF',
    'xbm': 'XBM',
    'xpm': 'XPM'}

if __name__ == "__main__":
    print(SUPPORTED_IMAGE_TYPES)

