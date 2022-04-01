import calc_2
import view 
dictionary = \
    {
        "+" :calc_2.sum,
        "-" :calc_2.dif,
        "*" :calc_2.mult,
        "/" :calc_2.div,
        "**":calc_2.pow
    }
oper = input('Введите оператор: ')
rez = round(calc_2.init(dictionary[oper],view.a,view.b),10) # передаем операцию и ее значения из view/в словарь вводим значени котрое ввел пользовател 
if rez - int(rez) == 0: #проверка целочисленное число 
    rez = int(rez)
print(f'Результат операции равен {rez}')
