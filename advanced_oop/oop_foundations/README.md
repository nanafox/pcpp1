# OOP Foundations

## Notes

- Methods are _called_ on behalf of an object and the object is passed as
  the first argument to the method.
  - it is usually executed on object data.
- Attributes can be retrieved and defined using the `getattr()` and `setattr()`
  functions.
- The `__dict__` attribute of an object is a dictionary that contains the
  object's attributes.
- Methods are usually referred to as _callable_ attributes.
- Class variables can be used store metadata relevant to the class.
  - It becomes a _shared_ attribute.
  - It exists outside any instance
  - It is accessed this way: `<ClassName>.<attribute>`
  - It can be modified only from the class level
