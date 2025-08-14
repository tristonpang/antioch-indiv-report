import math
import os
import string
from enum import Enum

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from markdown_pdf import MarkdownPdf, Section

from content.summary_text import (
    DOMAIN_LEVEL_SUMMARY_INSIGHTS,
    KEY_NEXT_STEP,
    SUBDOMAIN_LEVEL_TEXT_CONTENT,
)
from interfaces.form_response import FormResponse

SAMPLE_SUMMARY_PARAGRAPH = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris interdum, ipsum id eleifend interdum, lectus tellus iaculis est, ac fringilla tortor ipsum ut elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nulla non mattis neque. Vivamus vel purus dolor. Nunc in efficitur lectus, ac iaculis tortor. Fusce id lorem condimentum, efficitur ante non, tristique ligula. Quisque feugiat velit eu pretium aliquet."
RADAR_CHART_IMAGE_PATH = "images/radar_chart.png"
DOMAIN_TABLE_IMAGE_PATH = "images/domain_table.png"
LOGO_IMAGE_PATH = "images/logo_small.png"

Subdomains = Enum(
    "Subdomains",
    [
        ("education", "Education"),
        ("training", "Training"),
        ("sending1", "Sending"),
        ("membercare", "Member Care"),
        ("praying", "Praying"),
        ("giving", "Giving"),
        ("community", "Community"),
        ("organisation", "Organisation"),
        ("policies", "Policies"),
        ("partnerships", "Partnerships"),
    ],
)

Domains = Enum(
    "Domains",
    [
        ("discipleship", "Discipleship"),
        ("sending", "Sending"),
        ("support", "Support"),
        ("structure", "Structure"),
    ],
)

IconPaths = Enum(
    "IconPaths",
    [
        ("education", "images/education.png"),
        ("training", "images/training.png"),
        ("sending1", "images/sending1.png"),
        ("membercare", "images/membercare.png"),
        ("praying", "images/praying.png"),
        ("giving", "images/giving.png"),
        ("community", "images/community.png"),
        ("organisation", "images/organisation.png"),
        ("policies", "images/policies.png"),
        ("partnerships", "images/partnerships.png"),
    ],
)


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
    insert_domain_overview_table(pdf, data)

    insert_domain_breakdown(
        pdf, data, 1, Domains.discipleship.value, ["education", "training"]
    )
    insert_domain_breakdown(
        pdf, data, 2, Domains.sending.value, ["sending1", "membercare"]
    )
    insert_domain_breakdown(
        pdf, data, 3, Domains.support.value, ["praying", "giving", "community"]
    )
    insert_domain_breakdown(
        pdf,
        data,
        4,
        Domains.structure.value,
        ["organisation", "policies", "partnerships"],
    )
    insert_final_page(pdf)

    report_path = f"church_missions_readiness_report_{data.answers.church}.pdf"
    pdf.save(report_path)
    clean_up_generated_images()

    return report_path


def calculate_stage(score):
    stage = math.floor((score / 100) * 5)
    return stage if stage > 0 else 1


def insert_cover_page(pdf, data: FormResponse):
    church_name = data.answers.church or "Unknown Church"
    respondent = data.answers.respondent or "Anonymous"
    submitted_at = data.submitted_at or "Unknown Date"

    cover_page = f"![Logo image]({LOGO_IMAGE_PATH})\n\n"
    cover_page += f"# Church Missions Readiness Report\n\n<br><br>Prepared for: {church_name}\n\nCompleted by: {respondent}\n\nDate: {submitted_at}\n\nBased on the Antioch21 Church Missions Readiness Assessment (CMRA)\n\n"

    css = "h1 { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; } p { font-family: Arial, sans-serif; text-align: center; }"

    pdf.add_section(Section(cover_page), user_css=css)


