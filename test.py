try:
    if '2' + 2 == 4:
        raise ValueError
    else:
        print('same')
except ValueError:
    print('ValueError')
except:
    print('NameError')