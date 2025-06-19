from .mtx import *

# Тема -> Функция -> Задание
def description(
    dict_to_show=themes_list_funcs,
    key=None,
    show_only_keys: bool = False,
    show_keys_second_level: bool = True,
    n_symbols: int = 32,
    to_print: bool = True,
    show_doc = False):
    """
    Форматированный вывод информации о функциях и заданиях из словарей тем.

    Parameters
    ----------
    dict_to_show : str or dict, optional
        Имя словаря тем или сам словарь вида {функция: задание}.
        По умолчанию используется `themes_list_funcs`.
    key : hashable, optional
        Ключ для фильтрации конкретного элемента словаря.
    show_only_keys : bool, optional
        Если True - показывать только ключи словаря.
    show_keys_second_level : bool, optional
        Если True - показывать ключи второго уровня (названия функций).
    n_symbols : int, optional
        Максимальное количество символов описания для отображения.
    to_print : bool, optional
        Если True - выводить результат через print(), иначе вернуть как строку.
    show_doc : bool, optional
        Если True - выводить результат поиска функции по теме и названию вместе с ее докстрингом. Иначе без.
    Returns
    -------
    str or None
        Форматированная строка с информацией (если to_print=False).
        При to_print=True возвращает None, выводя результат напрямую.

    Notes
    -----
    1. Функция поддерживает два режима работы:
       - При передаче строки в dict_to_show: использует предопределенные словари тем
       - При передаче словаря напрямую: работает с пользовательскими структурами
    2. Использует вспомогательную функцию invert_dict() для преобразования словарей.
    3. При обработке описаний автоматически добавляется перенос строк для длинных текстов.
    4. В случае ошибок при извлечении описаний (например, отсутствующий ключ) - пропускает проблемные элементы.

    Examples
    --------
    >>> description('math_operations', show_only_keys=True)
    Сложение  : 
    Вычитание : 
    Умножение : 

    >>> description('data_processing', n_symbols=50)
    clean_data   : Очистка данных от пропусков...
    analyze_data : Проведение статистического анализа...

    >>> description('api_calls', key='get_request')
    get_request : Выполняет GET-запрос к API с параметрами...

    References
    ----------
    .. [1] Python Software Foundation. "Python Language Reference", version 3.11.
    .. [2] Beazley, D.M. "Python Essential Reference", 4th edition.
    .. [3] Ramalho, L. "Fluent Python: Clear, Concise, and Effective Programming".
    """
    
    # Если dict_to_show - строка (название темы) и не указан конкретный ключ (key)
    if type(dict_to_show) == str and key == None:
        dict_to_show = themes_list_dicts[dict_to_show]
        dict_to_show = invert_dict(dict_to_show)
        text = ""
        length1 = 1 + max([len(x.__name__) for x in list(dict_to_show.keys())])
        
        for key in dict_to_show.keys():
            text += f'{key.__name__:<{length1}}' # Имя функции, выровненное по левому краю
            
            if not show_only_keys:
                text += ': '
                text += f'{dict_to_show[key]};\n' + ' '*(length1+2) # Описание задачи
            text += '\n'
            
        if to_print == True:
            return print(text)
        return text
    
    # Если dict_to_show - строка (название темы) и указан конкретный ключ (имя функции)
    elif type(dict_to_show) == str and key in themes_list_dicts_full[dict_to_show].keys():
        if show_doc:
            return print(themes_list_dicts_full[dict_to_show][key]) # Вывод исходного кода функции
        else:
            return print(themes_list_dicts_full_nd[dict_to_show][key]) # Вывод исходного кода функции
    
    else:
        show_only_keys = False
    text = ""
    length1 = 1 + max([len(x) for x in list(dict_to_show.keys())]) # Максимальная длина ключа первого уровня (названия темы)
    
    for key in dict_to_show.keys():
        text += f'{key:^{length1}}' # Название темы, выровненное по центру
        if not show_only_keys:
            text += ': '
            for f in dict_to_show[key]:
                text += f'{f.__name__}'
                if show_keys_second_level:
                    text += ': '
                    try:
                        # Получение описания функции из инвертированного словаря
                        func_text_len = len(invert_dict(themes_list_dicts[key])[f])
                        
                        # Форматирование описания с переносами строк и ограничением по длине
                        func_text = invert_dict(themes_list_dicts[key])[f]
                        text += func_text.replace('\n','\n'+' '*(length1 + len(f.__name__))) if func_text_len < n_symbols else func_text[:n_symbols].replace('\n','\n'+' '*(length1 + len(f.__name__)))+'...'
                    except:
                        pass # Пропуск, если описание не найдено
                text += ';\n' + ' '*(length1+2) # + '\n' + ' '*(length1+2)
        text += '\n'
        
    if to_print == True:
        return print(text)
    return text