# Architectural Solutions

Use these standard patterns to propose robust solutions.

## SOLID Principles

1.  **Single Responsibility Principle (SRP)**: A class should have one, and only one, reason to change.
2.  **Open/Closed Principle (OCP)**: Entities should be open for extension, but closed for modification.
3.  **Liskov Substitution Principle (LSP)**: Derived classes must be substitutable for their base classes.
4.  **Interface Segregation Principle (ISP)**: Clients should not be forced to depend on interfaces they do not use.
5.  **Dependency Inversion Principle (DIP)**: Depend on abstractions, not concretions.

## Common Design Patterns

### Creational
-   **Factory Method**: Define an interface for creating an object, but let subclasses alter the type of objects that will be created.
-   **Singleton**: Ensure a class has only one instance and provide a global point of access to it.
-   **Builder**: Construct complex objects step by step.

### Structural
-   **Adapter**: Allow incompatible interfaces to work together.
-   **Facade**: Provide a simplified interface to a library, a framework, or any other complex set of classes.
-   **Decorator**: Attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

### Behavioral
-   **Strategy**: Define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.
-   **Observer**: Define a subscription mechanism to notify multiple objects about any events that happen to the object they're observing.
-   **Command**: Turn a request into a stand-alone object that contains all information about the request.
