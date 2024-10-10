def decoded_message(encoded_message):
    core_message=encoded_message.strip("&&&**$!!@1234")
    first_word,second_word=core_message.split()
    decode_first_message= first_word[::-1]
    vowel_replacement={"I":"E","O":"U"}
    #need to explain this
    decode_second_message=''.join(vowel_replacement.get(char,char)for char in second_word)
    decoded_message=f"{decode_first_message} {decode_second_message}"
    return decoded_message
encoded_message="&&&**$gnirtS PLIO!!@1234"
print(decoded_message(encoded_message))