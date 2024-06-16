"""
Lab 1

Scenario
    * create a class representing a mobile phone;
    * your class should implement  the following methods:
        * __init__ expects a number to be passed as an argument; this method
        stores the number in an instance variable `self.number`
        * turn_on() should return the message 'mobile phone {number} is
        turned on'.
        turn_off() should return the message 'mobile phone is turned off';
        call(number) should return the message 'calling {number}'.
"""

from time import sleep


class MobilePhone:
    """A simple blueprint for mobile phone."""

    def __init__(self, number: str):
        self.number = number

    def turn_on(self):
        return f"mobile phone {self.number} is turned on"

    @staticmethod
    def turn_off():
        return "mobile phone is turned off"

    def call(self):
        return f"calling {self.number}"


if __name__ == "__main__":
    mobile_1 = MobilePhone("012-345-6789")
    mobile_2 = MobilePhone("012-555-8833")

    mobile_phones = [mobile_1, mobile_2]

    for mobile_phone in mobile_phones:
        print(mobile_phone.turn_on())
        sleep(0.25)
        print(mobile_phone.call())
        sleep(0.25)
        print(mobile_phone.turn_off())
