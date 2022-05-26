# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename,'r') as f:
        content = f.read()
        print(content)
    
    return content
read_file_content('story.txt')
    


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    for char in '.,?':
        text = text.replace(char,' ')
    text = text.lower()
    data = text.split()
    #print(data)

    d = {}
    for word in data:
        if word in d:
            d[word] +=  1
        else:
            d[word] = 1
        d[word] += 1
    
    return  d
    #return {"as": 10, "would": 20}
print(count_words())