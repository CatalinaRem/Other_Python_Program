''' --------------------------
Do not change anything here 
------------------------------'''
import P8f

''' --------------------------
Put your code for the main part here 
------------------------------'''
if __name__ == "__main__":
    n,k=input("Enter n and k: ").split()
    n=int(n)
    k=int(k)
    c1=P8f.fact(n)
    c2=P8f.fact(k)*P8f.fact(n-k)
    c3=c1/c2

    print("C(%d,%d) = %d"%(n,k,c3))