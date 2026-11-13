#problem.2
letter = '''Dear <|Name|>
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "LOKI").replace("<|Date|>", "13 november 2026"))