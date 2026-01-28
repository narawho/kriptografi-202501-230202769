import hashlib
import time

# =========================
# Block
# =========================
class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
            + str(self.nonce)
        )
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(f"✅ Block {self.index} mined!")
        print(f"   Hash   : {self.hash}")
        print(f"   Nonce  : {self.nonce}\n")


# =========================
# Blockchain
# =========================
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # bisa diubah untuk eksperimen

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            previous_hash=latest_block.hash,
            data=data
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print("==============")
            print(f"Index : {block.index}")
            print(f"Time  : {block.timestamp}")
            print(f"Data  : {block.data}")
            print(f"Prev  : {block.previous_hash}")
            print(f"Hash  : {block.hash}")
            print(f"Nonce : {block.nonce}")


# =========================
# Main Program
# =========================
if __name__ == "__main__":
    tinychain = Blockchain()

    print("⛏️ Mining block 1...")
    tinychain.add_block("A -> B : 10 Coin")

    print("⛏️ Mining block 2...")
    tinychain.add_block("B -> C : 5 Coin")

    print("📦 Blockchain result:")
    tinychain.print_chain()
