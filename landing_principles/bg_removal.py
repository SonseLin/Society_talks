from rembg import remove
from PIL import Image

input_path = 'src/swagga_glasses.jpg'
output_path = 'src/no_bg.jpg'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input_data = i.read()
        output_data = remove(input_data)
        o.write(output_data)
