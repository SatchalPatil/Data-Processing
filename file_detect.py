import os

def detect_file_type(file_name):
    file_extension = file_name.split('.')[-1].lower()
    if file_extension == "pdf":
        return "pdf"
    elif file_extension == "docx":
        return "docx"
    elif file_extension in ["xls", "xlsx"]:
        return "excel"
    elif file_extension in ["jpg", "jpeg", "png"]:
        return "image"
    else:
        return None

def save_to_file(file_name, text):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Extracted text saved to {file_name}")
