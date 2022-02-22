

data_samples = ['Latitude: 0\n', 'Longitude: nan\n', 'Altitude: nan\n', 'Satellites: 0\n', 'Quality: 0\n', 'SigQuality: Good\n', 'SigQualitydBm: 0\n',
                'Latitude: 1', 'Longitude: nan\n', 'Altitude: nan\n', 'Satellites: 0\n', 'Quality: 0\n', 'SigQuality: Good\n', 'SigQualitydBm: 1\n',
                'Latitude: 2', 'Longitude: nan\n', 'Altitude: nan\n', 'Satellites: 0\n', 'Quality: 0\n', 'SigQuality: Good\n', 'SigQualitydBm: 2\n',
                'Latitude: 3', 'Longitude: nan\n', 'Altitude: nan\n', 'Satellites: 0\n', 'Quality: 0\n', 'SigQuality: Good\n', 'SigQualitydBm: 3\n',
                'Latitude: 4', 'Longitude: nan\n', 'Altitude: nan\n', 'Satellites: 0\n', 'Quality: 0\n', 'SigQuality: Good\n', 'SigQualitydBm: last\n'
                ]
#for i in range(32):
    #print(data_samples[i])

total_dict = {}
dict_1 = {}
dict_2 = {}
dict_3 = {}
dict_4 = {}
dict_5 = {}

array_of_dicts = []
num_points = int(len(data_samples) / 7) # 35 / 7 = 5 points from 0 to 4
number_samples = int(len(data_samples)) # should be 35
x = len(data_samples)

#print("THIS IS HOW MANY SAMPLES")
print(number_samples)
print(num_points)
print("----------------------------------------------------------------<<<<<<<")

for m in range(num_points):
    
    #print('---------')
    a = "Point" + str(m)
    array_of_dicts.append(a)
    #print(m)
    #print("---------")
    for n in range(number_samples):
        #print(n)
        #print("#######")
        if n < 7:
            j = n 
            #print(j)
            string = data_samples[j]
            print("---------")
            print(a)
            print(string)
            print(" ")

            # Take away these from each string
            x = string.split(':')
            x = string.split(' ')
            x[0] = x[0].strip(':')
            x[1] = x[1].strip('\n')
        n = n - (7 * m)

