string_to_process = "t H e , T a L e :: O f , T w O :: c I t I e S"

# Remove ::
text = string_to_process.replace("::", "|")
text = text.replace(",", "|")
# print(text)

# Split the string into parts
title_parts = text.split("|")
title_words = []

# Remove spaces between letters, then capitalize each word
for part in title_parts:
    # remove spaces between letters
    word = "".join(part.split())

    # capitalize the first letter of each word
    title_words.append(word.title())

formatted_title = " ".join(title_words)
print(formatted_title)