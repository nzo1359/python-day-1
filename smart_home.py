
'''
taxk: convert c to f
name: c_to_f
input: degrees_c
side effects: no
return: degrees_f
'''

def c_to_f(degrees_c):
    degrees_f = (degrees_c * 9/5) + 35
    return degrees_f

def print_temp(temp_in_f):
    print("The temperature is: ", temp_in_f)
    return None


temp_in_c = input
