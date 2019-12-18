#! python3

import re
import pyperclip

#Create a regex for phone numbers
PhoneRegex = re.compile(r'''
((\d\d\d) | (\(\d\d\d\)))+ # Area code (optional)
(\s | -)                   # First separator
(\d\d\d)                     # First 3 digits
-                          # Second separator
(\d\d\d\d)                  # Last 4 digits
(((ext(\.)?\s) | x)        # Exstention word part (optional)
(\d{2, 5}))?               # Exstention number-part (optional)
''',re.VERBOSE)

EmailRegex = re.compile(r'''
[\w_.+]+                   # Name part
@                          # @ symbol
[\w_.+]+                   # domain part 
''',re.VERBOSE)

Document = pyperclip.paste()
ProductDocumentE = EmailRegex.findall(Document)
ProductDocumentP = PhoneRegex.findall(Document)

AllPhoneNumbers = []
for PhoneNumber in ProductDocumentP:
    AllPhoneNumbers.append(PhoneNumber[0])

    
FinalDocument = '\n'.join(str(ProductDocumentP)) + '\n' + '\n'.join(ProductDocumentE)
pyperclip.copy(FinalDocument)
print (FinalDocument)

