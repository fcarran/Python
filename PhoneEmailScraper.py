import re
import pyperclip

# Create a regex object for phone numbers
phoneRegex = re.compile(r'''
#415-111-2233, 111-2233, (415)-111-2233, 111-2233 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))? #area code (optional)
(\s|-) #fist separator
\d\d\d #first 3 digits
- #separator
\d\d\d\d #last 4 digits
(((ext(\.)?\s)|x) #extension number-part (optional)
(\d{2, 5}))? #extension number pat
)
''', re.VERBOSE) #VERBOSE allows for cleaner line spacing in a regex obj, using whitespace

# Create a regex object for emails addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+ # name part
@ # @ symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)

# TODO: Get the text off the clipboard
text = pyperclip.paste()  # gather text from clipboard

# TODO: Extract the emails/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# TODO: Copy the extracted emails/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)