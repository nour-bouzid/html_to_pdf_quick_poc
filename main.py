import os
import pdfkit
from jinja2 import Environment, FileSystemLoader

# Setup pdfkit
path_to_wkhtmltopdf = "/usr/local/bin/wkhtmltopdf"
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# Setup Jinja2
env = Environment(loader=FileSystemLoader("."))  # or specify your templates folder
template = env.get_template("templates/sample.html")


# Preprocess image paths to absolute paths
def make_file_url(path):
    abs_path = os.path.abspath(path)
    return f"file://{abs_path}"


gallery_images = [
    make_file_url(img)
    for img in [
        "images/img1.png",
        "images/img2.png",
        "images/img3.png",
        "images/img4.png",
    ]
]

section_image = make_file_url("images/img1.png")

data = {
    "company_name": "Awesome Company",
    "details": "We make dreams come true!",
    "toc": ["Company Overview", "Gallery", "Our Services", "Contact Information"],
    "gallery_images": gallery_images,
    "section_image": section_image,
    "section_text": "We specialize in delivering exceptional service and outstanding products to all our customers.",
    "quick_links": ["Home", "About", "Services", "Contact"],
    "isic_codes": [
        ["001", "Agriculture"],
        ["002", "Fishing"],
        ["003", "Mining"],
    ],
    "table1": [
        ["Product", "Price"],
        ["Laptop", "$999"],
        ["Phone", "$499"],
        ["Tablet", "$299"],
    ],
    "table2": [
        ["Employee", "Position"],
        ["Alice", "Manager"],
        ["Bob", "Developer"],
        ["Charlie", "Designer"],
    ],
}

# Render HTML
html_out = template.render(data)

# Generate PDF
pdfkit.from_string(
    html_out,
    output_path="sample.pdf",
    configuration=config,
    options={
        "page-size": "A4",
        "orientation": "Landscape",
        "enable-local-file-access": "",  # <<< Important!
    },
)
