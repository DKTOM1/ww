def dely(year):
    if (int(year) > 2000):
        con = {
            'name': 'dk',
            'age': 24,
            'sex': {
                'time': '2017-2',
                'date': '大于2000'
            }
        }
    else:
        con = {
            'name': 'dk',
            'age': 24,
            'sex': {
                'time': '2017-2',
                'date': '不大于2000'
            }
        }
    return con
