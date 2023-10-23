**Behavioral Design Pattern**

They are all about identifying the common communication patterns between objects and realize these patterns. These patterns are concerned with algorithms and the assignment of responsibilities b/w objects

**Classification:**
1. Chain Of Responsibility
2. Observer
3. Visitor
4. Iterator
5. Strategy

**Chain Of Responsibility:**
It is behavioral design pattern and it is the object oriented version of if..elif..elif..else and make us capable to rearrange the condition
action blocks dynamically at the run time. It allows us to pass the requests along the chain of handlers. The processing is simple, whenever
any handler received the request it has 2 choices either to process it or pass it to the next handler in the chain. This pattern aims to
decouple the senders of a request from its receivers by allowing the request to move through chained receivers until it is handled.

**Observer:**
It allows you to define or create a subscription mechanism to send the notification to the multiple objects about any new event that happens
to the object they are observing. The subject is basically obsevred by multiple objects. The subject needs to be monitored and whenever there 
is a change in subject, the observers are being notified about the change. This pattern defines one to many dependencies between objects so 
that one object changes state, all of its dependents are notified and updated automatically.

**Visitor:**
It allows us to separate the algorithm from an object structure on which it operates. It helps us to add new features to an existing class 
hierarchy dynamically without changing it. All the behavioral patterns proved as the best methods to handle the communication b/w the objects. 
Similarly, it is used when we have to perform an operation on a group of similar kind of objects.

A visitor consists of 2 parts:
1. method named as Visit() implemented by the visitor an used and called for every element of the data structure.
2. visitable classes providing Accept() method that accept a visitor

**Iterator:**
It allows us to traverse the elements of the collection without taking the exposure of in-depth details of the elements. It provides a way to 
access the elements of a complex data structure sequentially without repeating them. It is used to access the elements of an aggregate object 
sequentially without exposing its underlying implementation

**Strategy:**
It allows you to define the complete family of algorithms, encapsulates each one and putting each of them into separate classes and also allows 
to interchange these objects. It is implemented in Python by dynamically replacing the content of a method defined outside the class. It enables 
selecting the algorithm at run-time. This method is also called as Policy model. 
