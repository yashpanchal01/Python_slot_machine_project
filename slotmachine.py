def print_hellow(**kwargs):
    a = kwargs.items()
    return a[0]

balance = print_hellow(word = 'Hellow')
print(balance)