// Defines the schema for educational subjects and their association with users.
table subjects {
  schema {
    int id
    text name
    text? teacher
    int hours

    // Foreign key to the user table
    int user_id {
      table = "user"
      on_delete = "cascade"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]},
    // Add btree index for user_id to optimize lookups
    {type: "btree", field: [{name: "user_id", op: "asc"}]}
  ]
}