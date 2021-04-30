class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return f'{self.title} by {self.author}'
    def __len__(self):
        return self.pages
    def __del__(self):
        print('a book object is deleted')
b=Book('python','jose',200)
print(b)
print(str(b))
print(len(b))

# delete variable from memory   del b
del b