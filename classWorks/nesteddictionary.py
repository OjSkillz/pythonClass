school_records = {
"class_1" : {
"students" : [ {"name" : "Harry", "scores" : {"Math" : 88, "English" : 76}}, 
                        {"name" : "Solomon", "scores" : {"Math" : 95, "English" : 89}}
                    ]
},
"class_2" : {
"students" : [ {"name" : "Daniel", "scores" : {"Math" : 78, "English" : 72}},
                        {"name" : "Samuel", "scores" : {"Math": 85, "English" : 80}}
                        ]
}   
}
total = 0
average = 0
count = 0

for value in school_records.values():
    for values in value["students"]:
        total += values["scores"]["Math"]
        count += 1
    
    
average = total / count    
print(average)

total_1 = 0
total_2 = 0
counter_1 = 0
counter_2 = 0
class_averages = []

for value in school_records["class_1"].values():
    for values in value:
        total_1 += values["scores"]["Math"]
        counter_1 += 1
    class_averages.append(total_1 / counter_1)
    
for value in school_records["class_2"].values():
    for values in value:
        total_2 += values["scores"]["Math"]
        counter_2 += 1
    class_averages.append(total_2 / counter_2)
print(class_averages)
    

        
        
        
    
    
