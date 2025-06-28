from docx import Document


doc = Document("my_report.docx")

for item in doc.paragraphs:
    if "paragraph" in item.text:
        item.text = item.text.replace("paragraph", "[CENSORED]")

doc.save("censored_my_report.docx")
