from pypdf import PdfReader
from transformers import pipeline

print("Loading summarization model...")

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

pdf_file = input(
    "\nEnter PDF file path: "
)

reader = PdfReader(pdf_file)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text + " "

print("\nDocument loaded successfully.")
print("Generating summary...")

# Limit text for the model
text = text[:4000]

summary = summarizer(
    text,
    max_length=150,
    min_length=50,
    do_sample=False
)

print("\n==========================================")
print("          DOCUMENT SUMMARY")
print("==========================================")

print(summary[0]["summary_text"])