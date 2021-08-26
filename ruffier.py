txt_index = "Ваш индекс Руфье: "
txt_workheart = "Работоспособность сердца: "
txt_nodata = '''
   нет данных для такого возраста'''
txt_res = []
txt_res.append('''низкая.
   Срочно обратитесь к врачу!''')
txt_res.append('''удовлетворительная.
   Обратитесь к врачу!''')
txt_res.append('''средняя.
   Возможно, стоит дополнительно обследоваться у врача.''')
txt_res.append('''
   выше среднего''')
txt_res.append('''
   высокая''')
 
def ruffier_index(P1, P2, P3):
    ''' возвращает значение индекса по трем показателям пульса для сверки с таблицей'''
    return (4 * (P1+P2+P3) - 200) / 10
 
def neud_level(age):
    ''' варианты с возрастом меньше 7 и взрослых надо обрабатывать отдельно,
    здесь подбираем уровень "неуд" только внутри таблицы:
    в возрасте 7 лет "неуд" - это индекс 21, далее каждые 2 года он понижается на 1.5 до значения 15 в 15-16 лет '''
    norm_age = (min(age, 15) - 7) // 2  # каждые 2 года разницы от 7 лет превращаются в единицу - вплоть до 15 лет
    result = 21 - norm_age * 1.5 # умножаем каждые 2 года разницы на 1.5, так распределены уровни в таблице
    return result
  
def ruffier_result(r_index, level):
    ''' функция получает индекс Руфье и интерпретирует его,
    возвращает уровень готовности: число от 0 до 4
    (чем выше уровень готовности, тем лучше).  '''
    if r_index >= level:
        return 0
    level = level - 4 # это не будет выполняться, если мы уже вернули ответ "неуд"
    if r_index >= level:
        return 1
    level = level - 5 # аналогично, попадаем сюда, если уровень как минимум "уд"
    if r_index >= level:
        return 2
    level = level - 5.5 # следующий уровень
    if r_index >= level:
        return 3
    return 4 # здесь оказались, если индекс меньше всех промежуточных уровней, т.е. тестируемый крут.
    
def test(P1, P2, P3, age):
    ''' эту функцию можно использовать снаружи модуля для подсчетов индекса Руфье.
    Возвращает готовые тексты, которые остается нарисовать в нужном месте
    Использует для текстов константы, заданные в начале этого модуля. '''
    if age < 7:
        return (txt_index + "0", txt_nodata) # тайна сия не для теста сего
    else:
        r_index = ruffier_index(P1, P2, P3) # расчет
        result = txt_res[ruffier_result(r_index, neud_level(age))] # интерпретация, перевод числового уровня подготовки в текстовые данные
        return (txt_index + str(r_index), txt_workheart + result) # возвращаем кортеж из двух строк для вывода человеку
# Модуль для расчета результатов

# Здесь должен быть твой код