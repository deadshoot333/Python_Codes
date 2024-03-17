from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("PDF_Generator/topics.csv")

for index, row in df.iterrows():
    # print(row["Topic"])
    pdf.add_page()  # total number of row is the total page numbers
    pdf.set_text_color(255, 150, 55)
    pdf.set_font(family="Times", style="B", size=20)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(10, 21, 200, 21)  ## x1,y1,x2,y2 and unit is in mm
    # pdf.cell(
    #     w=0, h=12, txt="HI I am first cell", align="L", ln=1, border=1
    # )  ## if w=0 then border will be in the whole width of pdf
    # pdf.set_font(family="Times", style="I", size=20)
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        ##set footer
        pdf.ln(265)
        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=5, txt=row["Topic"], align="R")
    pdf.line(10, 280, 200, 280)

pdf.output("PDF_Generator/MyPDF.pdf")
