from pycorvert import Pyconvert

test = {
    
    "People":{
        "Name":"Alan",
        "Address":{
            "Street": "Of dumbs",
            "Number":0
        }
    }
}

string = Pyconvert.convert_dict_to_xml(dictionary=test, raw_string=False)

print(string)