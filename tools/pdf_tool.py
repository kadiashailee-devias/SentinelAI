from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


def create_pdf_report(filename: str, title: str, content: str):
    """
    Create a simple disaster response PDF report.
    """

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph(f"<b>{title}</b>", styles["Title"]))

    story.append(Paragraph(content.replace("\n", "<br/>"), styles["BodyText"]))

    doc.build(story)

    return filename