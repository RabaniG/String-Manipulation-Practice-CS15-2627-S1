string_to_process = "   sMitH, aLeX    "

# Remove whitespace
name_parts = string_to_process.strip()

# Split the string into last name and first name
name_parts = name_parts.split(",")

# Capitalize the first letter of each name
last_name = name_parts[0].strip().title()
first_name = name_parts[1].strip().title()

print(first_name + " " + last_name)