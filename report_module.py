from markdown_pdf import MarkdownPdf, Section

from interfaces.form_response import FormResponse

SAMPLE_SUMMARY_PARAGRAPH = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris interdum, ipsum id eleifend interdum, lectus tellus iaculis est, ac fringilla tortor ipsum ut elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nulla non mattis neque. Vivamus vel purus dolor. Nunc in efficitur lectus, ac iaculis tortor. Fusce id lorem condimentum, efficitur ante non, tristique ligula. Quisque feugiat velit eu pretium aliquet."


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

    pdf.save(f"church_missions_readiness_report_{data['church_name']}.pdf")

    return "PDF report generated successfully."


def insert_cover_page(pdf, data: FormResponse):
    church_name = data.answers.church or "Unknown Church"
    respondent = data.answers.respondent or "Anonymous"
    role = data.answers.role or ""

    cover_page = f"# Church Missions Readiness Report\n\nPrepared for: {church_name}\n\nCompleted by: {respondent}\n\nDate: {data['date']}\n\nBased on the Antioch21 Church Missions Readiness Assessment (CMRA)\n\n"

    pdf.add_section(Section(cover_page))


def insert_executive_summary(pdf, data: FormResponse):
    overall_readiness_score = data.scores.finalpercentage or 0
    top_3 = data.scores.top_3_strongest_subdomains
    bottom_3 = data.scores.bottom_3_weakest_subdomains

    executive_summary = f"## Overall Readiness Score: {overall_readiness_score}\n\n{SAMPLE_SUMMARY_PARAGRAPH}\n\n"

    # TODO: Generate and insert radar chart here

    executive_summary += "## Top 3 Strongest Sub-domains\n\n"
    executive_summary += f"- {top_3[0][0]}\n- {top_3[1][0]}\n- {top_3[2][0]}\n\n"

    executive_summary += "## 3 Areas for Growth\n\n"
    executive_summary += (
        f"- {bottom_3[0][0]}\n- {bottom_3[1][0]}\n- {bottom_3[2][0]}\n\n"
    )

    pdf.add_section(Section(executive_summary))


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
