# Split List into Chunks
# Split a list into chunks of size n.


#     # Input: [1, 2, 3, 4, 5, 6], n=2
#     # Output: [[1, 2], [3, 4], [5, 6]]




def split_into_chunks(lst, n):
    chunks = []
    for i in range(0, len(lst), n):
        chunks.append(lst[i:i+n])
    return chunks


lst = [1, 2, 3, 4, 5, 6]
n = 2

result = split_into_chunks(lst, n)
print(result)