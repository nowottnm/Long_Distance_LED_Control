import json

in_dict = json.load(open("raspi_config.json"))
in_dict["connection"]["EmailInterface"]["host"] = input("please enter host (ie posteo.de):")
in_dict["connection"]["EmailInterface"]["account"] = input("email account:")
in_dict["connection"]["EmailInterface"]["password"] = input("please enter pw:")
json.dump(in_dict, open("/home/pi/Desktop/raspi_config.json", "w"))
