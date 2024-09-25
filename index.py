import sys
import os
from helpers import get_filepaths_by_extension, convert_svgs_to_pngs

def main():
  try:
    rootdir = sys.argv[1] if len(sys.argv) > 1 else "./test-images"
    outputdir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(rootdir, "converted-pngs")

    print(f'Running SVG => PNG conversion in {rootdir}, outputting to {outputdir}')

    svgpaths = get_filepaths_by_extension(rootdir, 'svg')
    pngpaths = convert_svgs_to_pngs(svgpaths, outputdir)

    print('\nAll done. Here are your generated PNG paths:')
    print('\n'.join(pngpaths))

    sys.exit(0)
  except IndexError:
    print("Missing filepath")
    sys.exit(1)

main()
