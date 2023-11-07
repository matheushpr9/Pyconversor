class Node:
    def __init__(self, name, value, path:str = '/') -> None:
        print(type(value))
        print(type(value) is dict)
        if type(value) is dict:
            self.value = []
            for key in value:
                self.value.append(Node(name=key, value=value[key], path= path+f"/{name}"))
                self.name = name
                self.path=path

        else:
            self.value = value
            self.name = name
            self.path = path

    def print_Node(self,cont = 0):
        print( f"\r{cont*'   ' }<{self.name}>")
        if type(self.value) is list:
            for node in self.value:
                node.print_Node(cont = cont+1)
        else:
            print(f"\r{cont*'   ' }"+str(self.value))

        print(f"\r{cont*'   ' }</{self.name}>")


    def convert_node_to_xml(self, string='<?xml version="1.0" encoding="utf-8"?>'):
        string += f"<{self.name}>"
        if type(self.value) is list:
            for node in self.value:
                print(node)
                string += node.convert_node_to_xml('')
        else:
            string+=str(self.value)
        string+=f"</{self.name}>"
        
        
        return string

    