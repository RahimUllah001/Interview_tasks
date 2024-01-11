# 9. Create a program that counts the occurrences of each word in a text document.

text = open('Interview_Tasks\sample.txt','r')

d =dict()

# remove extra spaces

for line in text:
    line = line.strip()         # remove leading spaces and new line character

    line = line.lower()

    words = line.split(" ")         # convert the lines into the words
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1


for key in d:
    print(key,":",d[key])            

text.close()
