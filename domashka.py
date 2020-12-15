listofdicts = [
{'model': 'LADA 2121', 'passengers': 4, 'power': 76, 'country': 'Russia'},
{'model': 'Mercedes E124', 'passengers': 4, 'power': 156, 'country': 'Denmark'},
# {'model': 'Mercedes E124', 'pasengers': 4, 'power': 156, 'country': 'Denmark'},

]


dictoflists = {
'model': ['LADA 2121', 'Mercedes E124'],
'passengers': [4, 4],
'power': [76, 156],
'country': ['Russia', 'Denmark'],
}


table = {
'columns': ['model', 'passengers', 'power', 'country'],
'data': [
['LADA 2121', 4, 76, 'Russia',],
['Mercedes E124', 4, 156, 'Denmark']
]
}

# listofdicts -> dictoflists: (цикл) заполняем словарь dictoflists =  {listofdicts[i].keys[i] (надо взять 1 ключ ) (возьмем и-тый ключ из первого словаря)} = list(listofdicts[listofdicts.keys[1]].values)

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

res = listofdicts2dictoflists(listofdicts)
print(res)


# dictoflists -> listofdicts: (цикл) заполняем словарь listofdicts = list({dictoflists.keys[i]: dictoflists[i] (вообщем надо взять значения по ключу i)
# listofdicts -> table: table[header] = (цикл) listofdicts[i].keys, значения по ключам из 1 листа помещаем в table[data] = list(все значения в listofdicts[i])
# dictoflists -> table: table[header] = dictoflists.keys, table[data] = list(только итые значения (???))
# table -> что угодно: как то с помощью зипа?
# print(listofdicts[1])