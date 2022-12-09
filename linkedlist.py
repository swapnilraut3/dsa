class Node:
    '''This is a node class''' 
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next
    
    # def __repr__(self) -> str:
    #     return(f'{self.value} --> {self.next}')


class LinkedList:
    '''This is linkeed list calls'''
    def __init__(self, value, next=None) -> None:
        self.head = Node(value)

    def add(self, value):
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = Node(value)

    def __repr__(self) -> str:
        '''This is how we traverse aks print 
        the LL'''
        current = self.head
        mystr = ''
        while current:
            mystr += f'{current.value}'
            current = current.next
        return ' --> '.join(mystr)


    def delete(self, index):
        '''deletes the node at given index 
        index: the 0th based position'''
        # deleting the head/first node
        if index == 0:
            self.head = self.head.next
            return

        # deleting elsewhere
        current = self.head
        for item in range(index-1):
            current = current.next
        current.next = current.next.next

          
        
if __name__ == '__main__':
    myll = LinkedList('a')
    myll.add('b')
    myll.add('c')
    myll.add('d')
    myll.add('e')
    myll.add('f')
    print(myll)
    myll.delete(4)
    print(myll)
