from stack import Stack
import operator

ops = { "+": operator.add,
        "-": operator.sub,
        "*":operator.mul,
        "/":operator.truediv,
        "^":operator.pow,
        "n":operator.neg
}
'''Precendence Table
Value at index 0 is precedence value at index outside the stack
Value at index 1 is precedence value inside the stack
'''
prec_table={
    '+':[1,2],
    '-':[1,2],
    '*':[3,4],
    '/':[3,4],
    'n':[6,5],
    '^':[8,7],
    '(':[9,0],
    ')':[0,None]
}

'''Makes sure that every opening parenthesis in the expression has 
a corressponding closing parenthesis'''

def isExpressionValid(exp):
    st=Stack()
    for item in exp:
        if item=="(":
            st.push(item)
        elif item==")":
            if st.isEmpty():
                return False
            st.pop()
    return st.isEmpty()

'''
Converts a valid infix expression to postfix expression
'''
def evaluate(exp):
    global prec_table
    if not isExpressionValid(exp):
        return "Invalid Expression"
    st=Stack()
    postfix=''
    #This array stores numbers in Expression
    #For e.g if expression is 55+27-19, it will contain [55,27,19]
    numbersInExp=[]
    currentNum=''
    for c in exp:
        #if c is not an operator
        if c not in prec_table.keys():
            postfix+=c
            currentNum+=c
        else:
            #Append previous number in numbers Array
            if currentNum.isdigit():
                numbersInExp.append(currentNum)
            #Set current num to empty string
            currentNum=''
            #If no operator in stack, push the operator into the stack
            if st.isEmpty():
                st.push(c)
            #If outside stack precedence of current operator is greater than inside
            #precedence of operator at the stack top, push it into the stack
            elif prec_table[c][0] > prec_table[st.getTop()][1]:
                st.push(c)
            else:
                #While the operator at stack top has higher precedence than current op,
                #pop it and add it to postfix expression
                #Unless precedence is equal which only happens if current op is ')' and stack top op is '('.
                #In this case simply pop out stack top op i.e. '('
                while not st.isEmpty():
                    if prec_table[c][0] < prec_table[st.getTop()][1]:
                        postfix+=st.pop()
                    else:
                        st.pop()
                        break
                #If current op isn't ')', push it to the stack
                if c!=')':
                    st.push(c)
    #APpend last number in infix exp to numbers array
    if currentNum.isdigit():
        numbersInExp.append(currentNum)
    #Add all remaining ops in stack to postfix op         
    while(not st.isEmpty()):
        postfix+=st.pop()

    print(numbersInExp,postfix)
    ##Evalute postfix expression
    i=0
    j=0
    while i<len(postfix):
        if postfix[i].isdigit():
            st.push(numbersInExp[j])
            i+=len(numbersInExp[j])
            j+=1
        else:
            item2=st.pop()
            item1=st.pop()
            item=ops[postfix[i]](float(item1),float(item2))
            st.push(item)
            i+=1
    return round(st.pop(),2)
        
print(evaluate('(5+5)*(70-5^5)'))
print(ops['n'](5))