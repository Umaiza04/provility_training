#managing student marks using list
marks=[75, 80, 90, 80, 75, 85]
print(marks)
total=len(marks)
print(total)

#conversion from list to tuple
tuple1=tuple(marks)
print(tuple1)

#printing the highest number
print(max(tuple1))

#conversion from tuple to set
set1=set(marks)
print(set1)
num_marks=len(set1)
print(num_marks)

#dictionary creation
dict={"alice" : 75,"bob" : 80, "charlie" : 90,"david" : 80,"eva" : 75, "frank" : 85}
print(dict)
#printing charlie mark
print(dict["charlie"])
#updating bob's mark
dict["bob"]=88
print(dict)

#printing the updated dictionary
print(dict)


