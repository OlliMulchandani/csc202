class Node:
    def __init__(self, left_child_index):
        self.DataValue = ""
        self.LeftChild = left_child_index
        self.RightChild = -1


class ExpressionTree:
    def __init__(self):
        self.Tree = list()
        for index in range(1, 21):
            self.Tree.append(Node(index))
        self.Fringe = list()
        self.Root = 0
        self.NextFreeChild = 0

    def IsOperator(self, s):
        if "+" in s:
            return True
        if "-" in s:
            return True
        if "*" in s:
            return True
        if "/" in s:
            return True
        return False
    
    def Insert(self, NewToken):
        if self.NextFreeChild == -1: # Check if tree is full
            return "Tree is Full"
        if self.NextFreeChild == 0: # Tree is not full, insert new token
            self.Tree[self.Root].DataValue = NewToken
            self.NextFreeChild = self.Tree[self.Root].LeftChild
            self.Tree[self.Root].LeftChild = -1
        else:
            # insert into tree with existing notdes
            # starting with Root
            Current = 0 # index of the current node
            Previous = -1
            NewNode = self.Tree[self.NextFreeChild] # declare new node
            NewNode.DataValue = NewToken

            # Finding the node where NewNode can be inserted
            while Current != -1:
                CurrNode = self.Tree[Current]
                if self.IsOperator(CurrNode.DataValue): # Check if CurrNode contains an operator
                    # if LeftChild is empty, insert here
                    if CurrNode.LeftChild == -1:
                        CurrNode.LeftChild = self.NextFreeChild
                        self.NextFreeChild = NewNode.LeftChild
                        NewNode.LeftChild = -1
                        Current = -1
                    # if rightchild is empty, insert here
                    elif CurrNode.RightChild == -1:
                        CurrNode.RightChild  = self.NextFreeChild
                        self.NextFreeChild = NewNode.LeftChild
                        NewNode.LeftChild = -1
                        Current = -1
                    # if LeftChild is an operator, traverse LeftChild subtree
                    elif self.IsOperator(self.Tree[CurrNode.LeftChild].DataValue):
                        Previous = Current
                        Current = CurrNode.LeftChild
                        self.Fringe.append(Previous)
                    # if RightChild is an operator, traverse RightChild subtree
                    elif self.IsOperator(self.Tree[CurrNode.RightChild].DataValue):
                        Previous = Current
                        Current = CurrNode.RightChild
                        self.Fringe.append(Previous)
                    # traverse right subtree
                    else:
                        Previous = self.Fringe.pop(-1)
                        Current = self.Tree[Previous].RightChild
                # no place to insert
                else:
                    return "Cannot be inserted"
    
    def Display(self):
        for index in range(len(self.Tree)):
            print("Index: ", index, "DataValue: ", self.Tree[index].DataValue)
    
    def Infix(self, root, arr):
        if root.DataValue != "":
            if self.IsOperator(root.DataValue):
                arr.append('(')
            
            self.Infix(self.Tree[root.LeftChild], arr)
            arr.append(root.DataValue)
            self.Infix(self.Tree[root.RightChild], arr)

            if self.IsOperator(root.DataValue):
                arr.append(')')
    
    def calculate(self, expression):
        def processing(left, stack): # evaluates an expression in parenthesis, returns the evaluation and stack up to "("
            right = stack.pop() # get right number
            right = int(right)
            operator = stack.pop() # get operator
            left = stack.pop() # get left number
            left = int(left)

            # calculating depending on operator
            if "+" in operator:
                left += right
            elif "-" in operator:
                left -= right
            elif "*" in operator:
                left *= right
            elif "/" in operator:
                left /= right
            return left, stack

        stack = []
        count = 0
        left = 0

        for char in expression:
            stack.append(char)
            if char == ")":
                stack.pop() # pops ")"
                left, stack = processing(left, stack)
                stack.pop() # pops "("
                stack.append(left) # appends the evaluated expression to the stack
        
            if count == len(expression)-1: # last char of expression string
                left, stack = processing(left, stack) # computes final evaluation
            count += 1
        return left # left is the calculated integer

    def infix_to_postfix(self, infix):
            stack = []
            postfix = ""
            priority = {'+':1, '-':1, '*':2, '/':2}

            for char in infix:
                # if char is "("
                if char == "(":
                    stack.append(char)

                # if char is ")"
                elif char == ")": 
                    while stack and stack[-1] != "(":
                        postfix += stack.pop() + ' '
                    stack.pop()

                # if char is an operand
                elif not self.IsOperator(char) and char != "(" and char != ")":
                    postfix += char + ' '

                # char is an operator
                else: 
                    while stack and stack[-1] != "(" and priority[char] <= priority[stack[-1]]:
                        postfix += stack.pop() + ' '
                    stack.append(char)

            while stack:
                postfix += stack.pop() + ' '
            return postfix

'''
    def infix_to_prefix(self, infix):
        pass
    def Build(self, postfix): # build a tree using postfix expression
        pass
'''

expressionTree = ExpressionTree()

expressionTree.Insert("+")
expressionTree.Insert("*")
expressionTree.Insert("4")
expressionTree.Insert("2")
expressionTree.Insert("/")
expressionTree.Insert("3")
expressionTree.Insert("1")

arr = []
expressionTree.Infix(expressionTree.Tree[0], arr)
expression_string = "".join(arr[1:-1])

infix = expression_string
postfix = expressionTree.infix_to_postfix(expression_string)
value = expressionTree.calculate(expression_string)

print(f"infix: {infix}\npostfix: {postfix}\nvalue: {value}")