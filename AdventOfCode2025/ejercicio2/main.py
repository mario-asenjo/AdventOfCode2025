from math import ceil
from operator import indexOf

''' PRIMERA ESTRELLA
def main() -> None:
    count = 0
    with open("input", 'r') as file:
        for line in file:
            line = line.split(",")
            for range_str in line:
                splitted = range_str.split('-')
                for num in range(int(splitted[0]), int(splitted[1])):
                    num_str = str(num)
                    if num_str[0:ceil(len(num_str)/2)] == num_str[ceil(len(num_str)/2):]:
                        count+=num
    print(count)
'''

'''
SEGUNDA ESTRELLA
'''
def main() -> None:
    count = 0
    with open("input", 'r') as file:
        for line in file:
            for range_str in line.split(","):
                inicio, fin = range_str.split('-')
                for num in range(int(inicio), int(fin) + 1):
                    if se_repite_mas_de_dos(num):
                        count += num
    print(count)

def se_repite_mas_de_dos(n) -> bool:
    n_str = str(n)
    n_len = len(n_str)

    for pattern in range(1, n_len // 2 + 1):
        if n_len % pattern == 0:
            val = n_len // pattern
            if val >= 2:
                g_pattern = n_str[:pattern]
                if g_pattern * val == n_str:
                    return True
    return False

if __name__ == "__main__":
    main()