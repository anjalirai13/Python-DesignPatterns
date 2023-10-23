**Structural Design Pattern:**

It is about organizing different classes and objects to form larger structures and provide new functionalities whilekeeping these structures flexible and efficient. 
Mostly they use inheritance to compose all the interfaces. It also identifies the relationships which led to the simplification of the structure.

**Classification**
1. Adapter Method
2. Bridge Method
3. Composite Method
4. Decorator Method
5. Proxy Method

**Brigde:**
It allows us to separate the implementation specific abstractions and implementation independent abstractions from each 
other and can be developed considering as the single entities. Bridge method is always considered as one of the best 
methods to organize the class hierarchy.

**Composite:**
It describes a group of objects that is treated the same way as a single instance of the same type of the objects. The 
purpose of the composite method is to compose objects into three type structures to represent whole partial hierarchies. 
One of the main advantages of using the composite method is that first, it allows you to compose the objects into the 
trees structure and then work with these structures as an individual object or an entity.

**Adapter:**
It helps us in making the incompatible objects adaptable to each other. The Adapter method is one of the easiest methods
to understand because we have lot of real life examples that show the analogy with it. The main purpose of this method 
is to create a bridge b/w 2 incompatible interfaces. This method provides a different interface for a class.

**Proxy:**
It allows you to provide the replacement for an another object. Here we use different classes to represent the 
functionalities of another class. The most important part is that we create an object, having original object functionality
to provide to outer world. The meaning of word Proxy is "in place" or "on behalf of" that directly explains the Proxy method.

**Decorator:**
It allows you to dynamically attach new behaviors to object without changing their implementations by placing those 
objects inside the wrapper object that contains the behaviors. It is much easier to implement Decorator method in Python 
because of its built-in feature. It is not equivalent to the inheritance because the new feature is added only to that 
particular object, not the entire subclass.  