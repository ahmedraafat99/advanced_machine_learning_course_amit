input_file = open("C:/Users/DOLLAR/Desktop/Amit/advanced_machine_learning_course_amit/pthon for ml/tasks/input_file.txt", "r")
def read_count_file(input_file):


    text = input_file.read()
    input_file.close()
    text = text.replace('\n', ' ')
    words = text.split(' ')
    unique_words = set(words)
    word_counts = dict()

    for word in unique_words:
        word_counts[word] = words.count(word)
        output_file = open("output_file.txt", "w")
    for word in word_counts:
        output_file.write("{}: {}\n".format(word, word_counts[word]))
    output_file.close()    
    
    
    
read_count_file
r1=read_count_file(input_file)
print(r1)