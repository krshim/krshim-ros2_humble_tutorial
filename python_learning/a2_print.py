def main():
    a=10
    b=5
    print("hello, world", end = "ENDSTRING")
    print("hello, world")
    print("this is","12", sep="\t", )
    print("hello, world")

    print("variable a is =", a)
    print("variable a is {1}, b is {0}".format(a,b))
if __name__ == "__main__":
    main()
    #f-string
    print(f"variable a is {a}, b is {b}")