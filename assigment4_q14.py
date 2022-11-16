#Program to find multipale character in the string
string =input("Enter a multicharacter string : ")
duplicates = []
for char in string:
    if string.count(char) > 1:
        if char not in duplicates:
                duplicates.append(char)
print(*duplicates)
