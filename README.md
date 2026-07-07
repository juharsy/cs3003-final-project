# CS3003 Final Project — OOP E-Commerce Backend

Rebuilds the business logic from my CS4092 database project using object-oriented
design — Person/Customer/Staff inheritance hierarchy, polymorphic display methods,
and encapsulated Product pricing.

## How to Run

cd src
python3 main.py


## File Structure

- `docs/design_writeup.md` — explains the OOP design decisions and how they connect to course paradigms
- `schema.sql` / `ecommerce.db` — reused from CS4092 (same data model)
- `src/models.py` — Person, Customer, Staff, Product classes
- `src/main.py` — CLI built on top of the OOP classes
