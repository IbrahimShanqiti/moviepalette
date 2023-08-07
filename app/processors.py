from PIL import Image
import cv2

def average_color_of_frame(image_1: Image) -> tuple:
    r, g, b = 0, 0, 0
    sizes = image_1.size 
    pixels = sizes[0] * sizes[1]
    for i in range(sizes[0] - 1):
        for j in range(sizes[1] - 1):
            r1, g1, b1 = image_1.getpixel((i, j))
            r, g, b = r + r1 ** 2, g + g1 ** 2, b + b1 ** 2
    r, g, b = int((r // pixels) ** (1/2)), int((g // pixels) ** (1/2)), int((b // pixels) ** (1/2))
    return (r, g, b)


def build_palette(video: str, width: int) -> None:
    vidcap = cv2.VideoCapture(video)
    length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    num_frames = length // width
    image1 = vidcap.read()[1]
    img = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(img)
    colors = []
    count = 0
    
    for i in range(0, length - 1):
        if i % num_frames == 0:
            print(i)
            colors.append(average_color_of_frame(image))         
            count += 1
        image_new = vidcap.read()[1]
        img1 = cv2.cvtColor(image_new, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(img1)

    image_final = Image.new('RGB', (width, width))

    for i in range(0, width):
        for j in range(0, width):
            image_final.putpixel((i, j), colors[i])
    
    image_final.save('static/final.png')