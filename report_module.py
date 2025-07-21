import os

import pandas as pd
import plotly.express as px
from markdown_pdf import MarkdownPdf, Section

from interfaces.form_response import FormResponse

SAMPLE_SUMMARY_PARAGRAPH = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris interdum, ipsum id eleifend interdum, lectus tellus iaculis est, ac fringilla tortor ipsum ut elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nulla non mattis neque. Vivamus vel purus dolor. Nunc in efficitur lectus, ac iaculis tortor. Fusce id lorem condimentum, efficitur ante non, tristique ligula. Quisque feugiat velit eu pretium aliquet."
RADAR_CHART_IMAGE_PATH = "images/radar_chart.png"


def generate_report_markdown(data: FormResponse):
    """
    Generate a markdown report from the provided data.

    Args:
        data (FormResponse): The data to include in the report.

    Returns:
        str: The generated markdown report.
    """

    pdf = MarkdownPdf(toc_level=2, optimize=True)

    insert_cover_page(pdf, data)
    insert_executive_summary(pdf, data)

    # pdf.add_section(
    #     Section(f"""# <a name='head1'></a>Head1\n\n{data['church_name']}\n"""),
    #     user_css="h1 {text-align:center;}"
    # )

    report_path = f"church_missions_readiness_report_{data.answers.church}.pdf"
    pdf.save(report_path)
    clean_up_radar_chart()

    return report_path


def insert_cover_page(pdf, data: FormResponse):
    church_name = data.answers.church or "Unknown Church"
    respondent = data.answers.respondent or "Anonymous"
    # role = data.answers.role or ""

    cover_page = f"# Church Missions Readiness Report\n\nPrepared for: {church_name}\n\nCompleted by: {respondent}\n\nDate: Test Date\n\nBased on the Antioch21 Church Missions Readiness Assessment (CMRA)\n\n"

    pdf.add_section(Section(cover_page))


def insert_executive_summary(pdf, data: FormResponse):
    overall_readiness_score = data.scores.finalpercentage or 0
    top_3 = data.scores.top_3_strongest_subdomains
    bottom_3 = data.scores.bottom_3_weakest_subdomains

    executive_summary = f"## Overall Readiness Score: {overall_readiness_score}\n\n{SAMPLE_SUMMARY_PARAGRAPH}\n\n"

    radar_chart_path = generate_executive_summary_radar_chart(data)
    executive_summary += f"![Radar Chart]({radar_chart_path})\n\n"

    executive_summary += "## Top 3 Strongest Sub-domains\n\n"
    executive_summary += f"- {top_3[0][0]}\n- {top_3[1][0]}\n- {top_3[2][0]}\n\n"

    executive_summary += "## 3 Areas for Growth\n\n"
    executive_summary += (
        f"- {bottom_3[0][0]}\n- {bottom_3[1][0]}\n- {bottom_3[2][0]}\n\n"
    )

    pdf.add_section(Section(executive_summary))


def generate_executive_summary_radar_chart(data: FormResponse):
    """
    Generate a radar chart for the executive summary.

    Args:
        data (FormResponse): The data to include in the radar chart.

    Returns:
        str: The path to the generated radar chart image.
    """
    values = [
        (data.scores.discipleship / 25) * 100,
        (data.scores.sending / 25) * 100,
        (data.scores.support / 25) * 100,
        (data.scores.structure / 25) * 100,
    ]

    df = pd.DataFrame(
        dict(
            r=values,
            theta=[
                "Discipleship",
                "Sending",
                "Support",
                "Structure",
            ],
        )
    )
    fig = px.line_polar(df, r="r", theta="theta", line_close=True)
    fig.update_traces(fill="toself")
    fig.write_image(RADAR_CHART_IMAGE_PATH)

    # This function should create a radar chart based on the scores in `data`
    # and return the path to the saved image.
    return RADAR_CHART_IMAGE_PATH


def clean_up_radar_chart():
    """
    Clean up the radar chart image after use.
    """
    if os.path.exists(RADAR_CHART_IMAGE_PATH):
        os.remove(RADAR_CHART_IMAGE_PATH)


def clean_up_report(report_path):
    """
    Clean up the generated report file after use.
    """
    if os.path.exists(report_path):
        os.remove(report_path)


if __name__ == "__main__":
    # Example data to generate a report
    example_data = {
        "church_name": "Antioch21",
        "respondent": "John Doe",
        "date": "2023-10-01",
        "overall_readiness_score": 85,
    }

    report = generate_report_markdown(example_data)
    print(report)
