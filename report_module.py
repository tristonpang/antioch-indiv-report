from markdown_pdf import MarkdownPdf, Section

SAMPLE_SUMMARY_PARAGRAPH = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris interdum, ipsum id eleifend interdum, lectus tellus iaculis est, ac fringilla tortor ipsum ut elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nulla non mattis neque. Vivamus vel purus dolor. Nunc in efficitur lectus, ac iaculis tortor. Fusce id lorem condimentum, efficitur ante non, tristique ligula. Quisque feugiat velit eu pretium aliquet.'

def generate_report_markdown(data):
    """
    Generate a markdown report from the provided data.
    
    Args:
        data (dict): The data to include in the report.
        
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

    return 'PDF report generated successfully.'

def insert_cover_page(pdf, data):
    cover_page = f"# Church Missions Readiness Report\n\nPrepared for: {data['church_name']}\n\nCompleted by: {data['respondent']}\n\nDate: {data['date']}\n\nBased on the Antioch21 Church Missions Readiness Assessment (CMRA)\n\n"

    pdf.add_section(Section(cover_page))

def insert_executive_summary(pdf, data):
    executive_summary = f"## Overall Readiness Score: {data['overall_readiness_score']}\n\n{SAMPLE_SUMMARY_PARAGRAPH}\n\n"

    executive_summary += '## Top 3 Strongest Sub-domains\n\n'
    executive_summary += '- Sub-domain 1\n- Sub-domain 2\n- Sub-domain 3\n\n'

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