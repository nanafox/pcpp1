"""
Lab 3 - Classes and inheritance


Scenario

    - Your task is to build a multifunction device (MFD) class consisting of
    methods responsible for document scanning, printing, and sending via fax.
    - The methods are delivered by the following classes:
        - `scan()`, delivered by the Scanner class;
        - `print()`, delivered by the Printer class;
        - `send()` and print(), delivered by the Fax class.
    - Each method should print a message indicating its purpose and origin,
      like:
        - 'print() method from Printer class'
        - 'send() method from Fax class'
"""


class Scanner:
    """A simple Scanner class."""

    def scan(self):
        """Prints a message stating the origin of the scan."""
        print("scan() method from Scanner class")


class Printer:
    """A simple Printer class."""

    def print(self):
        """Prints a message stating the origin of the print."""
        print("print() method from Printer class")


class Fax:
    """A simple Fax class."""

    def print(self):
        """Prints a message stating the origin of the print."""
        print("print() method from Fax class")

    def send(self):
        """Prints a message stating the origin of the send."""
        print("send() method from Fax class")


class MFD_SPF(Scanner, Printer, Fax):
    """A simple class to illustrate inheritance

    It inherits from the Scanner class, then the Printer class, then the Fax
    class.
    This order is important as it affects the MRO (Method Resolution Order)
    """
    pass


class MFD_SFP(Scanner, Fax, Printer):
    """A simple class to illustrate inheritance

    It inherits from the Scanner class, then the Fax class, then the Printer
    class. By so doing, the MRO is affected when calling methods that appear
    in two different methods.
    """
    pass


if __name__ == "__main__":
    # SPF instance
    spf = MFD_SPF()
    spf.scan()
    spf.print()
    spf.send()

    # SFP instance
    sfp = MFD_SFP()
    sfp.scan()
    sfp.print()
    sfp.send()
