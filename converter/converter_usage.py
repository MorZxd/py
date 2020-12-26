from converter import convert


table_ = {
    'columns': ['lalala', 'bububub'],
    'data': [
        [123, 'qqqqq'],
        [456, 'rrrrr'],
        [666, 'kwyekuewh']
    ]
}

print('guessed', guess_format(table_))


res = convert(table_, 'listofdicts')
print(res)