def even(n):
    print("The even number are.....")
    ans=2
    while(ans<=n):
        print(ans)
        ans=ans+2
if __name__=="__main__":
    n=int(input("Enter the range in which you want even numbers:"))
    even(n)
