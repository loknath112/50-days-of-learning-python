#problem.2
letter = '''Dear <|Name|>
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "LOKI").replace("<|Date|>", "13 november 2026"))





#write a program to detect double space in a string

name = "loki is a good boy"#if we use double spance during typing this 
#time  will be detected by the program
print(name.find("  "))  # This will return the index of the first occurrence of double space, or -1 if not found    
