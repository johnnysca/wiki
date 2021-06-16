import marko  # type:ignore
import re


def formatter(markdown_txt):
    """
    Formats markdown txt into html using Marko parser

    Calls external library to convert a given text written in markdown into html.
    Uses Marko library to parse text and map appopriate tags.  Also calls
    method to remove tags that may already exist in the text to ensure
    proper template rendering - this may change slightly.

    Args:
        markdown_txt: String input that is parsed and converted to html
        TODO: Create method or branch to handle opening files and reading their text

    Returns:
        String reformated to fit html syntax for rendering templates
    """
    removed_tag_txt = remove_tags(markdown_txt)
    html_txt = marko.convert(removed_tag_txt)
    return html_txt


def remove_tags(str1):
    """
    Removes html tags using regular expression library

    Uses python reg exp library to reformat the string and remove any html tags.
    Temporary solution for script injections.  TODO: branch for formatting only
    certain unaccepted tags since markdown also accepts html

    Args:
        str1: String whose tags will be removed

    Returns:
        Reformatted string with tags removed
    """
    taged_string = re.compile(r"<[^>]+>")
    return taged_string.sub("", str1)


def split_name(name):
    result = name
    upper_cases = re.search(r"^([^A-Z]*[A-Z]){2}", result)
    return (
        result[0 : upper_cases.span()[1] - 1]
        + " "
        + result[upper_cases.span()[1] - 1 :]
    )
