class SimpleClass:
    """A simple class"""

    num_of_instances = 0

    def __init__(self):
        SimpleClass.num_of_instances += 1


instance1 = SimpleClass()
instance2 = SimpleClass()

print(SimpleClass.num_of_instances)
print(instance1.num_of_instances)
print(instance2.num_of_instances)

print(f"contents of instance1: {instance1.__dict__}")
