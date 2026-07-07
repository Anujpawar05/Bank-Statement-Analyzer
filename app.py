import fitz

pdf_path = "uploads/statement.pdf"
password = input("Enter PDF Password (leave blank if none): ")

doc = fitz.open(pdf_path)

if doc.needs_pass:
    if not doc.authenticate(password):
        print("Wrong password!")
        exit()

print(f"Pages: {doc.page_count}")

for page_no in range(doc.page_count):
    page = doc.load_page(page_no)

    print(f"\n========== PAGE {page_no + 1} ==========")

    words = page.get_text("words")

    print(f"Words found: {len(words)}")

    if words:
        print(words[:10])   # Show first 10 words