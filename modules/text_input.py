def get_text():
    
    print("\nPaste your text (press Enter twice to finish):\n")
    
    lines = []
    
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = " ".join(lines)
    
    return text