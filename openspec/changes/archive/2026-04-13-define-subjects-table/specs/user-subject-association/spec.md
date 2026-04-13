## ADDED Requirements

### Requirement: Subject is associated with a user
The system SHALL ensure that each subject record is correctly associated with a user.

#### Scenario: Successful association
- **WHEN** a subject is created or updated with a valid `user_id`
- **THEN** the subject record is linked to the specified user through the `user_id` foreign key.

### Requirement: Subjects can be listed by user
The system SHALL allow for the retrieval of all subjects associated with a specific user.

#### Scenario: Successful retrieval of user's subjects
- **WHEN** a user requests a list of subjects associated with a particular `user_id`
- **THEN** the system returns all subject records that have the matching `user_id`.
