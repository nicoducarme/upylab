def trans(text, replaceA, replaceB):
    newText = ""
    for c in text:
        if c == replaceA[0]:
             newText += replaceA[1]
        elif c == replaceB[0]:
             newText += replaceB[1]
        else:
            newText += c
    return newText
