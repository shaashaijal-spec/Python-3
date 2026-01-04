import qrcode  # type: ignore
from qrcode.image.styledpil import StyledPilImage  # type: ignore
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer  # type: ignore
from qrcode.image.styles.colormasks import RadialGradiantColorMask  # type: ignore

# 1. Setup the QR Code with high error correction (good for logos/styling)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# 2. Add your data (e.g., link to your restaurant menu)
qr.add_data('https://www.example.com/shawarma-burgerlak-menu')
qr.make(fit=True)

# 3. Generate the image with specific styles
# - StyledPilImage: Enables the use of drawers and masks
# - RoundedModuleDrawer: Makes the blocks round instead of square
# - RadialGradiantColorMask: Adds a color gradient from the center
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=RadialGradiantColorMask(
        back_color=(255, 255, 255), # White background
        center_color=(255, 0, 0),   # Red center (Start color)
        edge_color=(0, 0, 255)      # Blue edge (End color)
    )
)

# 4. Save the file
img.save("fancy_menu_qr.png")
print("Styled QR code saved as 'fancy_menu_qr.png'")
