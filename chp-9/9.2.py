from pathlib2 import Path
def replacetext(search_text, replace_text):
    file = Path(r"doc.txt")
    data = file.read_text()
    data = data.replace(search_text, replace_text)
    file.write_text(data)
    return "Text replaced"
search_text = "ADJECTIVE"
b = str(input("Enter an adjective: "))
replace_text = b
print(replacetext(search_text, replace_text))
search_text = "NOUN1"
a = str(input("Enter a noun: "))
replace_text = a
print(replacetext(search_text, replace_text))
search_text = "VERB"
c = str(input("Enter a verb: "))
replace_text = c
print(replacetext(search_text, replace_text))
search_text = "NOUN2"
d = str(input("Enter a verb: "))
replace_text = d
print(replacetext(search_text, replace_text))
