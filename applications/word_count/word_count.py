import re
def word_count(s):
    counts = {}
    s = s.translate(str.maketrans({",":"",".":"",'"':''}))
    s = s.split()
    for i in s:
        i = str.lower(i)
        if i not in counts.keys() and i.islower():
            counts[i] = 1
        elif i in counts.keys():
            counts[i]+=1
        else:
            pass
    return counts



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))