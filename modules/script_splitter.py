def split_script(text):

    sentences = text.split(".")

    sentences = [s.strip() for s in sentences if s.strip() != ""]

    return sentences