import os
import markdown

def convert_to_html(markdown_filename):
    with open(markdown_filename, 'r') as markdown_in:
        md_text = markdown_in.read()
        html_text = markdown.markdown(md_text)

    with open("style.css", 'r') as css_in:
        css_text = css_in.read()

    with open(markdown_filename[:-3] + '.html', 'w') as html_out:
        html_out.write("<style>\n" + css_text + "\n</style>\n" + html_text)

if __name__ == "__main__":
    for x in list(filter(lambda filename: filename.endswith(".md"), os.listdir())):
        if x != "README.md":
            convert_to_html(x)