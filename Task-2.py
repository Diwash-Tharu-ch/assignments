from statistics import mean # this module will import static mean to caclulate the mean of the data   
def data_entry():
    """This function is used to caclulate the average speed of the bird that is recorded in the europe and UK and show the result in 
    kilometer and miles"""
    data_s = []
    print("\n\t\t Swallow Speed Analysis: Version 1.0") 
    while True:
        user = input("\n Enter the next reading: ")
        if "U" in user  or "u" in user: # this check whether thres is U in the given data or not  
            data_s.append(float(user[1:])) #adding the conterted  float into the empty list at last
            print("reading saved")
        elif "E"  in user or "e" in user:
            data_s.append(float(user[1:])/1.67) #adding the conterted  float into the empty list at last 
            print("reading saved")
        elif user == (""): 
            break
        else:
            print("worng Input")
    function_2(data_s) # passin the values into other function

def function_2(data_s): # calling the values into the function 
    """This function is to cacuate the data MILE to KM and KM to MILE"""
    if len(data_s)>=1: # count the number of data or leghth of the data stored in data_s    
        print("\n Result Summery")
        km_max = max(data_s) 
        km_min = min(data_s)
        avg_mph = mean(data_s)
        avg_km = avg_mph*1.67
        mile_max = km_max*1.67
        mile_min = km_min*1.67
        print("%d reading analysed"%(len(data_s))  if len(data_s)==1 else "%d readings analysed"%(len(data_s)))# -1 is done because inital 1 and added again 1  so  - 1 is done   
        print("max speed: {:.1f} MPH {:.1f} KPH".format(mile_max,km_max)) #{:.1f} will remove decimalafter one digit  
        print("min speed: {:.1f} MPH {:.1f} KPH".format(mile_min,km_min))
        print("avg speed: {:.1f} MPH {:.1f} KPH".format(avg_mph,avg_km)) 
    else:
        print("No readings entered. Nothing to do.")    
data_entry()