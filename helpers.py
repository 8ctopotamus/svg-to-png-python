import os
from wand.color import Color
from wand.image import Image

# Utility function to swap the file extension to .png
def swap_file_ext(filepath: str, newExt: str) -> str:
    splitpath = filepath.split('.')
    splitpath.pop(len(splitpath) - 1)  # Remove the old extension
    return '.'.join(splitpath) + '.' + newExt

# Convert a single SVG file to PNG and save it in the output directory
def convert_svg_to_png(filepath: str, outputdir: str) -> str:
    # Ensure the output directory exists
    os.makedirs(outputdir, exist_ok=True)

    # Get the filename without directory
    filename = os.path.basename(filepath)
    
    # Update the file path with the output directory and .png extension
    updatedFilepath = os.path.join(outputdir, swap_file_ext(filename, "png"))
    
    # Convert SVG to PNG using ImageMagick (via Wand)
    with Image(filename=filepath, background=Color("transparent"), resolution=144) as img:
        img.format = 'png'
        img.save(filename=updatedFilepath)  # Save the image as PNG
    
    return updatedFilepath

# Convert multiple SVG files to PNGs and save them to the output directory
def convert_svgs_to_pngs(filepaths: list[str], outputdir: str) -> list[str]:
    pngpaths = []
    for filepath in filepaths:
        # Convert each SVG file and append the new PNG file path
        pngpath = convert_svg_to_png(filepath, outputdir)
        pngpaths.append(pngpath)
    return pngpaths

# Fetch file paths with a specific extension (e.g., .svg) in a directory
def get_filepaths_by_extension(dir: str, ext: str) -> list[str]:
    filepaths = []
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if file.lower().endswith(ext):  # Case-insensitive match for extension
                filepaths.append(os.path.join(subdir, file))
    return filepaths
