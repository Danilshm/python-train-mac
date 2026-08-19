banana = "banana"
banana_center = banana.center(10,'$') # 10 is the length of the string
print(banana_center)
sentence = "value is the substring which is to be searched in the string"
sentence_count = sentence.count("value", 0,20)
sentence_count_2 = sentence.count("is")
print(sentence_count)
print(f"There is {sentence_count_2} is")