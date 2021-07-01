# Mimic an array using List.
# Python doesn't have an array (list's memory allocation isn't contiguous)
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size #size
    self.array = [None for item in range(array_size)] #initialising the arr.

  def hash(self, key, count_collisions=0):
    # for our purpose, which is to simply create a demo of hash map
    # just use the sum of ascii codes for each char in the string.
    # ** Use linear probing to address hash collision
    key_bytes = key.encode()
    hash_code = sum(key_bytes) # hash_code made
    return hash_code + count_collisions 

  def compressor(self, hash_code):
    # Hashed value -> sensible array index
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    # the value at the array index
    current_array_value = self.array[array_index]
    
    # If None, assign!
    if current_array_value is None: 
      self.array[array_index] = [key, value]
      return
    
    # If keys match, update!
    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # Otherwise, linear probe!
    number_collisions = 1
    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1

    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
      return None

    if possible_return_value[0] == key:
      return possible_return_value[1]

    retrieval_collisions = 1

    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      retrieval_collisions += 1

    return

hash_map = HashMap(15)
hash_map.assign("gabbro", "igneous")
hash_map.assign("sandstone", "sedimentary")
hash_map.assign("gneiss", "metamorphic")
print(hash_map.retrieve("gabbro"))
print(hash_map.retrieve("sandstone"))
print(hash_map.retrieve("gneiss"))