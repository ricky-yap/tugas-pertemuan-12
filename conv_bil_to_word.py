''' PROGRAM KONVERSI ANGKA KE KATA dalam bahasa Inggris
Dibuat oleh : Ricky - 20SI2 - 03081200006
'''

ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
tens = {2:'twent', 3:'thirt', 4:'fourt', 5:'fift', 6:'sixt', 7:'sevent', 8:'eight', 9:'ninet'}

def written(x):
    if x <= 10:             # 0 - 9 (base numbers)
        return ones[x]
    elif x >= 1_000_000_000:# 1 000 000 000 - 999 999 999 999
        return written(x // 1_000_000_000) + ' billion ' + (written(x % 1_000_000_000) if x % 1_000_000_000 != 0 else '')
    elif x >= 1_000_000:    # 1 000 000 - 999 999 999 
        return written(x // 1_000_000) + ' million ' + (written(x % 1_000_000) if x % 1_000_000 != 0 else '')
    elif x >= 1000:         # 1 000 - 999 999
        return written(x // 1000) + ' thousand ' + (written(x % 1000)  if x % 1000 != 0 else '')
    elif x >= 100:          # 100 - 999
        return written(x // 100) + ' hundred ' + (written(x % 100) if x % 100 != 0 else '')
    elif x >= 20:           # 20 - 99
        return tens.get(x // 10) + 'y ' + (written(x % 10) if x % 10 != 0 else '')
    elif 13 <= x <= 19:     # 13 - 19
            return tens.get(x % 10) + 'een'
    else:                   # 11 and 12
        if x == 11:
            return 'eleven'
        if x == 12:
            return 'twelve'

# user input       
import os
while True: 
    os.system('clear')

    try:
        print(' CONVERTING NUMBER TO WORDS ')
        print(' -------------------------- ')
        print()

        user = int(input('Input a number : '))

    except ValueError:
        print('>>> Error : Number must be an integer')
    except Exception as e:
        print()
        print(f'>>> Error : {e}')
    
    else:
        print(f'{user} = {written(user)}')
    
    finally:
        repeat = input('Go for another round? [Y/N] :  ')
        if 'n' in repeat.casefold():
            break
  
print('Thank You For Using!')
print()