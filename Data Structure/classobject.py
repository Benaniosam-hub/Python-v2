class Book:
    
    def __init__(self,title,author,total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages

    def get_info(self):
        return f" '{self.title}' by {self.author} ({self.total_pages} pages) "

    def read_pages(self,current_page):
       
       return f"Current progress: {current_page}/{self.total_pages}"



my_book = Book("The Hobbit", "J.R.R Tolkien", 310)

print(my_book.get_info())

print(my_book.read_pages(50))

