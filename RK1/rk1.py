from operator import itemgetter

class Book:
    def __init__(self, id, name, shop_id, page):
        self.id = id
        self.name = name
        self.shop_id = shop_id
        self.page = page

class Shop:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class BookInShop:
    def __init__(self, book_id, shop_id):
        self.book_id = book_id
        self.shop_id = shop_id

shops = [
    Shop(1, 'Библио-Глобус'),
    Shop(2, 'Читай - Москва'),
    Shop(3, 'Молодая гвардия'),
    Shop(4, 'Книжный лабиринт'),
    Shop(5, 'Читай - город'),
]

books = [
    Book(1, 'Преступление и наказание', 2, 200),
    Book(2, 'Вишневый сад', 3, 150),
    Book(3, 'Война и мир 1 том', 1, 450),
    Book(4, 'Война и мир 2 том', 5, 300),
    Book(5, 'Война и мир 3 том', 5, 200),
    Book(6, 'Капитанская дочка', 4, 100),
    Book(7, 'Евгений Онегин', 1, 250),
    Book(8, 'Мертвые души', 3, 350),
]

booksinshops = [
    BookInShop(1,2),
    BookInShop(2,3),
    BookInShop(3,1),
    BookInShop(4,5),
    BookInShop(5,5),
    BookInShop(6,4),
    BookInShop(7,1),
    BookInShop(8,3),
]


def main():
    one_to_many = [(b.name, b.page, s.name) 
        for s in shops
        for b in books
        if b.shop_id==s.id]
    

    many_to_many_temp = [(s.name, bs.shop_id, bs.book_id) 
        for s in shops
        for bs in booksinshops 
        if s.id == bs.shop_id]
    
    many_to_many = [(b.name, b.page, shop_name) 
        for shop_name, shop_id, book_id in many_to_many_temp
        for b in books if b.id==shop_id]


    print('Задание Е1\n')
    res_11 = list(filter(lambda i:i[2].find('Читай')!=-1, one_to_many))
    print(res_11)
    print('\nЗадание Е2\n')
    res_12_unsorted = []
    for d in shops:
        d_Books = list(filter(lambda i: i[2]==d.name, one_to_many))
        if len(d_Books) > 0:
            d_Books_page = [page for _,page,_ in d_Books]
            d_page_avg = round(sum(d_Books_page)/len(d_Books_page), 2)
            res_12_unsorted.append((d.name, d_page_avg))
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)
    print('\nЗадание Е3\n')
    print(list(filter(lambda i: i[0].find('В') != -1, many_to_many)))

if __name__ == '__main__':
    main()



    
