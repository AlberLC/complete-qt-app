from difflib import SequenceMatcher

from utilities.various import operators, normalize, split_operator_filter, to_date, to_number, NumericFilter, DateFilter


def match_ratio(string_a, string_b):
    return SequenceMatcher(None, string_a.lower(), string_b.lower()).ratio()


def match_all_words(line_words, item_words):
    if line_words:
        coincidences = 0
        objective = len(line_words)
        for line_word in line_words:
            for item_word in item_words:
                if line_word in item_word or match_ratio(line_word, item_word) > 0.7:
                    coincidences += 1
                    break
            if coincidences == objective:
                break
        else:
            return False
    return True


def filtered_items(items, text_line):
    filtered_items = []
    line_words = set(normalize(text_line).split())

    for i, item in enumerate(items):
        item_words = normalize(item).split()

        if match_all_words(line_words, item_words):
            filtered_items.append(item)
    return filtered_items


def rows_indices_filtered(items, text_line, my_strings=None):
    indices = []
    line_words = set(normalize(text_line).split())
    discards = {'-', '<', '>', '=', '<=', '>=', '=<', '=>'}
    line_words -= discards
    positive_words = set()
    negative_words = set()
    prices = set()
    powers = set()
    dates = set()

    # Classify line sub-strings in their respective sets
    for word in line_words:
        operator, data = split_operator_filter(word)
        if word[0] == '-':
            negative_words.add(word[1:])
        elif operator:
            if data:
                date = to_date(data)
                if date:
                    dates.add(DateFilter(operator, date))
                elif data[-1].lower() == 'w':
                    powers.add(NumericFilter(operator, to_number(data[:-1])))
                else:
                    prices.add(NumericFilter(operator, to_number(data)))
        else:
            positive_words.add(word)

    for i, item in enumerate(items):
        item_words = item.get_keywords(my_strings)
        skip = False

        if skip:
            continue

        # Discard dates out of range
        for date in dates:
            if (
                    not operators[date.operator](item.date_quotation, date.date) and
                    not operators[date.operator](item.date_validity, date.date)
            ):
                skip = True
                break

        if skip:
            continue

        # Discard prices out of range
        for price in prices:
            if not operators[price.operator](item.price, price.number):
                skip = True
                break

        if skip:
            continue

        # Discard powers out of range
        for power in powers:
            if (
                    not operators[power.operator](item.total_power, power.number) and
                    not operators[power.operator](item.panel_power, power.number)
            ):
                skip = True
                break

        if skip:
            continue

        # Discard negative words
        for negative_word in negative_words:
            for item_word in item_words:
                if negative_word in item_word:
                    skip = True
                    break
            else:
                continue
            break

        if skip:
            continue

        # Search positive words coincidences
        if match_all_words(positive_words, item_words):
            indices.append(i)
    return indices
