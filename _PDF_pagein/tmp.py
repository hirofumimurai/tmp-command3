from reportlab.pdfgen import canvas
import sys

def create_pdf(filename):
    #page_width = 595.276  # ページ幅をptsで指定
    #page_height = 841.89  # ページ高さをptsで指定
    page_width = float(sys.argv[2])  # ページ幅をptsで指定
    page_height = float(sys.argv[3])  # ページ高さをptsで指定
    c = canvas.Canvas(filename, pagesize=(page_width, page_height))
    

    #text = "Welcome to ReportLab!"
    text = sys.argv[4]

    font_size = 12  # フォントサイズを指定
    text_width = c.stringWidth(text, "Helvetica", font_size)

    #c.setFillColorRGB(0.9, 0.9, 0.9)  # 背景色を設定（灰色）
    #c.rect(page_width - text_width - 12, 0, text_width + 5, font_size + 5, fill=1)  # 背景を描画

    #text_width, text_height = c.stringWidth(text), c.getFont().size
    #c.drawString(page_width - text_width - 100, page_height - font_size - 100, text)
    #c.drawString(page_width - text_width - 100, font_size + 100, text)
    #c.setFillColorRGB(0, 0, 0)  # テキストの色を設定（黒色）
    c.drawString(page_width - text_width - 10, font_size + 0, text)
    c.save()

def create_pdf2(filename):
    #page_width = 595.276  # ページ幅をptsで指定
    #page_height = 841.89  # ページ高さをptsで指定
    page_width = float(sys.argv[2])  # ページ幅をptsで指定
    page_height = float(sys.argv[3])  # ページ高さをptsで指定
    c = canvas.Canvas(filename, pagesize=(page_width, page_height))
    

    #text = "Welcome to ReportLab!"
    text = sys.argv[4] + '/' + sys.argv[5]
    #text2 = sys.argv[1]

    font_size = 12  # フォントサイズを指定
    text_width = c.stringWidth(text, "Helvetica", font_size)
    #text2_width = c.stringWidth(text2, "Helvetica", font_size)


    #c.setFillColorRGB(0.9, 0.9, 0.9)  # 背景色を設定（灰色）
    #c.rect(page_width - text_width - 12, 0, text_width + 5, font_size + 5, fill=1)  # 背景を描画


    #text_width, text_height = c.stringWidth(text), c.getFont().size
    #c.drawString(page_width - text2_width - 10, page_height - font_size - 10, text2)
    #c.drawString(page_width - text_width - 100, font_size + 100, text)
    c.drawString(page_width - text_width - 10, font_size + 0, text)
    c.save()

def create_pdf3(filename):
    #page_width = 595.276  # ページ幅をptsで指定
    #page_height = 841.89  # ページ高さをptsで指定
    page_width = float(sys.argv[2])  # ページ幅をptsで指定
    page_height = float(sys.argv[3])  # ページ高さをptsで指定
    c = canvas.Canvas(filename, pagesize=(page_width, page_height))
    

    #text = "Welcome to ReportLab!"
    text = sys.argv[4] + '/' + sys.argv[5]
    text2 = sys.argv[1]

    font_size = 12  # フォントサイズを指定
    text_width = c.stringWidth(text, "Helvetica", font_size)
    text2_width = c.stringWidth(text2, "Helvetica", font_size)

    #c.setFillColorRGB(0.9, 0.9, 0.9)  # 背景色を設定（灰色）
    #c.rect(page_width - text_width - 12, 0, text_width + 5, font_size + 5, fill=1)  # 背景を描画



    #text_width, text_height = c.stringWidth(text), c.getFont().size
    c.drawString(page_width - text2_width - 10, page_height - font_size - 10, text2)
    #c.drawString(page_width - text_width - 100, font_size + 100, text)
    c.drawString(page_width - text_width - 10, font_size + 0, text)
    c.save()

create_pdf(sys.argv[1] + '_stamp_page-only.pdf')
create_pdf2(sys.argv[1] + '_stamp_pages.pdf')
create_pdf3(sys.argv[1] + '_stamp_all.pdf')

