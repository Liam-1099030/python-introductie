age_str = input('What is your age? ')
print(f'Your age is {age_str}')


wifi = input('Welke verbinding wilt u gebruiken? [4G, 5G, Wifi open] ')
if wifi == '4G':
    print(f'U bent verbonden via {wifi}!')

if wifi == '5G':
    print(f'U bent verbonden via {wifi}!')

if wifi == 'Wifi open':
    print('U heeft de voor de Wifi open gekozen, wij wijzen u erop dat de data door de eigenaar van dit netwerk is te lezen.')
    confirm = input('Wilt u nog verbinden? [Ja, Nee]')
    if confirm == 'Ja':
        print(f'U bent verbonden via {wifi}!')

    if confirm != 'Nee':
        print('U bent niet verbonden!')

    if confirm != 'Nee' or confirm != 'Ja':
        print('U bent niet verbonden!')