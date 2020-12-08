n=int(input("Cate alune sunt"))
if n%3==0:
    print("Fiecarui purcel i-au revenit cate ",n//3,"aluna")
    print("Rita i-a revenit 0 alune")
else:
    print("Fiecarui purcel i-au revenit cate ",n//3,"aluna")
    print("Rita i-au revenit",n-(3*(n//3)),"alune")