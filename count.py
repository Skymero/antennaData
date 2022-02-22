from collections import defaultdict
from re import search

def splitting_string(data_sample):
    
    data_sample = data_sample.strip('\n')
    data_sample = data_sample.strip('SigQualitydBm: ')   

    return data_sample


data_samples = ['Latitude: 0\n', 'Longitude: nan\n', 'Altitude: nan\n', 'Satellites: 0\n', 'Quality: 0\n', 'SigQuality: Good\n', 'SigQualitydBm: -75\n',
                'Latitude: 1', 'Longitude: nan\n', 'Altitude: nan\n', 'Satellites: 0\n', 'Quality: 0\n', 'SigQuality: Good\n', 'SigQualitydBm: line 2\n',
                'Latitude: 2', 'Longitude: nan\n', 'Altitude: nan\n', 'Satellites: 0\n', 'Quality: 0\n', 'SigQuality: Good\n', 'SigQualitydBm: line 3\n',
                'Latitude: 3', 'Longitude: nan\n', 'Altitude: nan\n', 'Satellites: 0\n', 'Quality: 0\n', 'SigQuality: Good\n', 'SigQualitydBm: line 4\n',
                'Latitude: 4', 'Longitude: nan\n', 'Altitude: nan\n', 'Satellites: 0\n', 'Quality: 0\n', 'SigQuality: Good\n', 'SigQualitydBm: line 5\n'
                ]


points_dict = defaultdict(list)
#print(int(len(data_samples)))

list_array = ['list1', 'list2', 'list3', 'list4', 'list5']

count = 0

# for element in data_samples: #itirates for the length of data_samples
#     for something in list_array: #iterates for the length of list_array
a = 0
loop_num = 0

for elements in list_array: # Loops for length of list array from 0 to 4 5 loops total
    #print(elements)
    
    for count in range(7): #print the first 7 elements in data samples
        a = count + (7 * loop_num) # loop 0 then a is 0 - 6
        
        if count == 6:
            b = splitting_string(data_samples[a])
            points_dict[elements].append(b)
        else: points_dict[elements].append(data_samples[a])       
    
    loop_num+=1


print(points_dict)


#Only print the SigQualitydBm value
#   remove '\n'
#   remove 'SigQualitydBm'
#   add value to list
#   plot list to a matplotlib plot

