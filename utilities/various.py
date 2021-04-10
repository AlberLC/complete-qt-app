import operator
import re
from datetime import date, datetime
from unicodedata import normalize as normalize_

EXACT_MATCH = 2
IN_RANGE_MATCH = 1
NO_MATCH = 0

operators = {
    '=': operator.eq,
    '<': operator.lt,
    '<=': operator.le,
    '=<': operator.le,
    '>': operator.gt,
    '>=': operator.ge,
    '=>': operator.ge
}


def clip_string_list(string_list):
    for i, string in enumerate(string_list):
        string_list[i] = string[:4]
    return ', '.join(string_list)


def color_gray(string):
    return f'<font color="#555555">{string}</font>'


def color_red(string):
    return f'<font color="#FF3300">{string}</font>'


def color_red_line(widget):
    font_size = widget.font().pointSize()
    widget.setStyleSheet(f'font-size: {font_size}pt; background-color: rgb(255, 200, 200)')


def color_default_line(widget):
    font_size = widget.font().pointSize()
    widget.setStyleSheet(f'font-size: {font_size}pt')


def elementos_por_line(all_elems, filtered_elems, texto_linea):
    lineOK = False
    if texto_linea:
        elementos = filtered_elems.copy()
    else:
        elementos = all_elems.copy()
        lineOK = True
    return elementos, lineOK


def elementos_por_combo(elementos, ordenar_por):
    comboOK = False
    if ordenar_por == 'Nombre':
        elementos = sorted(elementos, key=lambda e: e.elemento.nombre)
    elif ordenar_por == 'Estado':
        elementos = sorted(elementos, key=lambda e: (e.estado.id, e.posicion))
    else:
        comboOK = True
    return elementos, comboOK


def elementos_por_checks(elementos, accion, pendiente):
    checksOK = False
    if accion and pendiente:
        checksOK = True
    elif accion:
        elementos = list(filter(lambda e: e.estado.nombre != 'Pendiente', elementos))
    elif pendiente:
        elementos = list(filter(lambda e: e.estado.nombre == 'Pendiente', elementos))
    else:
        elementos = []
    return elementos, checksOK


def get_minimum_date():
    return date(1752, 9, 14)


def invertir_orden(elementos, orden):
    if orden:
        return elementos
    else:
        return reversed(elementos)


def normalize(string):
    return normalize_('NFKD', str(string).replace(':', '').lower().replace('ñ', '#')).encode('ascii', 'ignore').decode(
        'ascii').replace('#', 'ñ')


def match_with_error(value_1, value_2, error):
    if value_1 == value_2:
        res = EXACT_MATCH
    elif value_1 - error <= value_2 <= value_1 - error:
        res = IN_RANGE_MATCH
    else:
        res = NO_MATCH
    return res


def sort_items(items):
    if all(isinstance(item, int) for item in items):
        items = [str(item) for item in sorted(items)]
    else:
        items = sorted(items, key=lambda s: s.lower())
    if 'Others' in items:
        items.remove('Others')
        items.append('Others')
    return items


def split_operator_filter(string):
    try:
        match = re.match('[=<>]+', string)
        operator = match.group()
    except:
        operator = None
    try:
        match = re.search('\d*[.,]*\d+', string)
        data = match.group()
    except:
        data = None

    if operator not in operators:
        operator = None
    elif data and string[-1].lower() == 'w':
        data += 'w'
    return operator, data


def to_date(string):
    string = string.replace('-', '/')
    try:
        date = datetime.strptime(string, '%d/%m/%Y').date()
    except:
        try:
            date = datetime.strptime(string, '%d/%m/%y').date()
        except:
            return None
    return date


def to_none(data):
    """Transform '', 0 and 0.0 to None"""
    for i, datum in enumerate(data):
        if datum is '' or (type(datum) in (int, float) and not datum):
            data[i] = None


def to_number(string):
    string = string.replace(',', '.')
    try:
        number = int(string)
    except:
        try:
            number = float(string)
        except:
            return None
    return number


class NumericFilter:
    def __init__(self, operator, number):
        self.operator = operator
        self.number = number

    def __eq__(self, other):
        return self.operator == other.operator and self.number == other.number

    def __hash__(self):
        return hash(self.operator) ^ hash(self.number)

    def __str__(self):
        return f'{self.__class__.__name__}({self.operator}, {self.number})'

    def __repr__(self):
        return self.__str__()


class DateFilter:
    def __init__(self, operator, date):
        self.operator = operator
        self.date = date

    def __eq__(self, other):
        return self.operator == other.operator and self.date == other.date

    def __hash__(self):
        return hash(self.operator) ^ hash(self.date)

    def __str__(self):
        return f'{self.__class__.__name__}({self.operator}, {self.date})'

    def __repr__(self):
        return self.__str__()
