def main():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    x = set(a) & set(b)
    print(list(x))

if __name__ == '__main__':
    main()