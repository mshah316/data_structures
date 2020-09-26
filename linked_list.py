class linked_list:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self.length = 0
        
    def add_node(self,value):
        if self.head_node == None:
            self.head_node = node(value)
            self.tail_node = self.head_node
        else:
            self.tail_node.next_node = node(value)
            self.tail_node = self.tail_node.next_node
        self.length += 1
        
    def delete_node(self,value):
        curr_node = self.head_node
        prev_node = None
        while(curr_node != None):
            if curr_node.value == value:
                self.length -= 1
                if prev_node == None and curr_node.next_node == None:
                    self.head_node = None
                    self.tail_node = None
                elif prev_node == None:
                    self.head_node = curr_node.next_node
                    curr_node.next_node = None
                elif curr_node.next_node == None:
                    self.tail_node = prev_node
                    prev_node.next_node = None
                else:
                    prev_node.next_node = curr_node.next_node
                    curr_node.next_node = None
            prev_node = curr_node
            curr_node = curr_node.next_node
    
    def print_list(self):
        curr_node = self.head_node
        prev_node = None
        list_str = ''
        while(curr_node != None):
            if prev_node == None and curr_node.next_node == None:
                list_str = list_str + f'{curr_node.value}'
            elif prev_node == None:
                list_str = list_str + f'{curr_node.value}-->'
            elif curr_node.next_node == None:
                list_str = list_str + f'{curr_node.value}'
            else :
                list_str = list_str + f'{curr_node.value}-->'
            prev_node = curr_node
            curr_node = curr_node.next_node
        print(list_str)

class node:
    def __init__(self,value):
        self.value = value
        self.next_node = None