def insert_executive_summary(pdf, data: FormResponse):
    overall_readiness_score = data.scores.finalpercentage or 0
    top_3 = data.scores.top_3_strongest_subdomains
    bottom_3 = data.scores.bottom_3_weakest_subdomains

    executive_summary = f"## Overall Readiness Score: {overall_readiness_score}\n\n{SAMPLE_SUMMARY_PARAGRAPH}\n\n"

    radar_chart_path = generate_executive_summary_radar_chart(data)
    executive_summary += f"![Radar Chart]({radar_chart_path})\n\n"

    domain_summary = "### Top 3 Strongest Sub-domains\n\n"
    domain_summary += "| | | |\n| :---: | :---: | :---: |\n"
    domain_summary += f"| ![subdomain1]({IconPaths[top_3[0][0]].value}) | ![subdomain2]({IconPaths[top_3[1][0]].value}) | ![subdomain3]({IconPaths[top_3[2][0]].value}) |\n"
    domain_summary += f"| {Subdomains[top_3[0][0]].value} | {Subdomains[top_3[1][0]].value} | {Subdomains[top_3[2][0]].value} |\n"
    domain_summary += f"| Stage {calculate_stage(top_3[0][1])} | Stage {calculate_stage(top_3[1][1])} | Stage {calculate_stage(top_3[2][1])} |\n\n"

    domain_summary += "### 3 Areas for Growth\n\n"
    # executive_summary += f"- {Subdomains[bottom_3[0][0]].value} - Stage {calculate_stage(bottom_3[0][1])}\n- {Subdomains[bottom_3[1][0]].value} - Stage {calculate_stage(bottom_3[1][1])}\n- {Subdomains[bottom_3[2][0]].value} - Stage {calculate_stage(bottom_3[2][1])}\n\n"
    domain_summary += "| | | |\n| :---: | :---: | :---: |\n"
    domain_summary += f"| ![subdomain1]({IconPaths[bottom_3[0][0]].value}) | ![subdomain2]({IconPaths[bottom_3[1][0]].value}) | ![subdomain3]({IconPaths[bottom_3[2][0]].value}) |\n"
    domain_summary += f"| {Subdomains[bottom_3[0][0]].value} | {Subdomains[bottom_3[1][0]].value} | {Subdomains[bottom_3[2][0]].value} |\n"
    domain_summary += f"| Stage {calculate_stage(bottom_3[0][1])} | Stage {calculate_stage(bottom_3[1][1])} | Stage {calculate_stage(bottom_3[2][1])} |\n"

    css = "h1 { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; color: #AD0B0B; } table { margin-left: 55px } td { font-family: Arial, sans-serif; padding-left: 30px; padding-right: 30px; text-align: center; } h3 { text-align: center; font-family: Arial, sans-serif; margin-top: 30px} h2, p { font-family: Arial, sans-serif; }"

    pdf.add_section(Section(executive_summary), user_css=css)
    pdf.add_section(Section(domain_summary), user_css=css)


def insert_domain_overview_table(pdf, data: FormResponse):
    """
    Insert a table summarizing the scores for each domain.

    Args:
        pdf (MarkdownPdf): The PDF object to add the table to.
        data (FormResponse): The data containing scores for each domain.
    """
    # table_header = "| Domain | Score (%) | Stage (Avg) | Summary Insight |\n| :--- | :---: | :---: | :--- |\n"
    # table_rows = [
    #     f"| {Domains[domain].value} | {(getattr(data.scores, domain) / 25) * 100}% | {calculate_stage((getattr(data.scores, domain) / 25) * 100)} | {DOMAIN_LEVEL_SUMMARY_INSIGHTS[domain][calculate_stage((getattr(data.scores, domain) / 25) * 100)]} |\n"
    #     for domain in ["discipleship", "sending", "support", "structure"]
    # ]
    # table_content = "".join(table_rows)

    css = "table, th, td { border: 1px solid black; font-family: Arial, sans-serif; } h2 { font-family: Arial, sans-serif; }"

    table = f"![domain table]({generate_styled_table(data)})"

    pdf.add_section(Section("## Domain Overview\n\n" + table), user_css=css)


