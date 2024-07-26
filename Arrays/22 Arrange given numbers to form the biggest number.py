from functools import cmp_to_key
ar = ["54", "546", "548", "60"]
def comp (a,b):
    if a+b>b+a:
        return -1
    else:
        return 1
ar.sort(key=cmp_to_key(comp))
print(*ar,sep='')