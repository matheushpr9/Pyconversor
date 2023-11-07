from modules.Node import Node
from modules.Tree import Tree

class Pyconvert:

    def convert_dict_to_xml(dictionary: dict) -> str:
        root = Tree.create_tree_by_dict(dictionary=dictionary)

test = {
    
    "People":{
        "Name":"Alan",
        "Address":{
            "Street": "Of dumbs",
            "Number":0
        }
    }
}

root = Tree.create_tree_by_dict(dictionary=test)

print(root.convert_node_to_xml())