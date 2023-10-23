**Creational Design Pattern:**

Creational patterns provide essential information regarding the class instantiation or the object instantiation. Class Creational pattern and the object creational pattern is the major categorization of the creational design patterns. While class creation pattern uses inheritance effectively in the instantiation process, object creation patterns use delegation effectively to get the job done.

**Classification**
1. Factory Method
2. Abstract Factory Method
3. Builder Method
4. Prototype Method
5. Singleton Method

**Factory:**
It allows an interface or a class to create an object, but lets subclasses decide which class or object to instantiate. 
Using the factory method, we have the best ways to create an object. Here objects are created without exposing the logic 
to the client, adn for creating the new type of object. The client uses the same common interface.

**Abstract Factory:**
It allows you to produce the families of related objects without specifying their concrete class. This pattern is 
particularly useful when the client doesn't know exactly what type to create. It is ready to introduce new variants of 
the products without breaking the existing client code.

**Builder:**
It aims to separate the construction of a complex object from its representation so that the some construction process 
can create different representations. It allows you to construct complex objects step by step. Here, using the same 
construction code, we can produce different types and representation of the object easily. 

**Prototype:**
It aims to reduce the number of classes used for an application. It allows you to copy existing objects independent of 
the concrete implementation of their classes. Generally, here the object is created by copying a prototypical instance 
during run-time.

**Singleton:**
It is one of the simplest design pattern available to us. It is a way to provide one and only one object of a particular 
type. It involves only one class to create methods and specify the objects.
It can be understood by a very simple example of database connectivity. When each object creates a unique database 
connection to the database. It will highly affect the cost and expenses of the project. So, it is always better to make 
a single connection rather than making extra irrelevant connections which can be easily done by Singleton Design Pattern.
The Singleton pattern is a design pattern that restricts the instantiation of a class to ine object.




