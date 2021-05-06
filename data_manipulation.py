from csv import DictReader


with open('hero_stats.csv', 'r') as read_obj:
    dict_reader = DictReader(read_obj)
    data = list(dict_reader)
    # print list of dict i.e. rows

for x in range(0,1):
    print(data[x])

str_count =0 
agi_count =0
int_count =0 
for hero in data:
    if hero['primary_stat'] == 'STR':
        str_count += 1
    elif hero['primary_stat'] == 'AGI':
        agi_count +=1
    else:
        int_count+=1
print(str_count, agi_count, int_count)