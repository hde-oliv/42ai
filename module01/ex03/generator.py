def generator(text, sep=" ", option=None):
    """\
    Splits the text according to sep value and yield the substrings.\
    option precise if a action is performed to the substrings before it is yielded
    """
    if not isinstance(text, str) or option not in [None, "shuffle", "unique", "ordered"]:
        yield "ERROR"

    splitted_text = text.split(sep)

    if option == 'shuffle':
        splitted_text = set(splitted_text)
    elif option == 'unique':
        unique = []
        for word in splitted_text:
            if word not in unique:
                unique.append(word)
        splitted_text = unique
    elif option == 'ordered':
        splitted_text = sorted(splitted_text)
    for word in splitted_text:
        yield word
