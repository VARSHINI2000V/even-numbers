def even(n):
    print("The even number are.....")
    for i in range(n):
        if i%2==0:
            print(i)

if __name__=="__main__":
    n=int(input("Enter the range in which you want even numbers:"))
    even(n)