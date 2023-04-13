from PyPDF2 import PdfReader

#ファイル名aa.pdfのファイルを読み取る
with open("aa.pdf", "rb") as input:
    reader = PdfReader(input)
    page = reader.pages[0] 

    # 読み込んだページのテキストを抽出
    print(page.extract_text())