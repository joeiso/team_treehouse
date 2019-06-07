import os
import shutil

# Ask user for a file path to the RTC directory, then establishes motor 
# and dem_daq data file paths.
rtc_path = input("What is the path to the RTC folder? (should end in /RTC)  ")
current_path = os.curdir
motor_path = rtc_path + "/clamp_force_motor"
dem_daq_path = rtc_path + "/clamp_force_dem_daq"

#Prints relevent directory contents.
print(current_path)
print("{} \n".format(os.listdir(current_path)))
print("{} \n".format(os.listdir(rtc_path)))

dir_motor = next(os.walk(motor_path))[1]
print("dir_motor: {}".format(dir_motor))

dir_dem_daq = next(os.walk(dem_daq_path))[1]
print("dir_dem_daq: {}\n".format(dir_dem_daq))


# Iterates through the dir in dir_dem_daq to explore individual device folders. 
# Devices folders may have multiple time stamped folders. 
for dir in dir_dem_daq:
    # time_stamps creates a list of all time stamp directories in a device folder
    time_stamps = os.listdir(dem_daq_path +"/" + dir)
    
    # Iterate through time_stamps to generate determing src & dst file paths and files 
    # of interest. Files are transfered from teh dem_daq/device/time_stamp to teh motor/device/time_stamp
    
    for time_stamp in time_stamps:
        src_path = dem_daq_path + "/" + dir + "/" + time_stamp
        dst_path = motor_path + "/" + dir + "/" + time_stamp
    
        print("{} \n{}".format(src_path, dst_path))
    
        file_dem_daq = next(os.walk(src_path))[2]
        print("file_dem_daq: {}\n".format(file_dem_daq))
    
       
        for file in file_dem_daq:
                
            try:
                shutil.copy2(src_path + "/" + file, dst_path)
            except ValueError as err:
                print("\n{} failed to transfer".format(file))
                pass
            else:
                print("\n{} transfered successfully".format(file))

