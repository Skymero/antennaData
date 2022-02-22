from re import search
from collections import defaultdict
from signal import signal
from matplotlib import pyplot as plt


def plot_points(data_points, title):
    x_axis = []
    y_axis = []
    
    for i in range(int(len(data_points))):
        x_axis.append(i+1)
    for element in data_points:
        y_axis.append(int(element))
    print(y_axis)

    
    # plotting points as a scatter plot
    #plt.plot(x_axis, y_axis, color='green')
    plt.scatter(x_axis, y_axis, label= "stars", color= "green",
            marker= "*", s=30)
        
    plt.xlabel('x - axis')
    # frequency label
    plt.ylabel('Signal Quality dBm')
    # plot title
    plt.title(title)
    # showing legend
    plt.legend()
    
    # function to show the plot
    plt.show()

    return


def splitting_string(data_samp):
    
    data_sample = data_samp.strip('\n')
    data_sample = data_sample.strip('SigQualitydBm: ')
     
    return data_sample


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

# Gets all data into a list 
def iterate_lists(list_a, list_b):

    # Combines gsm_data & gps_data lists together
    list_c = []
    list_d = []
    #print("-------------------------------------------------")
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
            
            # x is used to make sure elements are added in order
            x += 1

        #adding 2 items from list_b after every 6 of list_a 
        if count > 4:        
            list_c.append(list_b[n])
            
            # n is used to make sure elements are added in order
            n += 1
        # Resets the count if 7 items have been appended to list_c
        if count >= 6:
            count = 0
        else: count += 1
    # Removes \n from element
    for element in list_c:
        d = splitting_string(element)
        list_d.append(d)

    return list_c

# generaltes list of keys for dict
def key_gen(num_points): 
    # numpoints = length of list c
    key_list = []
    for i in range(num_points):
        x = i + 1
        key_list.append("Point" + str(x))

    return(key_list)

# takes in your list_c and the list of keys to make dictionary
def list_to_dict(data_samples,list_array, bool_val):
    
    loop_lim = int(len(list_array)) / 7
    points_dict = defaultdict(list)
    sig_dbm_val = []
    count = 0
    a = 0
    loop_num = 0

    for element in list_array:
        
        if loop_num < loop_lim:
            # Every 7 elements gets appended to a unique key
            for count in range(7):  

                a = count + (7 * loop_num)
                j = 0 + (7 * loop_num)        

                if count == 6:                  
                    # Checking if there is a signal coming in
                    if ' nan\n' in data_samples[j]:
                        sig_dbm_val.append(0)
                    else: 
                        b = splitting_string(data_samples[a])
                        points_dict[element].append(b)
                        sig_dbm_val.append(b)

                else: points_dict[element].append(data_samples[a])

        loop_num+=1

    if bool_val == True:
        return points_dict
    if bool_val == False:
        return sig_dbm_val


# Parameters needed for each datapoint
substring_GPS = ['Latitude:','Longitude:', 'Altitude:', 'Satellites:', 'Quality:']
substring_GSM = ['SigQuality:', 'SigQualitydBm:']
key_list = ['lat', 'long', 'alt', 'qual', 'dbm']

# Parse through data to find needed parameters from each log
data_gps = parse_gps('gps.log', substring_GPS)
data_gsm = parse_gsm('gsm.log', substring_GSM)
data_gps_2 = parse_gps('gps2.log', substring_GPS)
data_gsm_2 = parse_gsm('gsm2.log', substring_GSM)


# Combining parameters into one list
data_index = iterate_lists(data_gps, data_gsm)
num_samples = int(len(data_index))

data_index_2 = iterate_lists(data_gps_2, data_gsm_2)
num_samples_2 = int(len(data_index_2))

key_array = key_gen(num_samples)
#print(key_array)
key_array_2 = key_gen(num_samples_2)

data_dictionary = list_to_dict(data_index, key_array, True)
print(data_dictionary)

data_dictionary_2 = list_to_dict(data_index_2, key_array_2, True)

sigQual_dBm = list_to_dict(data_index, key_array, False)
print(sigQual_dBm)
sigQual_dBm_2 = list_to_dict(data_index_2, key_array_2, False)

plot_points(sigQual_dBm, 'Antenna Data 1')
plot_points(sigQual_dBm_2, 'Antenna Data 2')