def generate_styled_table(data: FormResponse):
    fig = go.Figure(
        data=[
            go.Table(
                columnwidth=[150, 100, 100, 300],
                header=dict(
                    values=["Domain", "Score (%)", "Stage (Avg)", "Summary Insight"],
                    line_color="darkslategray",
                    fill_color="lightskyblue",
                    align="center",
                ),
                cells=dict(
                    values=[
                        [
                            Domains[domain].value
                            for domain in [
                                "discipleship",
                                "sending",
                                "support",
                                "structure",
                            ]
                        ],  # 1st column
                        [
                            f"{(getattr(data.scores, domain) / 25) * 100}%"
                            for domain in [
                                "discipleship",
                                "sending",
                                "support",
                                "structure",
                            ]
                        ],  # 2nd column
                        [
                            calculate_stage((getattr(data.scores, domain) / 25) * 100)
                            for domain in [
                                "discipleship",
                                "sending",
                                "support",
                                "structure",
                            ]
                        ],  # 3rd column
                        [
                            DOMAIN_LEVEL_SUMMARY_INSIGHTS[domain][
                                calculate_stage(
                                    (getattr(data.scores, domain) / 25) * 100
                                )
                            ]
                            for domain in [
                                "discipleship",
                                "sending",
                                "support",
                                "structure",
                            ]
                        ],  # 4th column
                    ],
                    line_color="darkslategray",
                    fill_color="lightcyan",
                    align="left",
                ),
            )
        ]
    )

    # fig.update_layout(width=700)
    fig.write_image(DOMAIN_TABLE_IMAGE_PATH)
    return DOMAIN_TABLE_IMAGE_PATH


def insert_domain_breakdown(
    pdf, data: FormResponse, domain_number, domain_name, subdomains
):
    """
    Insert a breakdown of scores for each sub-domain within each domain.

    Args:
        pdf (MarkdownPdf): The PDF object to add the breakdown to.
        data (FormResponse): The data containing scores for each sub-domain.
    """
    title = f"## Domain {domain_number}: {domain_name}\n\n"
    content = ""
    for subdomain_index, subdomain in enumerate(subdomains):
        subdomain_name = Subdomains[subdomain].value
        subdomain_score = getattr(data.scores, subdomain)
        subdomain_stage = calculate_stage(subdomain_score)
        content += f"### {domain_number}{string.ascii_uppercase[subdomain_index]}. {subdomain_name}\n\n"
        content += f"Score: {subdomain_score}%\n\n"
        content += f"Stage: {subdomain_stage}\n\n"
        content += f"Next Step: \n * {SUBDOMAIN_LEVEL_TEXT_CONTENT[subdomain][subdomain_stage][KEY_NEXT_STEP]}\n\n"
    content += "---\n\n"

    pdf.add_section(Section(title + content))


def insert_final_page(pdf):
    """
    Insert a section for reflections and notes.

    Args:
        pdf (MarkdownPdf): The PDF object to add the reflections and notes to.
    """
    reflections_section = "## Reflections and Notes\n\n"
    reflections_section += "*Feel free  to complete the following prompts and discuss them with your church leadership team.*\n\n<br>"
    reflections_section += (
        "1. What is one area you can improve in the next 3 months? \n\n<br><br>"
    )
    reflections_section += "2. Who in your church leadership team can you share this report with? \n\n<br><br>"
    reflections_section += (
        "3. What kind of external support would help you grow? \n\n<br><br>"
    )
    reflections_section += "<hr>\n\n"

    reflections_section += "**Contact Antioch21 if you’d like help processing your results**\n\n Email: [darrellong@antioch21.sg](mailto:darrellong@antioch21.sg)\n\nWebsite: [antioch21.sg](https://antioch21.sg)\n\n"

    pdf.add_section(Section(reflections_section))


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


def clean_up_generated_images():
    """
    Clean up the radar chart image after use.
    """
    if os.path.exists(RADAR_CHART_IMAGE_PATH):
        os.remove(RADAR_CHART_IMAGE_PATH)
    if os.path.exists(DOMAIN_TABLE_IMAGE_PATH):
        os.remove(DOMAIN_TABLE_IMAGE_PATH)


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
