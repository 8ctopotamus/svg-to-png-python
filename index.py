import sys
from helpers import get_filepaths_by_extension, convert_svgs_to_pngs

def main():
  try:
    rootdir = sys.argv[1] if 1 in range(len(sys.argv)) else "./test-images"
    print('Running SVG => PNG conversion in ' + rootdir)
    
    svgpaths = get_filepaths_by_extension(rootdir, 'svg')
    pngpaths = convert_svgs_to_pngs(svgpaths)

    print('\nAll done. Here are your generated PNG paths:')
    print('\n'.join(pngpaths))

    sys.exit(0)
  except IndexError:
    print ("Missing filepath")
    sys.exit(1)

main()