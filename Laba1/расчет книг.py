# TODO Найдите количество книг, которое можно разместить на дискете
byte_size = 1.44 * 1024 ** 2
book_size = 100 * 50 * 25 * 4
num = byte_size // book_size
print("Количество книг, помещающихся на дискету:", int(num))
