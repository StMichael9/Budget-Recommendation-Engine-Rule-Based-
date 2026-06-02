"""Handles:

standardizing category names

converting strings → numbers

filling missing categories

removing weird formatting"""

# Strips accidental spaces and forces text to lowercase so names match perfectly
def standardize_category(category_name):
    strip = category_name.strip().lower()
    return strip

# Converts raw spreadsheet text like "1500" into a real math-ready integer
def convert_to_number(amount_str):
    convert = int(amount_str)
    return convert

# Checks for completely blank inputs and gives them a default label like "Uncategorized"
def fill_missing_category(category_name):
    if category_name == "":
        return "uncategorized"
    return category_name

# Strips out problematic financial characters like dollar signs or commas
def remove_weird_formatting(amount_str):
    clean_text = amount_str.replace(",", "").replace("$", "")
    return clean_text
