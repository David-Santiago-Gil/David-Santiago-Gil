import os
from PIL import Image, ImageDraw, ImageOps, ImageFont

def create_circular_avatar(input_path, output_path, size=300, border_width=12):
    # Open image
    img = Image.open(input_path).convert("RGBA")
    
    # Calculate crop to square (center crop)
    width, height = img.size
    min_dim = min(width, height)
    left = (width - min_dim) / 2
    top = (height - min_dim) / 2
    right = (width + min_dim) / 2
    bottom = (height + min_dim) / 2
    img = img.crop((left, top, right, bottom))
    img = img.resize((size, size), Image.Resampling.LANCZOS)
    
    # Create mask for circular photo
    mask = Image.new("L", (size, size), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((border_width, border_width, size - border_width, size - border_width), fill=255)
    
    # Create circular image
    circular_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    circular_img.paste(img, (0, 0), mask=mask)
    
    # Draw gradient circular border (Cyan to Purple)
    # We can create a glowing circular ring
    border_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw_border = ImageDraw.Draw(border_img)
    
    # Draw multiple concentric circles for a gradient effect
    for i in range(border_width):
        t = i / border_width
        # Interpolate color between cyan (112, 165, 253) and purple (157, 124, 216)
        r = int(112 + (157 - 112) * t)
        g = int(165 + (124 - 165) * t)
        b = int(253 + (216 - 253) * t)
        
        draw_border.ellipse((i, i, size - i, size - i), outline=(r, g, b, 255), width=2)
        
    # Combine circular image over the border
    final_img = Image.alpha_composite(border_img, circular_img)
    final_img.save(output_path, "PNG")
    print(f"Created circular avatar at: {output_path}")

if __name__ == "__main__":
    photo_in = r"c:\Users\davi2\OneDrive\Documentos\hoja de v\perfil Git hub\David-Santiago-Gil\assets\photo.png"
    photo_out = r"c:\Users\davi2\OneDrive\Documentos\hoja de v\perfil Git hub\David-Santiago-Gil\assets\photo_framed.png"
    if os.path.exists(photo_in):
        create_circular_avatar(photo_in, photo_out)
    else:
        print("Input photo not found!")
