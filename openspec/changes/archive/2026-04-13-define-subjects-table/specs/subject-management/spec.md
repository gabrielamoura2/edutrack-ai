## ADDED Requirements

### Requirement: Subject can be created
The system SHALL allow for the creation of new subject records.

#### Scenario: Successful subject creation
- **WHEN** a user provides valid subject details including name, teacher, hours, and a valid user_id
- **THEN** a new subject record is added to the `subjects` table, and the system returns the ID of the newly created subject.

### Requirement: Subject can be retrieved by ID
The system SHALL allow for the retrieval of a specific subject record using its unique identifier.

#### Scenario: Successful subject retrieval
- **WHEN** a user requests a subject by providing its valid ID
- **THEN** the system returns the complete details of the corresponding subject.

### Requirement: Subject details can be updated
The system SHALL allow for the modification of an existing subject's details.

#### Scenario: Successful subject update
- **WHEN** a user provides updated details for an existing subject, identified by its ID
- **THEN** the subject's record in the `subjects` table is modified with the new details, and the system confirms the update.

### Requirement: Subject can be deleted
The system SHALL allow for the removal of a subject record.

#### Scenario: Successful subject deletion
- **WHEN** a user requests to delete a subject by providing its valid ID
- **THEN** the subject record is permanently removed from the `subjects` table, and the system confirms the deletion.
