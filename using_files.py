with open('xmen.txt', 'w+') as my_file:
    my_file.write('Beast\n')
    my_file.write('Pheonix\n')
    my_file.writelines([
        'Cyclops\n',
        'Bishop\n',
        'Nightcrawler'
    ])

my_file = open('xmen.txt', 'r')
with my_file:
    print(my_file.read())
    print("I'm reading again")
    my_file.seek(0)
    print(my_file.read())