// Endpoint to retrieve all subject records for a specific user.
api GET /user/{user_id}
  input {
    int user_id
  }
  output {
    list {
      object {
        int id
        text name
        text? teacher
        int hours
        int user_id
      }
    }
  }
