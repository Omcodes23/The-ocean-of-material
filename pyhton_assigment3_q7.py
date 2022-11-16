list=["Apple","Bananna","Cherry","graphs","Orange"]
list2=["h1","h2","h3","h4","h5"]
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(list[:])
print(list * 2)
print(list + list2)
list.append("Hi this ia append")
print(list)
list.extend(["UPSC","SSC","HSC"])
print(list)
list[1:4]=[15,89,78]
print(list)

#Using insert()function
list=[1,9]
list.insert(1,3)
print(list)
list[2:2]=[5,7]
print(list)

#Deleting the entire list
del list
print(list)

#Removing a given item from the list
list=['p','q','r','s','m']
list.remove('p')
print(list)

#Pop() method is used to remove an item at the given index

list.pop(1)   #Removes the item at the given index
print(list)
list.pop()  #Removes the last item if the index is not provied
print(list)

#clear()method to empty the whole list
list.clear()
print(list)

#index()method :  returms the index of the first matched item/first occurence
list=[7,8,12,15,96]
print(list.index(8))

#sort() method : sort items in a list in ascending order
list=[12,44,85,96,25,36]
list.sort()
print(list)

#reverse() method :  reverse the order of items in the list
list.reverse()
print(list)
