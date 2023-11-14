words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
min_len = 6
def check_len(word):
    return len(word)>min_len
#op=check_len([0])
#print(op)
op=list(filter(check_len,words))
print(op)
