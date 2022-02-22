from re import search  



def parse_gps(data_file, substrings):
    gps_data = []
    # Able to read the data
    with open(str(data_file)) as f:
        contents = f.readlines()
        # Loop for all lines in the .log file
        for content in contents:
            # based on the substrings it searches and adds
            #   the whole string to a the gps_data array
            for element in substrings:
                if search(element, content):
                    gps_data.append(content)        
    f.close
    return gps_data
    

def parse_gsm(data_file, substrings):
    gsm_data = []
    # Able to read the data
    with open(str(data_file)) as f:
        contents = f.readlines()
        # Loop for all lines in the .log file
        for content in contents:
            # based on the substrings it searches and adds
            #   the whole string to a the gsm_data array
            for element in substrings:
                if search(element, content):
                    gsm_data.append(content)        
    f.close
    return gsm_data
    

def iterate_lists(list_a, list_b):
    # Combines gsm_data & gps_data lists together
    list_c = []
    #print("-------------------------------------------------")
    mod_a = len(list_a) / 5
    mod_b = len(list_b) / 2
    # Finds the loop count based on the smaller sample size
    if mod_a < mod_b:
        cnt_limit =int( mod_a * 7)
    if mod_b < mod_a:
        cnt_limit =int( mod_b * 7)
    # print(cnt_limit)
    count = 0
    n = 0
    x = 0
    for i in range(cnt_limit):    
        
        # Appends 2 items from list_a then adds 2 from list_b
        if count <= 4: #adding 5 items from list_a       
            list_c.append(list_a[x])
            #print("APPENDING FROM LIST_A")
            # x is used to make sure elements are added in order
            x += 1
        
        if count > 4: #adding 2 items from list_b after every 6 of list_a        
            list_c.append(list_b[n])
            # print("APPENDING FROM LIST_B")
            # n is used to make sure elements are added in order
            n += 1
        # Resets the count if 7 items have been appended to list_c
        if count >= 6:
            count = 0
        else: count += 1
        
    return list_c


def generate_hashmap(data_points):
    x = 0
    data_dict = {}
    num_points = int(len(data_points) / 7)
    key_list = []
    #create points for every 7 num_points
    #   i.e if you have 14 data_points, num_points = 2
    #   this also means you should have 2 dictionaries
    #   w/ 7 keys and values.
    for i in range(num_points):
        i += 1
        key_list.append("Point" + str(i))
    print(key_list)

    key_num = int(len(key_list) - 1)
    count = 0
    
    print("key_num")
    print(key_num)
    for j in range(key_num):
        
        print("LOOP..........:")
        print(j)
        print("  ")
        print("KEY:  ")
        print(key_list[j])
        print(" ")
        print(" DATA: ")

        for v in range(num_points):
            #adds 7 elements to dictionary per key
            # should be point1: 7 items(0-6), point2: 7 items (7-13)
            key = str(key_list[j])
            if count < 1:                
                print(data_points[v])
                data_dict[key] = data_points[v]
                count += 1
            if count > 0:
                print(data_points[v])
                data_dict[key].update(data_points[v])
                count += 1
        count = 0
    print(data_dict)
    return data_dict


# def data_key_array(p_data):



# Parameters needed for each datapoint
substring_GPS = ['Latitude:','Longitude:', 'Altitude:', 'Satellites:', 'Quality:']
substring_GSM = ['SigQuality:', 'SigQualitydBm:']
key_list = ['lat', 'long', 'alt', 'qual', 'dbm']

# Parse through data to find needed parameters from each log
data_gps = parse_gps('gps.log', substring_GPS)
data_gsm = parse_gsm('gsm.log', substring_GSM)

# Combining parameters into one list
data_index = iterate_lists(data_gps, data_gsm)
print(data_index)

#print(data_index)


# use data_index for a hashmap
#hash_dict = generate_hashmap(data_index)

#data_samples = []

'''
records = [
    {long:123, lat: 456, ...}
    ,{long:123, lat: 456, ...}
    ,{long:123, lat: 456, ...}
    ,{long:123, lat: 456, ...}
    ,{long:123, lat: 456, ...}
    ,{long:123, lat: 456, ...}
    ,{long:123, lat: 456, ...}
]

for i in records:
    variable1 = "long"
    map.addPoint(records[i]["long"], records[i][variable1], records[i].value)


{key1: [long:123, lat: 456, ...], key2}
'''

# use hashmap as reference for data points of DJANGO map





