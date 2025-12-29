from secretsharing import SecretSharer

secret = "KRIPUPB2025"

secret_hex = secret.encode().hex()

shares = SecretSharer.split_secret(secret_hex, 3, 5)
print("Shares:", shares)

recovered_hex = SecretSharer.recover_secret(shares[:3])
recovered = bytes.fromhex(recovered_hex).decode()

print("Recovered secret:", recovered)
