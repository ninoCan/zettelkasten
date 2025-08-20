---
date: 2025-08-20T07:14:08
source: [https://refactoring.guru/design-patterns/strategy, https://www.linkedin.com/learning/programming-foundations-design-patterns-2/exploring-the-strategy-pattern, https://search.worldcat.org/title/1224279001]
tags: ["Software Design", "Design Pattern", "Behavioural Pattern"]
---

# 000-000-00B: Strategy pattern

This pattern extract the implementation of multiple behaviours out of a parent class into a separate family of Interface-Traits hierarchy.
The strategy is then incorporated into the parent class through composition, and the parent delegates the action to it.
 The child class set the concrete strategy as property, making thus the chosen algorithm interchangeable.

```mermaid
---
config:
  look: neo
  layout: dagre
title: Strategy Pattern
---
classDiagram
direction TB
    namespace Algorithm {
        class Strategy {
            action()
        }
        class Implementation1 {
            action()
        }
        class Implementation2 {
            action()
        }
    }

    class Parent {
	    strategy Strategy
	    - setStrategy()
	    + performAction()
    }
    class Child1 {
        - strategy
	    + performAction()
    }
    class Child2 {
        - strategy
	    + performAction()
    }
    class Child3 {
        - strategy
	    + performAction()
    }

	<<interface>> Strategy

    Parent *-- Strategy : Has-a
    Strategy <|.. Implementation1 : Implements
    Strategy <|.. Implementation2 : Implements
    Parent <|-- Child1 : Is-a
    Parent <|-- Child2 : Is-a
    Parent <|-- Child3 : Is-a


```


## connections:
<!-- Example
[anchor]: <link> "title"
-->
