from csv import DictReader


with open('hero_stats.csv', 'r') as read_obj:
    dict_reader = DictReader(read_obj)
    data = list(dict_reader)

# Get the count of hero types
def count_heroes_by_type(type):
    counter = 0
    for hero in data:
        if hero['primary_stat'] == type:
            counter += 1
    return counter

#str_count = 37 
#agi_count = 37
#int_count = count_heroes_by_type("INT")

#Calculate dps per hero type
def average_dps_by_type(type):
    type_count = count_heroes_by_type(type)
    sum_dps = 0
    dmg_type = {}
    dmg_list = []
    for hero in [hero for hero in data if hero['primary_stat'] ==  type]:
        #data if hero['primary_stat'] ==  type: 
        sum_dps += float(hero['dps'])
        if not float(hero['dps']) in dmg_list:
            dmg_list.append(float(hero['dps']))
            dmg_type[hero['dps']] = 1
        else: 
            dmg_type[hero['dps']] = dmg_type[hero['dps']] + 1
    dmg_list.sort()
    dmg_type = dict(sorted(dmg_type.items(), key=lambda item: item[1]))
    return int(sum_dps/type_count), dmg_type, dmg_list

avg_str_dps = average_dps_by_type('STR')
avg_agi_dps = average_dps_by_type("AGI")
avg_int_dps = average_dps_by_type('INT')
print(avg_str_dps,avg_agi_dps,avg_int_dps)

