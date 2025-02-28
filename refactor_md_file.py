from openai import OpenAI
from pydantic import BaseModel
from typing import List
import yaml


class MarkdownFileYAML(BaseModel):
    title: str
    date: str
    updated: str
    tags: list[str]
    toc: bool


class MarkdownFileContent(BaseModel):
    full_text: str
    introduction: str
    quick_start: str
    recap: List[str]
    reference: List[str]


class MarkdownFile(BaseModel):
    yaml: MarkdownFileYAML
    content: MarkdownFileContent


def convert_to_markdown(md_file: MarkdownFile) -> str:
    """
    Convert a MarkdownFile object to a properly formatted Markdown string.
    """
    # Convert YAML to string format
    yaml_content = yaml.dump(
        md_file.yaml.model_dump(mode="json"), sort_keys=False)

    # Convert reference list to Markdown bullet points
    references = "\n".join(f"- {url}" for url in md_file.content.reference)

    # Convert recap list to Markdown bullet points
    recap = "\n".join(f"- {point}" for point in md_file.content.recap)

    # Assemble final Markdown content
    markdown_output = f"""---
{yaml_content}---

# 📌 Introduction
{md_file.content.introduction}
<!-- more -->

# 🚀 Quick Start
{md_file.content.quick_start}

# 🔁 Recap
{recap}

# 🔗 References
{references}
"""

    return markdown_output


def refactor_md_file(client: OpenAI, full_text: str) -> MarkdownFile:

    prompt = """
    Please read the following IT Blog article and summarize it according to the specified format:

    - **Introduction**: Summarize the key points of this article.
    - **Quick Start**: Extract all operational steps and commands mentioned in the article.
        - **Note**: Please **do not refactor / modify / remove** the content. Keep it exactly as it appears in the article. Include all commands, descriptions and details. 
        - **Note**: Please **do not include** the comments in the markdown file.
    - **Recap**: List the key takeaways from this article in bullet points.
    - **Reference**: Extract and list only the URLs that serve as references or additional resources. 
        - Exclude any URLs that are part of example commands (e.g., `pip install git+https://github.com/...` or similar).
        - Include only URLs that are cited as sources, documentation, or further reading.

    Article content:
    ---
    {full_text}
    """

    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for refactoring markdown files into specific formats."},
            {"role": "user", "content": prompt.format(full_text=full_text)},
        ],
        response_format=MarkdownFile
    )
    return response.choices[0].message.parsed


if __name__ == "__main__":

    import datetime
    import os
    from dotenv import load_dotenv

    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Load the source file
    md_files = os.listdir("source/_posts")

    for md_file in md_files:
        if "chinese" in md_file:
            continue

        else:
            print(f"Processing {md_file}")
            with open(f"source/_posts/{md_file}", "r") as f:
                full_text = f.read()

            response = refactor_md_file(client, full_text)
            response.yaml.updated = datetime.datetime.now().strftime("%Y-%m-%d")
            markdown_string = convert_to_markdown(response)

            # Save to file
            with open(f"source/{md_file}", "w") as f:
                f.write(markdown_string)
