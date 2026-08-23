class SimpleDB:
    def __init__(self):
        self.tables = {"users": []}

    def insert(self, table, record):
        if table not in self.tables:
            raise ValueError(f"Table '{table}' does not exist")
        self.tables[table].append(record)
        return len(self.tables[table])

    def count(self, table):
        return len(self.tables.get(table, []))

    def find_by_id(self, table, record_id):
        for record in self.tables.get(table, []):
            if record.get("id") == record_id:
                return record
        return None


if __name__ == "__main__":
    db = SimpleDB()

    db.insert("users", {"id": 1, "name": "Jenkins"})
    db.insert("users", {"id": 2, "name": "Docker"})

    count = db.count("users")
    print(f"✅ DB initialized. Row count: {count}")

    user = db.find_by_id("users", 1)
    print(f"✅ Lookup check: found user -> {user}")

    assert count == 2, "Expected 2 seeded rows"
    assert user is not None, "Expected to find user with id=1"
    print("✅ DB validation passed")