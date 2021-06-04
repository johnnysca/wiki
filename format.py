import marko  # type:ignore
import re


def formatter(markdown_txt):
    removed_tag_txt = remove_tags(markdown_txt)
    html_txt = marko.convert(removed_tag_txt)
    return html_txt


def remove_tags(str1):
    taged_string = re.compile(r"<[^>]+>")
    return taged_string.sub("", str1)
