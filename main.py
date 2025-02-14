import os
import nltk
nltk.download('punkt')

from file_detect import detect_file_type, save_to_file
from extractor import (
    extract_text_from_pdf,
    extract_text_from_docx,
    extract_text_with_ocr,
    extract_data_from_excel,
    extract_text_from_image
)
from textclean import clean_text_with_nltk

def process_directory(directory_path):
    if not os.path.exists(directory_path):
        print(f"Directory not found: {directory_path}")
        return

    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            file_type = detect_file_type(file_name)
            try:
                with open(file_path, "rb") as file:
                    if file_type == "pdf":
                        print(f"Processing PDF: {file_name}")
                        extracted_text = extract_text_from_pdf(file)
                    elif file_type == "docx":
                        print(f"Processing DOCX: {file_name}")
                        extracted_text = extract_text_from_docx(file)
                    elif file_type == "excel":
                        print(f"Processing Excel: {file_name}")
                        extracted_text = extract_data_from_excel(file)
                    elif file_type == "image":
                        print(f"Processing Image: {file_name}")
                        extracted_text = extract_text_from_image(file)
                    else:
                        print(f"Skipping unsupported file: {file_name}")
                        continue

                    # Apply cleaning only to PDF and DOCX files
                    if file_type in ["pdf", "docx"]:
                        cleaned_text = clean_text_with_nltk(extracted_text)
                    else:
                        cleaned_text = extracted_text

                    output_file = os.path.join(directory_path, f"{os.path.splitext(file_name)[0]}.txt")
                    save_to_file(output_file, cleaned_text)
            except Exception as e:
                print(f"Error processing file {file_name}: {e}")

def main():
    print("Enter the path of the directory containing your files:")
    print("Type 'exit' to quit the program.\n")
    while True:
        directory_path = input("Enter the directory path: ").strip()
        if directory_path.lower() in ['exit', 'quit']:
            print("Exiting the program.")
            break
        process_directory(directory_path)
        print("\nProcessing complete. You can enter another directory or type 'exit' to quit.\n")

if __name__ == "__main__":
    main()
