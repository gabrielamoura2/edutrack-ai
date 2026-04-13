// Endpoint to delete a subject record.
api DELETE /{id}
  input {
    int id
  }
  output {
    object {
      bool success
      int deleted_id
    }
  }
