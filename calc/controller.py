# импортировали в контролер модули 
import model_dif as model # импорт  модуль сложения вычетания и тд 
import view #импорт представления 
# тут мы опишем метод нажатия на кнопку для пользователя 
def button():
    #model_sum.init(get_value)#сюда должны прийти значения из view - то с чем взаимодействует пользователь 
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a,value_b)#инициализация входных данных и передача  аргуметов 
    result = model.do_it() # !!! не забывай про скобки !!!
    view.view_data(result, " result ")# передаем метод из view
#теперь это надо как то заставить работать ?
# надо создать точку входа(main- фаил)