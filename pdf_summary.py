from openai import OpenAI
from dotenv import load_dotenv
import os
import pymupdf


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
model_ver = os.getenv("MODEL_VER")


def pdf_to_text(pdf_file_path):
    doc = pymupdf.open(pdf_file_path)

    header_height = 80
    footer_height = 80
    full_text = ""

    for page in doc:
        rect = page.rect
        text = page.get_text(clip=(0, header_height, rect.width, rect.height - footer_height))
        full_text += text + "\n------------------------------------------------------------\n"

    txt_file_path = "data/output/text_sample.txt"
    with open(txt_file_path, "w", encoding="utf-8") as f:
        f.write(full_text)
    
    return txt_file_path


def summarize_txt(txt_file_path):
    client = OpenAI(api_key=api_key)

    with open(txt_file_path, "r", encoding="utf-8") as f:
        txt = f.read()

    system_prompt = f"""
        You are a bot that summarizes the following text.
        Read the text below and identify the author’s problem awareness and argument, then summarize the main points in Korean.

        The format you must write in is as follows:
        # Title
        ## Author’s Problem Awareness & Argument
        ## Author Introduction

        ========== Text follows ==========
        {txt}
    """
    response = client.chat.completions.create(
        model=model_ver,
        temperature=0.1,
        messages=[
            {"role": "system", "content": system_prompt},
        ]
    )
    return response.choices[0].message.content


def summarize_pdf(file_path, dest_path):
    txt_file_path = pdf_to_text(file_path)
    summary = summarize_txt(txt_file_path)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(summary)


if __name__ == "__main__":
    pdf_file_path = "data/input/pdf_sample.pdf"
    dest_path = "data/output/result.txt"
    summarize_pdf(pdf_file_path, dest_path)