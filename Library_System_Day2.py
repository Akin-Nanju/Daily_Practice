def list():
    books = ["MHA", "ONE PIECE", "12 WAYS", "HARRY POTTER", "THE ODYSSEY"]
    return books

def implementation():
    book_list = list()
    print("1. AVAILABLE BOOKS\n2. BORROW BOOKS\n3. RETURN A BOOK\n4. EXIT")
    print("")
    choice = int(input("ENTER YOUR CHOICE among 1,2,3,4: "))
    if choice == 1:
        print("THE LIST OF BOOKS ARE: ")
        for i in book_list:
            print(i, end=',')
    if choice == 2:
        borrow = input("WHICH BOOK DO YOU WANT TO BORROW?: a,b,c,d,e")
        if borrow == 'a':
            print(f"YOU BORROWED '{book_list[0]}'")
        if borrow == 'b':
            print(f"YOU BORROWED '{book_list[1]}'")
        if borrow == 'c':
            print(f"YOU BORROWED '{book_list[2]}'")
        if borrow == 'd':
            print(f"YOU BORROWED '{book_list[3]}'")
        if borrow == 'e':
            print(f"YOU BORROWED '{book_list[4]}'")
    if choice == 3:
        borrow = input("WHICH BOOK DO YOU WANT TO RETURN?: a,b,c,d,e")
        if borrow == 'a':
            print(f"YOU RETURNED '{book_list[0]}'")
        if borrow == 'b':
            print(f"YOU RETURNED '{book_list[1]}'")
        if borrow == 'c':
            print(f"YOU RETURNED '{book_list[2]}'")
        if borrow == 'd':
            print(f"YOU RETURNED '{book_list[3]}'")
        if borrow == 'e':
            print(f"YOU RETURNED '{book_list[4]}'")
    if choice == 4:
        print("THANK YOU FOR VISITING")

def end():
    print("THANK YOU FOR VISITING")

list()
implementation()
end()
