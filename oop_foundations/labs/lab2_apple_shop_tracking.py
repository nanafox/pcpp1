"""
Lab 2

Scenario

Imagine that you receive a task description of an application that monitors
the process of apple packaging before the apples are sent to a shop.

A shop owner has asked for 1000 apples, but the total weight limitation cannot
exceed 300 units.

Write a code that creates objects representing apples as long as both
limitations are met. When any limitation is exceeded, then the packaging
process is stopped, and your application should print the number of apple
class objects created, and the total weight.

Your application should keep track of two parameters:
    * the number of apples processed, stored as a class variable;
    * the total weight of the apples processed; stored as a class variable.
    Assume that each apple's weight is random, and can vary between
    0.2 and 0.5 of an imaginary weight unit;
"""

import random


class ApplePackage:
    """Blueprint for a fictional apple packaging shop."""

    apples_processed: int = 0
    apple_base_unit: float = random.uniform(0.2, 0.5)  # nosec
    total_weight_of_apples_processed: float = 0.0
    weight_threshold: float = 300.0
    packable_apples_threshold: int = 1000

    def __init__(self):
        ApplePackage.check_limit()
        ApplePackage.apples_processed += 1
        ApplePackage.total_weight_of_apples_processed += (
            ApplePackage.apple_base_unit
        )

        print("Apple packaged successfully.")

    @classmethod
    def check_limit(cls):
        """
        Checks to ensure the request apple can be packaged and doesn't
        violate the threshold requirements.
        """
        if (
            (cls.total_weight_of_apples_processed + cls.apple_base_unit)
            >= cls.weight_threshold
            or cls.apples_processed >= cls.packable_apples_threshold
        ):
            print("*" * 50)
            print("\nWarning: Packaging limit reached!")
            print(f"Number of apples packaged: {cls.apples_processed}")
            print(
                "Total weight of apples packaged: "
                f"{cls.total_weight_of_apples_processed:.2f}\n"
            )
            print("*" * 50)

            raise SystemExit


if __name__ == "__main__":
    for _ in range(1500):
        ApplePackage()
