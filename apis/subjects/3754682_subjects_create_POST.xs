// Endpoint to create a new subject record.
api POST /
  input {
    text name
    text? teacher
    int hours
    int user_id
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
