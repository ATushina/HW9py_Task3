import sys
def select_action():
     try:
         action = int(input('Что вы хотите сделать? 1 - найти контакт, 2 - создать новый контакт: '))
         while action not in (1, 2):
             action = int(input('Что вы хотите сделать? 1 - найти контакт, 2 - создать новый контакт: '))
     except:
         print('Некорректный ввод, программа завершена')
         sys.exit()
     return action