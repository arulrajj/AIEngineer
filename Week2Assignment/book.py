from datetime import datetime
class Book:

    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_age_of_book(self):
        current_year = datetime.now().year
        return current_year - self.publication_year
    


book1 = Book("Python basics", "John Doe", 2000)
print("Age of the book is: ",book1.get_age_of_book(), "years")
