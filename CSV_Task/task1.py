'''
1. Split a.csv to a1.csv and a2.csv
2. Combine a1.csv and a2.csv to b.csv
'''
import pandas as pd


def split_data(file):
    data = pd.read_csv(file)
    print('Splitting csv file')
    a1, a2 = data.iloc[:, :3], data.iloc[:, 3:]
    a2.columns = ['1', '2', '3']
    a1.to_csv('a1.csv', index=False)
    a2.to_csv('a2.csv', index=False)
    print('Done!')
    return True


def check_csv():
    lst = ['a.csv', 'a1.csv', 'a2.csv']
    for item in lst:
        print(item)
        curr = pd.read_csv(item)
        print(curr.head())
        print('--------------')
    return True


def combine_data(file1, file2):
    f1 = pd.read_csv(file1)
    f2 = pd.read_csv(file2)
    f2.columns = ['4', '5', '6']
    print('Combining files')
    b = pd.concat([f1, f2], axis=1)
    b.to_csv('b.csv', index=False)
    print('Combining done!')
    return True


if __name__ == "__main__":
    file = 'a.csv'
    split_data(file)
    check_csv()
    combine_data('a1.csv', 'a2.csv')
    b = pd.read_csv('b.csv')
    print('b.csv')
    print(b.head())
