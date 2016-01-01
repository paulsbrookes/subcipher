def filter(text_in, alpha):
    filtered_text = ''
    for x in text_in.lower():
        if x in alpha:
            filtered_text += x
    return filtered_text
