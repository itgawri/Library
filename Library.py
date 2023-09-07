hamlet_info = ("William Shakespeare", "Tragedy", 1603)
martian_chronicles_info = ("Ray Bradbury", "Science fiction", 1950)
my_books = {"Hamlet": hamlet_info, "The Martian Chronicles": martian_chronicles_info}
print(f"My books: {my_books}")

my_books["Fahrenheit 451"] = ("Ray Bradbury", "Dystopian", 1953)
print(f"Fahrenheit 451 info: {my_books['Fahrenheit 451']}")

my_books_authors = set()

for book in my_books:
    book_info = my_books[book]
    author = book_info[0]
    my_books_authors.add(author)
print(f"Authors: {my_books_authors}")

is_my_author = "Ray Bradbury" in my_books_authors

if is_my_author:
    print("Ray Bradbury belongs to my authors!")

# PL-------------------------------------------------------------------

informacje_o_hamlecie = ("William Shakespeare", "Tragedia", 1603)
informacje_o_Kronikach_Marsa = ("Ray Bradbury", "Science fiction", 1950)
moje_ksiazki = {"Hamlet": informacje_o_hamlecie, "Kroniki Marsa": informacje_o_Kronikach_Marsa}
print(f"Moje książki: {moje_ksiazki}")

moje_ksiazki["Fahrenheit 451"] = ("Ray Bradbury", "Dystopia", 1953)
print(f"Informacje o Fahrenheit 451: {moje_ksiazki['Fahrenheit 451']}")

autorzy_moich_ksiazek = set()

for ksiazka in moje_ksiazki:
    informacje_o_ksiazce = moje_ksiazki[ksiazka]
    autor = informacje_o_ksiazce[0]
    autorzy_moich_ksiazek.add(autor)
print(f"Autorzy: {autorzy_moich_ksiazek}")

czy_moj_autor = "Ray Bradbury" in autorzy_moich_ksiazek

if czy_moj_autor:
    print("Ray Bradbury należy do moich autorów!")
