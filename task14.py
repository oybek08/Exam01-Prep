fayl_nomi = "report.pdf"

if fayl_nomi.endswith(".pdf"):
    tur = "pdf"
elif fayl_nomi.endswith(".docx"):
    tur = "docx"
elif fayl_nomi.endswith(".txt"):
    tur = "txt"
else:
    tur = "noma'lum"

print(f"Fayl turi: {tur}")