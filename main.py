import hashlib

class NeuralCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash   #This line will join the transaction and gives us the hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()     #This line encodes and gives us the hash for each transaction

#Transaction List
t1 = "Anna sends 2 NC to Mike"
t2 = "Bob sends 4.1 NC to Mike"
t3 = "Mike sends 3.2 NC to Bob"
t4 = "Daniel sends 0.3 NC to Anna"
t5 = "Mike sends 1 NC to Charlie"
t6 = "Mike sends 5.4 NC to Daniel"

first_block = NeuralCoinBlock("This is the first block", [t1, t2])  #This is the first block which shows the first 2 transactions

print(first_block.block_data)
print(first_block.block_hash)

second_block = NeuralCoinBlock(first_block.block_hash, [t3, t4])   #This is the second block which will show the transactions have the hash of the previous block and

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_hash, [t5, t6])  #The same applies here

print(third_block.block_data)
print(third_block.block_hash)