import os
from wand.color import Color
from wand.image import Image

def swap_filename_ext(filepath, newExt):
  print(vars(filepath.split('.')))

def convert_svg_to_png(filepath):
  updatedFilepath = filepath + '.png' #.split('.svg')
  with Image(filename=filepath, background=Color("transparent")) as img:
    img.format = 'png'
    img.save(filename=updatedFilepath)
  return updatedFilepath 

def convert_svgs_to_pngs(filepaths):
  pngpaths = []
  for filepath in filepaths:
    pngpath = convert_svg_to_png(filepath)
    pngpaths.append(pngpath)
  return pngpaths

def get_filepaths_by_extension(dir, ext):
  svgpaths = []
  for subdir, dirs, files in os.walk(dir):
    for file in files:
      file = file.lower()
      filepath = os.path.join(subdir, file)
      if (filepath.endswith(''+ext)):
        svgpaths.append(filepath)
  return svgpaths