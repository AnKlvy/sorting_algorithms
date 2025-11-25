#        *
#       * *
#      *   *
#     * * * *
def triangle(n):
    odd = 0
    for i in range(n):
        if i != n - 1:
            if i > 1:
                odd += 1
            print((n - i - 1) * ' ' + '*' + (i + odd) * ' ' + ('*' if i != 0 else ''))
        else:
            print('* ' * n)

# triangle(5)

def triangle2(n):
    odd = n*2-3
    for i in range(n):
        if i > 0:
            if i < n:
                odd -= 1
            print(i * ' ' + '*' + (odd - i) * ' ' + ('*' if i != n-1 else ''))
        else:
            print('* ' * n)

# triangle2(5)

# *
# **
# * *
# *  *
# *   *
# ******
def triangle3(n):

    for i in range(n):
        if i != n-1 or i == 0:
            print('*' + (i-1) * ' ' + ('*' if i!=0 else ''))
        else:
            print('*' * n)
triangle3(7)