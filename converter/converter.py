from collections import defaultdict

def listofdicts2dictoflists(listofdicts):
    # find keys:
    dictoflists = defaultdict(list) 
    ks = set(listofdicts[0].keys())
    for d in listofdicts:
        if (set(d.keys()) != ks):
            raise Exception('wrong set of keys in dict: ' + str(d))
        for key in d:
            dictoflists[key].append(d[key])
    return dict(dictoflists)


def table2dictoflists(table):
    dictoflists = defaultdict(list)
    for i, col in enumerate(table["columns"]):
        for row in table["data"]:
            try:
                dictoflists[col].append(row[i])
            except IndexError:
                raise Exception('Wrong row {}'.format(str(row)))

    # columns = table["columns"]
    # for row in table['data']:
    #     for col, val in zip(columns, row):
    #         dictoflists[col].append(row)

    return dict(dictoflists)


def listofdicts2dictoflists2(listofdicts):
    # find keys:
    dictoflists = {} 
    for d in listofdicts:
        for key in d:
            # dictoflists[key] = dictoflists.get(key, []) + [d[key]]
            if key not in dictoflists:
                dictoflists[key] = []
            dictoflists[key].append(d[key])
    return dictoflists

def dictoflists2listofdicts(dictoflists):
    listofdicts = []
    keys = list(dictoflists.keys())
    L = len(dictoflists[keys[0]])
    for i in range(L):
        dct = {}
        for key in keys:
            dct[key] = dictoflists[key][i]
        listofdicts.append(dct)
    return listofdicts


def dictoflists2listofdicts2(dictoflists):
    listofdicts = []
    for values in zip(*dictoflists.values()):
        dct = dict(zip(dictoflists.keys(), values))
        listofdicts.append(dct)
    return listofdicts

def dictoflists2table(dictoflists):
    table = {}

    table["columns"] = list(dictoflists.keys())
    table["data"] = []
    L = len(dictoflists[table["columns"][0]])
    for i in range(L):
        row = []
        for key in table["columns"]:
            row.append(dictoflists[key][i])
        table["data"].append(row)
    return table

def guess_format(data):
    if isinstance(data, list):
        return 'listofdicts'
    if isinstance(data, dict):
        if set(data.keys()) == set(['columns', 'data']):
            if isinstance(data['data'], list):
                if len(data['data']) > 0:
                    if isinstance(data['data'][0], list):
                        return 'table'
                else:
                    return 'table'
    if isinstance(data, dict):
        if all([isinstance(val, list) for val in data.values()]):
            return 'dictoflists'
    return None     

def convert(data, output_format: str, input_format: str = None):

    if input_format is None:
        input_format = guess_format(data)
    if (input_format is None) or (input_format not in ('table', 'listofdicts', 'dictoflists')):
        raise Exception('unknown input format')
    if (output_format not in ('table', 'listofdicts', 'dictoflists')):
        raise Exception('unknown output format')


    # inner_data -- data in our inner format (e.g. listofdicts)
    if (input_format == 'dictoflists'):
        inner_data = data
    if (input_format == 'table'):
        inner_data = table2dictoflists(data)
    if (input_format == 'listofdicts'):
        inner_data = listofdicts2dictoflists(data)
    

    if (output_format == 'table'):
        out_data = dictoflists2table(inner_data)
    if (output_format == 'listofdicts'):
        out_data = dictoflists2listofdicts(inner_data)
    if (output_format == 'dictoflists'):
        out_data = inner_data
    

    # if not check(out_data):
    #     raise 'out check failed'

    return out_data


if __name__ == '__main__':

    from sample_data import table, dictoflists, listofdicts

    assert table2dictoflists(table) == dictoflists
    assert dictoflists2listofdicts(dictoflists) == listofdicts


    # import pandas as pd
    # df1 = pd.DataFrame(listofdicts)
    # df2 = pd.DataFrame(dictoflists)
    # print(df1)
    # print(df2)
    # df1['hp_per_pass'] = df1['power'] / df1['passengers']
    # print(df1)

