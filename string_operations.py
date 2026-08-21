banana = "banana"
# Center string
banana_center = banana.center(10,'$') # 10 is the length of the string
print(banana_center)
print("")
sentence = "value is the substring which is to be sEarchEd in tHe string value"
# Count string
sentence_count = sentence.count("value", 0,20)
sentence_count_2 = sentence.count("is")
print("there is ",sentence_count, "\"value\" from 0 to 20")
print(f"There is {sentence_count_2} \"is\"")
# Find string
sentence_find= sentence.find("is",0,10) 
sentence_find_2= sentence.find("value", 10)
print("find \"is\" from 0 to 10    ", sentence_find)
print("find \"value\" from 10      ", sentence_find_2)
#Swapcase string
sentence_swapcase= sentence.swapcase()
print(sentence_swapcase)
# startswith(True if the string starts) and endswith(returns True if the string endswith)
sentence_startwith= sentence.startswith("value",61)
print("start with \"value\" in the index 61?",sentence_startwith)
sentence_endwith=sentence.endswith("banana")
print("end with \"banana\"?",sentence_endwith)