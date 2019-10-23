

from numpy.random import uniform, seed

def search(v, x):
    # search list v for closest element to x and return index
    # DO NOT use any built-in Python functions
    # TODO
    return 0


def gaussian(u, m, s):
    # Convert the list u of uniform random deviates, to Gaussian
    # random deviates with mean m and standard deviation s
    # DO NOT use any built-in Python functions
    # TODO
    return u


def main(n, m, s):
    seed(0xc0ffee)
    u = sorted(uniform(size=n))
    print(u)
    g = gaussian(u, m, s)
    i = search(g, 0.0)   #find the index of the item closest to zero
    print(f'deviate closest to zero is {g[i]} at index {i}')



if __name__ == '__main__':
    main(100, 0, 1)
