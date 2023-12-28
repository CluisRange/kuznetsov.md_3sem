def formock():
    path = "res\primer_faila.txt"
    with open(path, 'r') as a:
        contents = a.read()
    print(contents)
if __name__ == "__main__":
    formock()