import qrcode
from PIL import Image, ImageDraw, ImageFont

def generate_framed_qr(data, filename, logo_path=None, text="SCAN TO VIEW MENU"):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # Get dimensions
    qr_width, qr_height = qr_img.size
    
    # Add logo in center if provided
    if logo_path:
        try:
            logo = Image.open(logo_path)
            # Calculate logo size (max 20% of QR size)
            logo_max_size = qr_width // 5
            logo.thumbnail((logo_max_size, logo_max_size), Image.Resampling.LANCZOS)
            
            # Calculate position
            logo_x = (qr_width - logo.size[0]) // 2
            logo_y = (qr_height - logo.size[1]) // 2
            
            # Paste logo
            qr_img.paste(logo, (logo_x, logo_y))
        except Exception as e:
            print(f"Error adding logo: {e}")
    
    # Create background with frame (padding for text)
    padding = 60
    bg_width = qr_width + 40
    bg_height = qr_height + padding + 40
    
    # Create white canvas
    framed_img = Image.new('RGB', (bg_width, bg_height), 'white')
    draw = ImageDraw.Draw(framed_img)
    
    # Draw a green border/frame
    border_color = "#4CAF50"
    draw.rectangle([10, 10, bg_width-10, bg_height-10], outline=border_color, width=5)
    
    # Paste QR code
    framed_img.paste(qr_img, (20, 20))
    
    # Add text at bottom
    try:
        # Try to find a font, fallback to default
        font = ImageFont.load_default()
        # If possible, use a bigger font size if we had a specific ttf, 
        # but for simplicity in this environment we'll use default or basic
    except:
        font = ImageFont.load_default()
        
    # Calculate text position (centered)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = (bg_width - text_width) // 2
    text_y = qr_height + 30
    
    draw.text((text_x, text_y), text, fill="black", font=font)
    
    # Save the result
    framed_img.save(filename)

if __name__ == "__main__":
    menu_url = "https://f2c2fde9-590d-4849-a746-8a97898ac57b-00-2kypipbtj6yaw.sisko.replit.dev/"
    generate_framed_qr(menu_url, "menu_qr_framed.png", logo_path="restaurant_logo.png")
    print("Framed QR code with logo generated: menu_qr_framed.png")
