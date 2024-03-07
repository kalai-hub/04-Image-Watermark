# Import the necessary libraries from Pillow
from PIL import Image, ImageDraw, ImageFont

image_list = ['image-file-names-list']

for image_item in image_list:

    # Load the image and font
    image = Image.open(f"images/{image_item}")
    font = ImageFont.truetype('arial.ttf', 36)

    # Specify the text to draw, along with the position
    watermark_text = 'kalaipythontest@gmail.com'
    text_position = (100, 100)

    # Specify the transparency level for the watermark
    watermark_transparency = 128  # Ranges from 0 to 255

    # Prepare the watermark text
    watermark = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark)
    draw.text(text_position, watermark_text, font=font, fill=(255, 255, 255, watermark_transparency))

    # Merge the watermark with the image
    watermarked_image = Image.alpha_composite(image.convert('RGBA'), watermark)

    # Save the image
    watermarked_image.save(f'watermarked-image-png/{image_item.split(".")[0]}.png', 'PNG')

    # Convert PNG to JPEG
    im = Image.open(f'watermarked-image-png/{image_item.split(".")[0]}.png')
    rgb_im = im.convert('RGB')
    rgb_im.save(f'watermarked-image-jpg/{image_item.split(".")[0]}.jpg')