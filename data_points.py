
data_samples = ['Latitude: 0\n', 'Longitude: nan\n', 'Altitude: nan\n', 'Satellites: 0\n', 'Quality: 0\n', 'SigQuality: Good\n', 'SigQualitydBm: -75\n',
                'Latitude: 1', 'Longitude: nan\n', 'Altitude: nan\n', 'Satellites: 0\n', 'Quality: 0\n', 'SigQuality: Good\n', 'SigQualitydBm: -75\n'
                'Latitude: 2', 'Longitude: nan\n', 'Altitude: nan\n', 'Satellites: 0\n', 'Quality: 0\n', 'SigQuality: Good\n', 'SigQualitydBm: -75\n'
                'Latitude: 3', 'Longitude: nan\n', 'Altitude: nan\n', 'Satellites: 0\n', 'Quality: 0\n', 'SigQuality: Good\n', 'SigQualitydBm: -75\n'
                'Latitude: 4', 'Longitude: nan\n', 'Altitude: nan\n', 'Satellites: 0\n', 'Quality: 0\n', 'SigQuality: Good\n', 'SigQualitydBm: -75\n'
                ]
#######String to dictionary ###########################

# Converting string to dictionary
# Iterates through data_samples[i]
def str_to_dict(data_points, ):
    
    total_dict = {}
    dict_1 = {}
    
    for g in range(len(data_points)):
        string = data_samples[g]

        x = string.split(':')
        x = string.split(' ')
        x[1] = x[1].strip('\n')
        x[0] = x[0].strip(':')    
        dict_1[x[0]] = x[1]

    print(dict_1)
    return dict_1


dict_3 = {}
key_array = []
that_array = []
num_points = int(len(data_samples) / 7)

for i in range(num_points):
        i += 1
        key_array.append("Point" + str(i))
print(key_array)

count = 0
for m in range(len(key_array)):
    for v in range(len(data_samples)):
        # dict_3 
        if count < 7:
            dict_3[key_array[m]][count] = data_samples[v]
            count += 1
        
        if count == 7:
            count = 0
print(dict_3)

    




    