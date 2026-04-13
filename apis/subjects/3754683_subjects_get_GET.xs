// Endpoint to retrieve a single subject record by ID.
api GET /{id}
  input {
    int id
  }
  output {
    object {
      int id
      text name
      text? teacher
      int hours
      int user_id
    }
  }
