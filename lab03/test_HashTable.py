from lab03.HashTable import HashTable


class TestHashTable:
    size = 10

    def test_get_size(self):
        hash_table = HashTable(self.size)

        assert hash_table.getSize() == self.size

    def test_add(self):
        hash_table = HashTable(self.size)

        keyword1 = "read"
        hash_table.add(keyword1)
        assert hash_table.contains(keyword1)

        keyword2 = "write"
        hash_table.add(keyword2)
        assert hash_table.contains(keyword2)

    def test_contains(self):
        hash_table = HashTable(self.size)

        keyword1 = "read"
        keyword2 = "write"
        assert hash_table.contains(keyword1) is False
        assert hash_table.contains(keyword2) is False

        hash_table.add(keyword1)
        assert hash_table.contains(keyword1) is True

        hash_table.add(keyword2)
        assert hash_table.contains(keyword2) is True

    def test_remove(self):
        hash_table = HashTable(self.size)

        keyword1 = "read"
        keyword2 = "write"
        assert hash_table.contains(keyword1) is False
        assert hash_table.contains(keyword2) is False

        hash_table.add(keyword1)
        assert hash_table.contains(keyword1) is True

        hash_table.remove(keyword1)
        assert hash_table.contains(keyword1) is False

        hash_table.add(keyword2)
        assert hash_table.contains(keyword2) is True

        hash_table.remove(keyword2)
        assert hash_table.contains(keyword2) is False
