## 1. Database Schema Definition

- [x] 1.1 Identify or create database migration script/mechanism for `subjects` table.
- [x] 1.2 Define `id` column: `INTEGER PRIMARY KEY AUTOINCREMENT`.
- [x] 1.3 Define `name` column: `VARCHAR(255) NOT NULL`.
- [x] 1.4 Define `teacher` column: `VARCHAR(255) NULLABLE`.
- [x] 1.5 Define `hours` column: `INTEGER NOT NULL CHECK (hours > 0)`.
- [x] 1.6 Define `user_id` column: `INTEGER NOT NULL`.
- [x] 1.7 Add foreign key constraint: `subjects.user_id` references `user.id` `ON DELETE CASCADE`.

## 2. Backend Model/Schema Implementation

- [x] 2.1 Create `Subject` model/schema in the backend (e.g., ORM model, Xano table definition).
- [x] 2.2 Map `Subject` model fields to the defined database columns and data types.
- [x] 2.3 Implement validation logic for `hours` to ensure it is a positive integer.

## 3. CRUD Operations for Subjects (subject-management)

- [x] 3.1 Implement backend function/endpoint to create a new subject record.
- [x] 3.2 Implement backend function/endpoint to retrieve a subject record by its `id`.
- [x] 3.3 Implement backend function/endpoint to update an existing subject record.
- [x] 3.4 Implement backend function/endpoint to delete a subject record by its `id`.

## 4. User-Subject Association Operations (user-subject-association)

- [x] 4.1 Implement backend function/endpoint to retrieve all subject records associated with a given `user_id`.
