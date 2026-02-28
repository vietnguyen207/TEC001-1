import re

def redact_phone_numbers(text):
    # Pattern explanation:
    # \b\d{10}\b  → exactly 10 digits
    # \+84\d+     → starts with +84 followed by digits
    pattern = r'(\b\d{10}\b|\+84\d+)'
    redacted_text = re.sub(pattern, '[REDACTED]', text)
    
    return redacted_text


paragraph = input("Enter a paragraph that have phone number: ")
result = redact_phone_numbers(paragraph)
print(result)