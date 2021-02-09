"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """
        Initialize starting numbers for reset and start 
        """
        self.start = start -1
        self.begin = start -1

    def __repr__(self):
        return f"SerialGenerator start= {self.begin+1} next= {self.begin+2}"

    def generate(self):
        """
        add one to start number and then return number
        """
        self.start += 1
        return self.start

    def reset(self):
        """
        Change number to original start input when counter was initialized
        """
        self.start = self.begin

    


