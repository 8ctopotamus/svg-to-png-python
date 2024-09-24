import sys
from helpers import get_filepaths_by_extension, convert_svgs_to_pngs

def main():
    try:
        # Input directory: either from the command-line argument or default to "./test-images"
        rootdir = sys.argv[1] if len(sys.argv) > 1 else "./test-images"
        
        # Output directory: either from the command-line argument or default to "./output-images"
        outputdir = sys.argv[2] if len(sys.argv) > 2 else "./output-images"
        
        print(f'Running SVG => PNG conversion in {rootdir}, outputting to {outputdir}')
        
        # Fetch SVG file paths
        svgpaths = get_filepaths_by_extension(rootdir, 'svg')
        
        # Convert SVGs to PNGs and save them to the output directory
        pngpaths = convert_svgs_to_pngs(svgpaths, outputdir)

        print('\nAll done. Here are your generated PNG paths:')
        print('\n'.join(pngpaths))

        sys.exit(0)
    except IndexError:
        print("Missing filepath")
        sys.exit(1)

main()
