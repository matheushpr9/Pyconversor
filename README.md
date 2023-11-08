# Pyconvert

## Motivation

Pyconvert is a lib developed with the aim of unifying all the conversion tools a dev might need during development in one place.

## Instructions

1. Install:

    ``` shell
        pip install pyconvert
    ```

2. Convert:

    **Example:**

    ``` python
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

    ```

## features and plans

- [x] Convert a dictionary to a XML (on a raw string or not)
- [ ] Convert a xml to a dictionary/.
