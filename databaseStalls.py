import datetime

# This is the database file, currently 2 stalls. Carissa can check and see how to convert this to a pickle filemanagement system
# and add more stalls based on the same format

#datetime.time(hours,mins,sec)
stall1_dict ={
    "Name" : "Chicken Rice",
    "Operating Hours" : [datetime.time(8,0,0) , datetime.time(16,0,0)],
    "Operating Days":[0,1,2,3,4,5],
    "Waiting Time" : 5,
    "Food available" :
        {   #For each item, first datetime.time is opening hours, last datetime.time is closing hours
            "Chicken Rice" : ("$5.00" , [0,1,2,3,4,5], datetime.time(8,0,0),datetime.time(17,0,0)),
            "Chicken Noodles" : ("$4.00", [0,1,2,3,5], datetime.time(10,0,0),datetime.time(17,0,0)),
            "Chicken Soup" : ("$3.00", [0,1,2,3,4,5], datetime.time(8,0,0),datetime.time(11,0,0)),
        }
    }

stall2_dict ={
    "Name" : "Macdonalds",
    "Operating Hours" : [datetime.time(6,0,0) , datetime.time(22,0,0)],
    "Operating Days":[0,1,2,4,5],
    "Waiting Time" : 3,
    "Food available" :
        {
            "2-Piece Chicken Meal" : ("$7.00" , [0,1,2,3,4,5], datetime.time(8,0,0),datetime.time(17,0,0)),
            "Big Breakfast" : ("$4.00", [0,1,2,3,4,5], datetime.time(6,0,0),datetime.time(11,0,0)),
            "Hershey's McFlurry" : ("$2.00", [0,1,2,3,4], datetime.time(6,0,0),datetime.time(22,0,0)),
        }
    }


stall3_dict ={
    "Name" : "Mini Wok",
    "Operating Hours" : [datetime.time(10,0,0) , datetime.time(21,30,0)],
    "Operating Days":[2,3,4,5,6],
    "Waiting Time" : 8,
    "Food available" :
        {
            "Salted Fish Fried Rice" : ("$7.00" , [2,3,4,5], datetime.time(10,0,0),datetime.time(17,0,0)),
            "Pineapple Fish Fried Rice" : ("$8.00", [0,1,2,3,5], datetime.time(6,0,0),datetime.time(11,0,0)),
            "Chicken Fried Rice" : ("$6.00", [0,1,3,4,6], datetime.time(6,0,0),datetime.time(22,0,0)),
        }
    }
allStalls_dict = [stall1_dict, stall2_dict,stall3_dict]

