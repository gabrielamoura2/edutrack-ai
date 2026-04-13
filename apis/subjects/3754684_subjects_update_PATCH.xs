// Endpoint to update an existing subject record.
api PATCH /{id}
  input {
    int id
    text? name
    text? teacher
    int? hours
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
