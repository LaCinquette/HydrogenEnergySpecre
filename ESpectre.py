from PIL import Image, ImageFont, ImageDraw
from wl_to_rgb import *

def createSpectreImage(wavelengths, spectre_range=(100, 1000)): # wavelengths список с числами от 100 до 1000
    if(min(wavelengths) < spectre_range[0] or spectre_range[1] < max(wavelengths)):
        print("Incorrect spectr range")
        return
    
    img = Image.new(mode="RGB", size=(round(spectre_range[1] - spectre_range[0]), 250), color="black")
    pixel_map = img.load()

    flag = -1
    fontpoints = 9
    text_ydelta = float(fontpoints) * 4.0/3.0 - 8.0
    font = ImageFont.truetype("arial.ttf", fontpoints)
    draw = ImageDraw.Draw(img)

    for x in range(0, img.size[0]):
        for y in range(201, 250):
            pixel_map[x, y] = (255, 255, 255)
    
    draw.text((0, 240 - round(text_ydelta)), str(round(spectre_range[0])), (0, 0, 0), font=font)
    draw.text((900 - draw.textlength(str(round(spectre_range[1])), font), 240 - round(text_ydelta)), str(round(spectre_range[1])), (0, 0, 0), font=font)

    for i in wavelengths:
        if(i < 380 or 750 < i):
            for y in range(0, 201):
                pixel_map[round(i - spectre_range[0]), y] = (255, 255, 255)
        else:
            for y in range(0, 201):
                pixel_map[int(i - spectre_range[0]), y] = wavelength_to_rgb(i)

        draw.text((round(i - spectre_range[0]) - round(draw.textlength(str(round(i)), font)/2), round(210.0 + round(text_ydelta)*flag)), str(i), (0, 0, 0), font=font)
        flag = (-1)*flag
    
    img.save("spectre.png", format="png")

if __name__ == '__main__':
    wavelengths = [121.56, 102.57, 97.25, 94.97, 656.426, 486.24, 434.14]
    createSpectreImage(wavelengths, spectre_range=(90, 1000))
        
