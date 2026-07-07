# Design Write-Up — OOP E-Commerce Backend

## Paradigm: Object-Oriented Programming

This project reuses the database and schema from my CS4092 final project, but
rebuilds the business logic layer using core OOP principles instead of standalone
functions, to demonstrate how object-oriented design changes program structure.

## Design Decisions

**Inheritance:**
`Customer` and `Staff` both extend a shared `Person` base class, since both
represent people with an ID and a name. This avoids duplicating that logic in
both classes and reflects a real "is-a" relationship.

**Polymorphism:**
Each subclass overrides `display_info()` to show role-appropriate details —
`Customer` shows email, `Staff` shows role — while calling code can treat any
`Person` the same way without knowing which subclass it is.

**Encapsulation:**
`Product.price` is implemented as a property with a setter that rejects negative
values, protecting internal state instead of allowing direct, unchecked field
access.

**Behavior placement:**
Rather than free-floating functions, actions belong to the class responsible
for them: `Staff.add_product()` and `Staff.process_purchase()` reflect that
staff perform those actions, and `Customer.view_purchase_history()` reflects
that a customer looking up their own history is a natural method on that class.

## Comparison to Procedural Version

My CS4092 project used a purely procedural CLI — standalone functions passed
data directly. This version instead models the same domain as interacting
objects with responsibilities, which is the core imperative-to-OOP shift
discussed in the paradigm unit of this course.
