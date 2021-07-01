## Hash Maps

Just an exercise of making a hash map.

1. Create Hash
2. Compress the hash using modulo
3. Adding a value can have the following scenarios:
   1. The array element can be empty: simply ADD.
   2. The array element can have the same key: UPDATE.
   3. The array element can hav different key:
      1. Hash collision! Resolve it. I used Linear Probing here.
      2. With a new hash code, go back to 3-1.
4. Retrieving is similar:
   1. The array element can be empty: return None (Null, etc.).
   2. The array element can have the same key: return the value!
   3. The array element can hav different key:
      1. Hash collision; resolve.
      2. With a new hash code, go back to 3-1.

## Improvements

As this is a very basic model, it can be improved in many ways.

1. It can have more methods such as delete;
2. Linear probing should check if the index reached the end of the array, in which case should go back to index 0.
3. Definitely need a better hashing function.
