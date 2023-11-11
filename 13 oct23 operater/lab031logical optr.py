#logical operators
#And logical And
#and gate table  i/p-T T op-T
#                    T F    F
#                    F T    F
#                    F F    F
#OR gate .table i/p- T T op-T
#                    T F    T
#                    F T    T
#                    F F    F
# Not gate table i/p- T op  F
#                     F     T
p=True
q=False
print(p and q)
print(q or p)
print(not p)