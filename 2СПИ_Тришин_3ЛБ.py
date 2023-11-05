def main():

    # 1 задача
    a = input()
    while a != "":
        print(len(a))
        a = input(" ")

    # 2 задача
    a = float(input())
    g = 0
    while a <= 36.6:
        if a <= 0:
            g += 1
            a = float(input())
    print(g)

    # 4 задача
    g = input().split()
    d = int(g[0])
    v = len(g)
    n = 0
    while n != v:
        if int(d) > int(g[n]):
            d = int(g[n])
        else:
            pass
        n += 1
    print(d)

    # 5 задание
    while True:
        a = int(input())
        if a == 0:
            break
        elif a % 3 == 0 and a % 7 == 0:
            print('Караул!')
        elif a % 3 == 0:
            print('Несчастливое')
        elif a % 7 == 0:
            print('Опасное')
        else:
            print(a)

    # 8 задание
    a = input().split()
    b = a[0]
    c = len(a) - 1
    n = 0
    while n != c:
        if len(b) > len(a[n]):
            b = a[n]
        else:
            pass
        n += 1
    print(b)

    # 9 задание
    h = input()
    if h == 'стоп':
        exit()
    h = int(h)
    n = ''
    while True:
        r = input()
        if r == 'стоп':
            break
        elif r in '+-/*':
            n = r; continue
        elif n == '+':
            h += int(r)
        elif n == '-':
            h -= int(r)
        elif n == '/':
            h /= int(r)
        elif n == '*':
            h *= int(r)
    print(int(h))

    # 10 задание
    phrase = ''
    while True:
        q = input()
        if q == 'стоп': break
        phrase += q + ' '
    phrase = phrase.split('!')
    for str in phrase:
        if str.strip() != '':
            print(f'{str.strip()}!')

if __name__ == "__main__":
    main()


