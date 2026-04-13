## Context

This design document outlines the technical approach for implementing a new `subjects` table within the existing system. The primary motivation is to enable the management and association of educational subjects with individual users, as detailed in the `define-subjects-table` proposal and its associated specifications. The current system includes a `user` table, which will be referenced by the new `subjects` table.

## Goals / Non-Goals

**Goals:**
- To define a robust and normalized database schema for the `subjects` table.
- To establish a clear foreign key relationship between the `subjects` table and the existing `user` table.
- To support fundamental CRUD (Create, Read, Update, Delete) operations for subject records.
- To facilitate the retrieval of subject lists pertinent to specific users.

**Non-Goals:**
- This document does not cover the implementation details of the API endpoints or backend services that will interact with the `subjects` table.
- Detailed user interface (UI) or user experience (UX) design for subject management is out of scope.
- Specific authentication and authorization rules for subject data are not covered, beyond the basic association with `user_id`.

## Decisions

- **Database Table Structure for `subjects`**:
    - The `subjects` table will be designed with the following columns:
        - `id`: Primary Key, Integer, Auto-incrementing.
        - `name`: Text/Varchar(255), Not Null. Represents the name of the subject (e.g., "Mathematics").
        - `teacher`: Text/Varchar(255), Nullable. Stores the name of the teacher for the subject.
        - `hours`: Integer, Not Null, Positive. Represents the duration or credit hours of the subject.
        - `user_id`: Integer, Not Null. Foreign Key referencing the `id` column in the `user` table.
    - **Rationale**: This structure directly addresses the requirements outlined in the proposal. Making `teacher` nullable provides flexibility as not all subjects may have an assigned teacher initially. `hours` is enforced as positive to ensure data validity.

- **Foreign Key Constraint**:
    - A foreign key constraint will be implemented on `subjects.user_id` that references `user.id`.
    - **ON DELETE Action**: `ON DELETE CASCADE` is proposed, meaning that if a user record is deleted, all associated subject records for that user will also be automatically deleted.
    - **Rationale**: Enforces referential integrity between users and their subjects. `ON DELETE CASCADE` simplifies data cleanup and is generally appropriate when subject records are considered dependent on the existence of a user.

- **Data Type Mapping**:
    - `id`: `BIGINT` or `INT` depending on expected scale, with `PRIMARY KEY` and `AUTO_INCREMENT` properties.
    - `name`: `VARCHAR(255)` or `TEXT`.
    - `teacher`: `VARCHAR(255)` or `TEXT`.
    - `hours`: `INT`.
    - `user_id`: `BIGINT` or `INT` to match the `user.id` type.
    - **Rationale**: Standard and appropriate SQL data types ensuring efficient storage and querying.

## Risks / Trade-offs

- **Risk: Accidental Data Loss with `ON DELETE CASCADE`**: If a user is inadvertently deleted, all their associated subject records will also be removed without explicit confirmation at the application layer.
    - **Mitigation**: Implement soft deletes for users or subjects at the application level, or ensure robust transactional integrity and user confirmation prompts before user deletion. For the database schema design, `ON DELETE CASCADE` is chosen for simplicity, but this specific behavior should be clearly communicated and potentially revisited if business logic dictates a different retention policy for subject data upon user deletion (e.g., `ON DELETE SET NULL`).
