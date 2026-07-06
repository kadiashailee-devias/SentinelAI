import os

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


def create_pdf_report(filename: str, title: str, content: str):
    """
    Create a disaster response PDF report.
    """

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(title, styles["Title"])
    )

    story.append(
        Paragraph(
            content.replace("\n", "<br/>"),
            styles["BodyText"],
        )
    )

    doc.build(story)

    return filename


def generate_pdf(report_text: str):
    """
    Generate a SentinelAI PDF report and return its path.
    """

    os.makedirs("reports", exist_ok=True)

    pdf_path = os.path.join(
        "reports",
        "SentinelAI_Report.pdf",
    )

    create_pdf_report(
        filename=pdf_path,
        title="SentinelAI Disaster Response Report",
        content=report_text,
    )

    return pdf_path