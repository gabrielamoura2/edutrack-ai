## Why

To introduce a structured way to manage educational subjects within the system, allowing for the storage of subject details such as name, teacher, and hours, and linking them to specific users. This enables features like user-specific subject tracking and improved data organization.

## What Changes

- Introduce a new database table named `subjects`.
- The `subjects` table will have the following columns: `id` (auto-incrementing primary key), `name` (text), `teacher` (text), `hours` (integer), and `user_id` (foreign key referencing the `user` table).
- Establish a foreign key constraint linking `subjects.user_id` to `user.id`.

## Capabilities

### New Capabilities
- `subject-management`: Provides core functionality for creating, reading, updating, and deleting subject records.
- `user-subject-association`: Enables the system to link subjects to individual users, facilitating personalized subject tracking.

### Modified Capabilities
- None

## Impact

- **Database Schema**: A new `subjects` table will be added to the database.
- **Backend Logic**: New or modified backend logic will be required to handle CRUD operations for the `subjects` table and to manage the foreign key relationship with the `user` table.
- **API Endpoints**: Potential new API endpoints for interacting with subject data will need to be developed.
