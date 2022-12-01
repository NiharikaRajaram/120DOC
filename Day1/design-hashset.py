# Using double hashing technique
# hash 1 - find bucket
# hash 2 - find items in bucket

class MyHashSet:

    def __init__(self):
        self.buckets = 100000 - 1
        self.bucket_items = 1001
        self.storage = [None] * self.buckets
    
    def getBucket(self, key):
        return key % self.buckets

    def getBucketItems(self, key):
        return key // self.bucket_items

    def add(self, key: int) -> None:
        bucket = self.getBucket(key)
        bucket_item = self.getBucketItems(key)
        if not self.storage[bucket]:
            self.storage[bucket] = [None] * self.bucket_items
        self.storage[bucket][bucket_item] = key

    def remove(self, key: int) -> None:
        bucket = self.getBucket(key)
        bucket_item = self.getBucketItems(key)
        if self.storage[bucket]:
            if self.storage[bucket][bucket_item]:
                self.storage[bucket][bucket_item] = None

    def contains(self, key: int) -> bool:
        bucket = self.getBucket(key)
        bucket_item = self.getBucketItems(key)
        if self.storage[bucket]:
            if self.storage[bucket][bucket_item] == key:
                return True
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)