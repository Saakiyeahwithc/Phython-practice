'''representing the graph with dictionary'''
my_graph={
 'a':['b','c'],
 'b':['d','e'],
 'c':['f'],
 'd':['g'],
 'e':['h']
 }
new_weight_graph={
    'Biratnagar':{
        'ithari':22,
        'rangeli':25,
        'biratchowk':30
        },
    'ithari':{
        'dharan':20,
        'biratchowk':11,
        'biratnagar':22
        },
    'rangeli':{
        'biratnagar':25,
        'kanepokhari':25,
        'urlabari':40
        },
    'biratchowk':{
        'biratnagar':30,
        'ithari':11,
        'kanepokhari':10
        },
    'kanepokhari':{
        'biratchowk':10,
        'rangeli':25,
        'urlabari':12
        },
    'urlabari':{
        'kanepokhari':12,
        'rangeli':40,
        'damak':6
        },
    'damak':{
        'urlabari':6
        }
    }
print("question a:")
for key in my_graph.keys():
    print('{}>'.format(key,my_graph[key]))
print("***********")
print("question b:")
for key in new_weight_graph.keys():
    for item in new_weight_graph[key].items():
        print('{}>{}'.format(key,item))