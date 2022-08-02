class Evaluate:
  """This class validates and evaluate postfix expression.
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
  """
    # Write your code here


  def __init__(self, size):
    """Inits Evaluate with top, size_of_stack and stack.
    Arguments:
      size_of_stack: An integer to set the size of stack.
    """
    self.top = -1
    self.size_of_stack = size
    self.stack = []


  def isEmpty(self):
    """
    Check whether the stack is empty.
    Returns:
      True if it is empty, else returns False.
    """
    # Write your code here
    if self.stack==[]:
        return True
    else:
        return False
        


  def pop(self):
    """
    Do pop operation if the stack is not empty.
    Returns:
      The data which is popped out if the stack is not empty.
    """
    # Write your code here
    if not self.isEmpty():
        return self.stack.pop()
        
        


  def push(self, operand):
    """
    Push the operand to stack if the stack is not full.
    Arguments:
      operand: The operand to be pushed.
    """
    # Write your code here
    if len(self.stack)!=self.size_of_stack:
        self.stack.append(operand)
        self.top=self.top+1


  def validate_postfix_expression(self, expression):
    """
    Check whether the expression is a valid postfix expression.
    Arguments:
      expression: A String which represents the expression to be validated.
    Returns:
      True if the expression is valid, else returns False.
    """
    # Write your code here
    count1=0
    count2=0
    opr=[]
    for i in expression:
      if (i=="+" or i =="-" or i=="*" or i=="/" or i=="^"):
        count1=count1+1
        opr.append(i)
      else:
          k=int(i)
          if isinstance(k,int):
            count2+=1
    if count2-1==count1:
        a=int(expression[0])
        b=int(expression[1])
        if isinstance(a,int) and isinstance(b ,int) and expression[-1] in opr:
          return True
        else:
          return False
        
    else:
      return False
    
        


  def evaluate_postfix_expression(self, expression):
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
    # Write your code here
    for i in expression:
        if i=="+":
            a=self.pop()
            b=self.pop()
            self.stack.insert(0,b+a)
            
        elif i=="-":
            a=self.pop()
            b=self.pop()
            self.stack.insert(0,b-a)
        elif i=="*":
            a=self.pop()
            b=self.pop()
            self.stack.insert(0,b*a)
        elif i=="/":
            a=self.pop()
            b=self.pop()
            if b>a:
              self.stack.insert(0,b//a)
             else:
              self.stack.insert(0,a//b)
        elif i=="^":
            a=self.pop()
            b=self.pop()
            self.stack.insert(0,b**a)
        else:
            k=int(i)
            if isinstance(k,int):
                self.push(k)
    return(self.stack[0])
        
    


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')


