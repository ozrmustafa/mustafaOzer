import json
my_file=open("mustafa.json","r")
my_json=json.load(my_file)
print(my_json["kimlik"]["Ad"])
print(my_json["kimlik"]["Soyad"])
print("##########")
print(my_json["kimlik"])
