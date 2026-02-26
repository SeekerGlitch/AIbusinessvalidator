#input --> business idea
#country
#audience
#online, offline, product

#streamlit, google-genai, reportlab


import streamlit as st
from google import genai
from google.genai import types
import os
from reportlab.pdfgen import canvas

st.title("AI business Idea Validator")

idea = st.text_area("Business Idea")
location =st.text_input("Target Country & city")
biz_type =st.selectbox ("Business type", ["online", "offline", "product", "service"])
audience = st.text_input("Whose your audience")

client = genai.Client(api_key = os.getenv("API_KEY")

if st.button("Generate report"):

    prompt = f"""

    Analyse this business idea:
    Idea : {idea}
    Location: {location}
    type: {biz_type}
    audience: {audience}


    Give a structured report with:
    1.Overview
    2.Market Analysis
    3.Revenue possibility
    4.Funding options
    5.Competitor Analysis



"""
    answer = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = prompt
        )
    st.subheader("AI Analysis")
    st.write(answer.text)


    report_content = answer.text

    pdffile = "Analysis_report.pdf"

    c = canvas.Canvas(pdffile)
    c.setFont("Helvetica",12)

    y = 800
    #\n --> new line
    for line in report_content.split("\n"):
        c.drawString(50,y,line)
        y= y - 15

        if y<50:
            c.showPage()
            y=800
    c.save()

    with open(pdffile,"rb") as file:
              st.download_button(
                  label="Download report",
                  data =file,
                  file_name = "Analysis_report.pdf"

                  )
    
    

