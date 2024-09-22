import os

# Configurações do Pool e Carteira
pool_url = "pool.supportxmr.com:3333"  # URL do Pool
wallet_address = "45v8rTEDqJBRuKkBpRk8foLdTnUGyDVhfcRAML9JnSdeh4pynchoF4uzVdWAnSkdKb75EAzt6SePV3bQWvvoUYP9nHAG7"  # Substitua pelo seu endereço de carteira Monero
cpu_priority = "5"
threads = "4"  # Número de threads que deseja usar

# Comando para executar o XMRig no Termux
xmrig_command = f"./xmrig -o {pool_url} -u {wallet_address} -p x --cpu-priority {cpu_priority} --threads {threads}"

# Executar o comando
os.system(xmrig_command)
