test = "# let see if this works"

def from_md_to_html(string):
    formated_str = string.lstrip("# ")
    formated_str = f"<h1>{formated_str}</h1>"
    return formated_str

print(from_md_to_html(test))
