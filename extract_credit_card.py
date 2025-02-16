from PIL import Image, ImageDraw, ImageFont
import os

def a8_credit_card_image():
    """Generate a credit card image at credit_card.png that mimics a real credit card layout"""
    data = get_credit_card(config["email"])

    # Create image with credit card proportions (3.375" x 2.125" at 300 DPI)
    WIDTH, HEIGHT = 1012, 638
    image = Image.new("RGB", (WIDTH, HEIGHT), (25, 68, 141))  # Deep blue background
    draw = ImageDraw.Draw(image)

    # Try to use a more readable font (Arial), fallback to default font if unavailable
    try:
        large_font = ImageFont.truetype("arial.ttf", 60)  # Use Arial font if available
    except IOError:
        large_font = ImageFont.load_default()  # Fallback to default if Arial is not available

    # Format credit card number with spaces
    cc_number = " ".join([data["number"][i: i + 4] for i in range(0, 16, 4)])

    # Position elements on the card
    draw.text((50, 250), cc_number, fill=(255, 255, 255), font=large_font)
    draw.text((50, 400), "VALID\nTHRU", fill=(255, 255, 255))
    draw.text((50, 480), data["expiry"], fill=(255, 255, 255))
    draw.text((250, 480), data["security_code"], fill=(255, 255, 255))
    draw.text((50, 550), data["name"], fill=(255, 255, 255))

    # Save the image to the specified directory
    image.save(os.path.join(config["root"], "credit_card.png"))
