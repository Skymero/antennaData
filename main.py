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

def points_Count(data_points):

    x = 0
    data_dict = {}
    num_points = int(len(data_points) / 7)
    key_list = [] # Array with how many data points to be used

    # How many data points
    for i in range(num_points):
        i += 1
        key_list.append("Point" + str(i))
    #print(key_list)
    return key_list

def data_dict(list_a, list_b):
    # Creates a dictionary for all points
    #adds array of 7 elements into one element in 2Darray
    list_c = {}    
    
    for x in range(0,len(data_index), 1):

        # Add every 7 values as an element - 2D array
        location_string = "Point " + str(x+1)
        #print(location_string)
        x_array = data_index[x:x+7]
        #print(x_array)
        list_c[location_string] = x_array
        #print(data_index[x:x+7])
    #print(list_c)
    
    return list_c

def iterate_lists(list_a, list_b):

    # Combines gsm_data & gps_data lists together
    list_c = []    
    mod_a = len(list_a) / 5
    mod_b = len(list_b) / 2

    # Finds the loop count based on the smaller sample size
    if mod_a < mod_b:
        cnt_limit =int( mod_a * 7)

    if mod_b < mod_a:
        cnt_limit =int( mod_b * 7)
    
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

#################################################
# Parameters needed for each datapoint

substring_GPS = ['Latitude:','Longitude:', 'Altitude:', 'Satellites:', 'Quality:']
substring_GSM = ['SigQuality:', 'SigQualitydBm:']
key_list = ['lat', 'long', 'alt', 'qual', 'dbm']

##########################################################

# Parse through data to find needed parameters from each log
data_gps = parse_gps('gps.log', substring_GPS)
data_gsm = parse_gsm('gsm.log', substring_GSM)

##########################################################
# Combining parameters into one list

data_index = iterate_lists(data_gps, data_gsm)
point_list = points_Count(data_index)
list_of_lists = data_dict(point_list, data_index)

for i in list_of_lists:
    print("---------------------------")
    print(" ")
    print(i)
    print(list_of_lists[i])

# Finsh by adding this to a csv file or notepad in this format




