import hashlib
import time

# ================= BLOCK =================
class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = ""

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        print(f"Mining block {self.index}...")
        while True:
            self.hash = self.calculate_hash()
            if self.hash[:difficulty] == "0" * difficulty:
                break
            else:
                self.nonce += 1

        print("Block mined!")
        print("Hash:", self.hash)
        print("Nonce:", self.nonce)
        print("-" * 40)


# ================= BLOCKCHAIN =================
class Blockchain:
    def __init__(self):
        self.difficulty = 4
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        genesis = Block(0, "0", "Genesis Block")
        genesis.mine_block(self.difficulty)
        return genesis

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest = self.get_latest_block()
        new_block = Block(len(self.chain), latest.hash, data)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)


# ================= TEST =================
my_chain = Blockchain()

my_chain.add_block("Transaksi A → B : 10 Coin")
my_chain.add_block("Transaksi B → C : 5 Coin")
