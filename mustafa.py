# Fill in this file with the code from parsing JSON exercise
import json
my_file=open("mustafa.json","r")
my_json=json.load(my_file)
print(my_json["kimlik"]["Ad"],my_json["kimlik"]["Soyad"],sep="\n")
