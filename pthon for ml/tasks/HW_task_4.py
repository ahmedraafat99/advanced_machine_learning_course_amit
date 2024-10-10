def decoded_message(encoded_message):
    core_message=encoded_message.strip("#@!$*789")
    first_word,second_word=core_message.split()
    encoded_first_word=first_word[::-1]
    vowel_replacement={"E":"A","U":"O"}
    encoded_second_word=''.join(vowel_replacement.get(char,char)for char in second_word)
    decoded_message= f"{encoded_first_word} {encoded_second_word}"
    return decoded_message

encoded_message="##$$$@!yalpstcejorp EPUVT****9887"
print(decoded_message(encoded_message))