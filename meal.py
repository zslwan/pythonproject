"""
Module for making meals in Python.
Import this module and then call
"""
__all__ = ['Meal','AngryChefException','makeBreakfast','Breakfast']

#Helper functions.

def makeBreakfast():
    """Creates a Breakfast object."""
    return Breakfast()
#Exception
class SensitiveArtistException(Exception):
    """Exception raised by an overly-sensitive artist."""
    pass
class AngryChefException(SensitiveArtistException):
    pass
class Meal:
    """Holds the food and drink used in a meal."""
    def __init__(self,food='omelet',drink='coffee'):
        """Initialize to default values"""
        self.name = 'generic meal'
        self.food = food
        self.drink = drink
    def printIt(self,prefix=''):
        """print the data nicely."""
        print(prefix,'A fine',self.name,'with',self.food,'and',self.drink)
    def setFood(self,food='omelet'):
        self.food = food
    def setName(self,name=''):
        self.name = name

class Breakfast(Meal):
    """Holds the food and drink for breakfast"""
    def __init__(self):
        """Initialize with an omelet and coffee."""
        Meal.__init__(self,'omelet','coffee')
        self.setName('breakfast')

def test():
    """the function"""
    print ('Module meal test')
    print('Testing meal class')
    m = Meal()
    m.printIt("\t")
    m = Meal('green eggs','tea')
   # m.printIt("\t")
    print('Testing Breakfast class')
    b = Breakfast()
    b.printIt("\t")

if __name__ == '__main__':
    test()


