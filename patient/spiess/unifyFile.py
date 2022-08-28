import csv

def __main__():
    data = []
    for n in range(100):
        reader = csv.reader(open(f'Arquivos/temp_{n}.csv'))
        for l in reader:
            if l:
                data.append(l)

    wirter = csv.writer(open(f'Arquivos/Todos.csv', 'w'), csv.excel)
    wirter.writerows(data)
if __name__ == '__main__':
    __main__()