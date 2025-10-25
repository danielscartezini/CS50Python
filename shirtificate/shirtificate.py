from fpdf import FPDF
import requests
from io import BytesIO

def main():
    # 1. Get user input for the name
    name = input("Name: ")

    # 2. Create a new PDF object
    # Orientation: Portrait (default)
    # Unit: mm (default)
    # Format: A4 (default: 210mm wide x 297mm tall)
    pdf = FPDF(format='A4')
    pdf.add_page()

    # Set the font for the header
    pdf.set_font("helvetica", "B", 48)

    # 3. Add the "CS50 Shirtificate" header
    # 0: Auto-calculated height
    # ln=1: Move to the next line after drawing the text
    # align='C': Center the text
    pdf.cell(0, 50, "CS50 Shirtificate", align='C', new_x="LMARGIN", new_y="NEXT")

    # 4. Download and add the shirt image
    # Note: The URL is derived from the prompt's context (shirtificate.png)
    image_url = "https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png"

    # Download the image content using requests
    response = requests.get(image_url, timeout=10)
    response.raise_for_status() # Raise an exception for bad status codes

    # Use BytesIO to load the image from memory instead of saving to a file
    image_data = BytesIO(response.content)

    # Calculate X position to center the image
    # A4 width is 210mm. Image width is 150mm.
    # X = (210 - 150) / 2 = 30mm
    image_x = 30

    # Add the image
    # x: 30 (centered)
    # y: 80 (starting below the header)
    # w: 150 (image width)
    pdf.image(image_data, x=image_x, y=80, w=150)

    # 5. Add the user's name onto the shirt

    # Set the font for the name
    pdf.set_font("helvetica", "B", 24)

    # Set the text color to white (RGB 255, 255, 255)
    pdf.set_text_color(255, 255, 255)

    # Construct the personalized text
    text_on_shirt = f"{name} took CS50"

    # Print the text on top of the shirt image
    # The shirt is centered at X=30, W=150.
    # The center of the shirt is at 30 + (150/2) = 105mm.
    # Set the current position to place the text
    # y=130 places the text roughly in the middle of the shirt graphic
    pdf.set_xy(0, 130)

    # Draw the text, centered across the *entire* page (0 width)
    pdf.cell(0, 10, text_on_shirt, align='C')

    # 6. Output the final PDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
