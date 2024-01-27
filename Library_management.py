
#    *** PYTHON PROGRAM FOR LIBRARY MANAGEMENT  ***        


class book:
    def __init__(self,book_id,book_name,author):
        self.book_id=book_id
        self.book_name=book_name
        self.author=author
        self.borrowed=False


class member:
    def __init__(self,member_id,member_name,phone_number,subscription=True):
        self.member_id=member_id
        self.member_name=member_name
        self.subscription=subscription
        self.phone_number=phone_number
        self.borrowed_books=[]

    def borrow_book(self, book):
        if self.subscription and not book.borrowed:  #if subscription is active and book is available
            book.borrowed = True
            self.borrowed_books.append(book)
            return True  #returns that boorowing is successful
        else:
            return False   #returns that boorowing is unsuccessful
        
    def return_book(self,book):
        if book in self.borrowed_books:
            book.borrowed=False
            self.borrowed_books.remove(book)
            return True
        else:
            return False
        

class Library:
    def __init__(self):
        self.books=[]
        self.members=[]
    
    def add_books(self,book_name):
        self.books.append(book_name)

    def add_members(self,member_name):
        self.members.append(member_name)

    def books_display(self):
        available_books = [book for book in self.books if not book.borrowed]
        for book in available_books:
            print(book)

    def remove_subscription(self,member_name):
        self.members.remove(member_name)



#initializing books
book1=book(1234,"FIRE WINGS","A.P.J.ABDUL KALAM")
book2=book(123456,"LOST WINGS","CHETAN BHAGAT")
book3=book(3455,"TURN BACK","NAVAL RAVIKANT")
book4=book(7689,"ANGEL WITHOUT WINGS","GEETHA")

#initializing members
member1=member(1091,"DEVARATHA",9999999999)
member2=member(1095,"VARADHA",8888888888)
member3=member(1097,"RADHARAMA",7777777777)
member4=member(2001,"AARYA",4536382739)

#creating library object
library=Library()

#adding books and members into library
library.add_books(book1)
library.add_books(book2)
library.add_books(book3)
library.add_books(book4)

library.add_members(member1)
library.add_members(member2)
library.add_members(member3)
library.add_members(member4)

#to print available books
Library.books_display()


# Member borrowing a book
borrow= member1.borrow_book(book1)
if borrow:
    print(f"{member1} borrowed {book1}")
else:
    print(f"{member1} can't borrow {book1}")

# Member returning book  
book_return= member1.return_book(book1)
if book_return:
    print(f"{member1} returned {book1}")
else:
    print(f"{member1} cannot return {book1}")




    






    


