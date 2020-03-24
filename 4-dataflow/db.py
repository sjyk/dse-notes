'''
This module define a basic set of relational algebra operators.
Relational algebra, first created by Edgar F. Codd while at IBM, 
is a family of algebras with a well-founded semantics used for 
modelling the data stored in relational databases, and defining 
queries on it. The main application of relational algebra is 
providing a theoretical foundation for relational databases, 
particularly query languages for such databases, chief among 
which is SQL.
'''


#First, we define a helper class "Load" which retrieves
#files off disk
class Load:
    """The Load operator loads a file in line by line. It 
    uses the first line of the file as the attribute names
    """

    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        '''
        This is similar to the FileScan operator seen in
        class. But it uses the first line to assign real 
        names to the fields.
        '''
        self.file = open(self.filename, 'r')
        self.schema = self.file.readline().split(",")
        line = self.file.readline().split(",")
        self.line = self.line2dict(line)
        return self

    def __next__(self):
        '''
        Calls line2dict to transform the line into a dict with 
        named fields
        '''
        if self.line != None:
            result = self.line
            self.line = self.line2dict(self.file.readline().split(","))
            return result
        else:
            raise StopIteration


    def line2dict(self, line):
        '''
        The main subroutine that transforms the line
        into a dict with named fields. Returns None if
        there are any errors
        '''
        if len(line) != len(self.schema):
            return None

        return {self.schema[i].strip():v.strip() \
                for i,v in enumerate(line)}



#Now, we define the relational algebra operators

class Select:
    '''The selection operator retrievs all tuples 
       in R for which a condition θ holds. Conditions
       are specified as boolean functions over tuples:

       E.g.,

       lambda x: x['attr'] == 5 # all tuples where x['attr'] is 5
       lambda x: x['attr1'] > x['attr2'] # all tuples where x['attr1'] is greater than x['attr2']  
    '''

    def __init__(self, iter_in, condition):
        self.iter_in = iter_in
        self.condition = condition

    def __iter__(self):
        self.input_state = iter(self.iter_in)
        return self
    
    def __next__(self):
        '''
        Note the similarities with the Filter operator
        '''
        elem = next(self.input_state)

        if not self.condition(elem):
            return self.__next__() #Recursive, whoa!

        return elem



class Project:
    '''
    A relational algebra projection operation picks a subset of 
    all available attributes and restricts each tuple to that subset. 
    For example, if the attributes are (name, age), then projection 
    of the relation {(Alice, 5), (Bob, 8)} onto attribute 
    list (age) yields {5,8} – we have discarded the names, 
    and only know what ages are present.
    '''

    def __init__(self, input, attrs):
        self.iter_in = input
        self.attrs = attrs   
        
    def __iter__(self):
        self.input_state = iter(self.iter_in)
        return self
    
    def __next__(self):
        elem = next(self.input_state)    
        return {a:elem[a] for a in self.attrs}

class Join:
    '''
    A join operation returns all pairs of tuples that 
    satisfy some condition across input iterators. It
    can be thought of the sequential composition of the
    Cartesian operator (all pairs) and the Selec 
    operator.
    '''

    def __init__(self, input, condition):
        '''
        Takes in a tuple of input iterators (i1,i2)
        '''
        self.condition = condition
        self.cart = Cartesian(input)
        self.join = Select(self.cart, condition)

    def __iter__(self):
        self.input_state = iter(self.join)
        return self

    def __next__(self):
        return next(self.input_state)


class Cartesian:
    '''
    Returns all pairs of two iterators. This is 
    very similar to the MatchOperator seen in class
    before
    '''

    def __init__(self, input):
        '''
        Takes in a tuple of input iterators (i1,i2)
        '''
        self.in1, self.in2 = input
        # a list of iterators
        
    def __iter__(self):
        '''
        Initializes the iterators and fetches the first element
        '''

        self.it1 = iter(self.in1) # initialize the first input
        self.it2 = iter(self.in2) # initialize the second input
        
        self.i = next(self.it1)
        self.j = next(self.it2)
        
        return self


    """
    Below are two helper methods. Conceptually,
    we are running the following patter:
    for i in it1:
        for j in it2:
            if j == i:
                return (i,j)
    To implement this with iterators, we need two
    helper methods _reset_or_inc2 (go back to the
    beginning of the inner for loop), or _inc1_or_end
    (increment the first for loop or stop)
    """

    def _reset_or_inc2(self):
        try:
            self.j = next(self.it2)

        except StopIteration:
            self.it2 = iter(self.in2)
            self.j = next(self.it2)
            self._inc1_or_end()

    def _inc1_or_end(self):
        try:
            self.i = next(self.it1)
        except StopIteration:
            self.i = None
            self.j = None


    def __next__(self):
        '''
        The next method fetches the next element
        '''

        rtn = (self.i, self.j)

        self._reset_or_inc2()

        # skip non-pairs
        if rtn[0] == None:
            raise StopIteration()

        rtn[0].update(rtn[1])

        return rtn[0]



