def field(items, *args):
    assert len(args) > 0
    for i in items:
        if(len(args) == 1):
            yield i.get(args[0])
        else:
            dict = {}
            for j in args:
                if(i.get(j)!=None): dict[j]=i.get(j)
            yield dict

def zapusk(data, str):
    a=[]
    for i in field(data, str):
        a.append(i)
    return a
def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    for i in field(goods, 'title', 'price'):
        print(i, end='\n')
