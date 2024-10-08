code = input("enter your encoded message").strip("#!@6789").split('E')
first_word= code[0][::-1]+"e"
second_word=code[1]
decode= f"{first_word} {second_word}"
print(decode)