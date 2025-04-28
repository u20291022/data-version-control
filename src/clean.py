from numpy import delete, loadtxt, ndarray, savetxt

FILE_PATH = "data/raw/9.csv"

data: ndarray = loadtxt(FILE_PATH, dtype=str, delimiter='\t', encoding='utf-8')
empty_rows_indexes = []

for index, row in enumerate(data):
    if row[0].strip() == "" or row[1].strip() == "":
        empty_rows_indexes.append(index)

data = delete(data, empty_rows_indexes, axis=0)
savetxt(FILE_PATH, data, fmt='%s', delimiter='\t', encoding='utf-8')
