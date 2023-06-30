import pymongo

con=pymongo.MongoClient("mongodb://localhost:27017")
db=con["Exam"]
col=db["Questions"]

qus=[
    {"_id":1,"qa":"Trimethylxanthine is a chemical name of a stimulant which is found in tea and coffee. What is the popular name?","opt1":"a) Thein","opt2":"b) Caffeine","opt3":"c) Theobromine","opt4":"d) Theophylline","ans":"b"},
    {"_id":2,"qa":"Effective TB treatment is difficult because of the unusual structure and chemical composition of the which among the following parts of the cells of Tuberculosis Bacteria (Mycobacterium tuberculosis)?","opt1":"a) Cell membrane","opt2":"b) Cell wall","opt3":"c) Nucleus","opt4":"d) Plasama","ans":"b"},
    {"_id":3,"qa":"Which among the following is the smallest Human Chromosome?","opt1":"a) Chromosome 10","opt2":"b) Chromosome 16","opt3":"c) Chromosome 20","opt4":"d) Chromosome 21","ans":"d"},
    {"_id":4,"qa":"What will be the buoyant force acting on the stone, on being immersed in water, if it displaces 100gms of water?","opt1":"a) 1000 gm-weight","opt2":"b) 100 gm-weight","opt3":"c) 10 gm-weight","opt4":"d) 1 gm-weight","ans":"b"},
    {"_id":5,"qa":"Which of the following is a commonly used moderator in a Nuclear reactor?","opt1":"a) Heavy water","opt2":"b) Graphite","opt3":"c) Water","opt4":"d) All of the above","ans":"d"},    
    ]

##test=col.insert_many(qus)
count=0
count1=0
for i in col.find():
    print(i["qa"])
    print(i["opt1"])
    print(i["opt2"])
    print(i["opt3"])
    print(i["opt4"])
    user_input=input("Please enter your answer ")
    if user_input == i["ans"]:
        count+=1
    else:
        count1+=1
    print("")
print(f"You have correctly answered  for {count} questions")
print(f"You have wrongly answered  for {count1} questions")

    
