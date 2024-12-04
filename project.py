# import fitz  # type: ignore # PyMuPDF

# doc = fitz.open("work.pdf")  # Replace with your PDF file path

# # Access the first page (index 0)
# page = doc[0]

# # Extract text
# text = page.get_text()
# print(text)

# for page_num in range(len(doc)):
#     page = doc[page_num]
#     print(f"Page {page_num + 1} Text:")
#     print(page.get_text())

# for page_num in range(len(doc)):
#     page = doc[page_num]
#     images = page.get_images(full=True)  # Get all images

#     for img_index, img in enumerate(images):
#         xref = img[0]  # The image reference number
#         base_image = doc.extract_image(xref)
#         image_bytes = base_image["image"]  # Image data as bytes
#         image_ext = base_image["ext"]  # File extension (e.g., 'png', 'jpeg')

#         # Save the image
#         with open(f"page_{page_num + 1}_image_{img_index + 1}.{image_ext}", "wb") as img_file:
#             img_file.write(image_bytes)

# # page = doc[0]  # Select the first page
# # page.insert_text((72, 72), "Hello, World!", fontsize=12, color=(1, 0, 0))  # Coordinates (x, y)
# # doc.save("output.pdf")


# # page = doc[0]
# # highlights = page.search_for("specific text")

# # for highlight in highlights:
# #     page.add_highlight_annot(highlight)

# # doc.save("highlighted_output.pdf")

# # metadata = doc.metadata
# # print(metadata)

# # new_doc = fitz.open()  # Create a new PDF
# # new_doc.insert_pdf(doc, from_page=0, to_page=2)  # Extract pages 1-3
# # new_doc.save("split_output.pdf")

# # doc1 = fitz.open("file1.pdf")
# # doc2 = fitz.open("file2.pdf")

# # doc1.insert_pdf(doc2)
# # doc1.save("merged_output.pdf")




# import fitz

# # Open the PDF
# doc = fitz.open("work.pdf")

# # Extract and print text from each page
# for page_num in range(len(doc)):
#     page = doc[page_num]
#     text = page.get_text()
#     print(f"Page {page_num + 1} Text:")
#     print(text)

# # Extract images from the first page
# page = doc[0]
# images = page.get_images(full=True)

# for img_index, img in enumerate(images):
#     xref = img[0]
#     base_image = doc.extract_image(xref)
#     image_bytes = base_image["image"]
#     image_ext = base_image["ext"]

#     with open(f"page_1_image_{img_index + 1}.{image_ext}", "wb") as img_file:
#         img_file.write(image_bytes)

# # Close the document
# doc.close()


from PIL import Image
import pytesseract

# Path to Tesseract executable (adjust this for your OS)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image
image = Image.open("page_199_image_1.png")

# Extract text
text = pytesseract.image_to_string(image)

print("Extracted Text:")
print(text)


# import pytesseract

# # Set the path to Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
