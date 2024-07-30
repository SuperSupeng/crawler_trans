import os 
import argparse
import sys
sys.path.append('./src')

import translation_agent as ta
import crawler as cr

script_dir = os.path.dirname(os.path.abspath(__file__))

def write_to_file(content, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

def crawl_and_save(url):
    content=cr.fetch_content(url)
    title = cr.get_title(content)
    file_en_path = "./content_en/" + title + ".md"
    full_path = os.path.join(script_dir, file_en_path)
    write_to_file(content, full_path)
    return title

def translate_and_save(title):
    source_lang, target_lang, country = "English", "Chinexe", "China"
    file_en_path = "./content_en/" + title + ".md"
    full_path = os.path.join(script_dir, file_en_path)

    with open(full_path, encoding="utf-8") as file:
        source_text = file.read()

    translation = ta.translate(
        source_lang=source_lang,
        target_lang=target_lang,
        source_text=source_text,
        country=country,
    )

    file_zh_path = "./content_zh/" + title + ".md"
    full_path = os.path.join(script_dir, file_zh_path)
    write_to_file(translation, full_path)

    return translation

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Fetch content from a URL and extract the title.")
    parser.add_argument("url", help="The URL to fetch content from")
    args = parser.parse_args()
    url = args.url

    # title = crawl_and_save(url)
    title = "test"
    print(f"Saved to content_en/{title}.md")
    translation = translate_and_save(title)
    print(translation)