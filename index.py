import sys
from helpers import get_filepaths_by_extension, convert_svgs_to_pngs

def main():
  rootdir = sys.argv[1] if 1 in sys.argv else "./test-images"
  print('Running SVG => PNG conversion in ' + rootdir)
  
  svgpaths = get_filepaths_by_extension(rootdir, 'svg')
  pngpaths = convert_svgs_to_pngs(svgpaths)

  print('All done. PNG paths:')
  print('\n'.join(pngpaths))

main()