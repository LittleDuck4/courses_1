import re

phone_book = "Some phone numbers: +3898483149, +380625262, +0689810597, 0682667575, +380683423853, 3801235125, 380693875955"

print(re.findall(r"(?:\s\+380|\s380|\s0)\d{9}\b", phone_book))
