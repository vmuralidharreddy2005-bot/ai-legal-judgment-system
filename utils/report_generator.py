from fpdf import FPDF

def generate_pdf_report(

    summary,
    prediction,
    confidence

):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=16)

    pdf.cell(
        200,
        10,
        txt="AI Legal Analysis Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(
        0,
        10,
        txt=f"AI Summary:\n\n{summary}"
    )

    pdf.ln(5)

    pdf.multi_cell(
        0,
        10,
        txt=f"Prediction Result: {prediction}"
    )

    pdf.ln(5)

    pdf.multi_cell(
        0,
        10,
        txt=f"Confidence Score: {confidence:.2f}%"
    )

    output_path = "legal_report.pdf"

    pdf.output(output_path)

    return output_path