# Django Backend Engineering Internship Log

This repository documents my structured engineering progression during my 8-week Backend Development Internship at TMR Consulting. It covers advanced Python programming concepts, object-oriented principles, database management systems, and building production-ready RESTful APIs using the Django REST Framework (DRF).

## Repository Roadmap

### 01_python_core_and_memory (task_1_fundamentals.py)
* **Concepts Covered:** Core data types, mutable vs. immutable objects, explicit type casting, error handling (try-except blocks), and defensive programming.
* **Key Implementation:** Engineered custom Python generators (yield) and memory-efficient data streams (read_large_file) designed to parse files line-by-line without overloading server memory.

### 02_oop_and_advanced_python (task_2_oop_decorators.py)
* **Concepts Covered:** Inheritance, overrides, encapsulation, constructors, and Python dunder methods.
* **Key Implementation:** 
  * Created custom iterators using __iter__ and __next__ workflows.
  * Designed utility functions using @staticmethod and factory creation pipelines via @classmethod.
  * Implemented object properties utilizing @property alongside implicit validation setters (@name.setter).
  * Formulated functional Python decorators (@decorator) to intercept execution paths.

### 03_django_architecture_theory (task_3_mvt_and_http.py)
* **Concepts Covered:** Virtual Environment isolation (venv), Django's MVT architectural pattern, the core request-response cycle, project-vs-app modular directory structures, and the built-in Admin panel.
* **Key Framework Realignment:** Documentation exploring the mechanics of transitioning a monolithic backend template into an API-driven application utilizing decoupled serialization and explicit HTTP verb configurations.

### 04_django_books_api
* **Concepts Covered:** Database schema design, database migrations tracking (makemigrations and migrate), and stateless routing.
* **Key Implementation:** Built a complete, standalone Books management application with:
  * Persistent SQLite3 schemas containing strict fields, null=False, and unique=True constraints.
  * Explicit, granular CRUD routing utilizing Django REST Framework Function-Based Views (FBVs).
  * Payload validation and endpoint integrity testing verified entirely through Postman.

### 05_drf_university_management
* **Concepts Covered:** Multi-table relational modeling, cascading constraints, Generic Views, nested serialization, and advanced QuerySet evaluation.
* **Key Implementation:** Developed a robust, hierarchical university administration infrastructure modeling three linked relational tables:
  * Departments -> Courses (Foreign Key validation) -> Students (Foreign Key validation).
  * Optimized API endpoints combining DRF Generics and Function-Based Views (FBVs).
  * Implemented nested object serializers and specialized QuerySet data fetch methods to prevent database overhead.
