#builtin fun
original_str="suchi"
def pallindrom(original_str):
    rev_str = original_str [::-1]
    print(rev_str)
    if original_str==rev_str:
      print("palindrom")
    else:
       print("not a palindrom")
pallindrom(original_str)


#sayHEllolambda=lambda name:print("Hii ,my name is",name)
revnum=lambda original_str: original_str [::-1]
if revnum("suchi")=="pramod":
    print("palindrome")
else:
    print("not pallindrome")