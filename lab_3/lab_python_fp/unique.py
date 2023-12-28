import gen_random
class Unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.set = set()

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.items)
        if isinstance(item, str) and self.ignore_case:
            key = item.lower()
        else:
            key = item
        if key not in self.set:
            self.set.add(key)
            return key
def zapusk(data, bool):
    unique_iter = Unique(data, ignore_case=bool)
    a=[]
    for item in unique_iter:
        output = item
        if (output != None): a.append(output)
    data.clear()
    return a

def main():
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data = gen_random.gen_random(10, 1, 5)
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    unique_iter = Unique(data, ignore_case=False)
    for item in unique_iter:
        output = item
        if (output != None): print(output, end=' ')
