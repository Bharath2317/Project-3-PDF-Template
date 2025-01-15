from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P",unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)

df = pd.read_csv("topics.csv")

for index,row in df.iterrows():
    pdf.add_page()

    #set the Header
    pdf.set_font(family="Times",style="B",size=20)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",ln=1)
    pdf.line(10,20,200,20)

    #set footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(140, 140, 140)
    pdf.cell(w=0, h=8, txt=row["Topic"], align="R", ln=1)

    for i in range(row["Pages"]):
        pdf.add_page()

        #set footer
        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(140, 140, 140)
        pdf.cell(w=0, h=8, txt=row["Topic"], align="R", ln=1)

pdf.output("output.pdf")