input_list=["amit","learning","python","machine learning","data science","deep learning",["ahmed","raafat"],["good","job"]]
item=input("what do you need to remove ")
added=input("what do you need to add")
if item in input_list[-1]:
    input_list[-1].remove(item)
    input_list.append(added)
    print(input_list)
elif item in input_list[-2]:
    input_list[-2].remove(item)
    input_list.append(added)
    print(input_list)    
else:
    input_list.remove(item)
    input_list.append(added)
    print(input_list)    