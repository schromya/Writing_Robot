# import mobrob.parse_svg_for_path_following as parsesvg    # This is a program that sorts out SVG files to find their waypoints. 
# path_file_svg = rospy.get_param('/path_file_svg')    # Get the parameter that has the file's full path
# path_specs = parsesvg.convert_svg_to_path_specs(path_file_svg, xlength=1., ylength=1.)    # Parse the SVG file for "d=" lines (paths)


from svgpathtools import svg2paths

# Load SVG and extract paths and attributes
paths, attributes = svg2paths('svg/line.svg')

# Iterate through paths
for path in paths:
    print(path.d())  # Path data as string