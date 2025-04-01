# notebooks/generate_mock_data.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import ipaddress

# Configuration
NUM_RECORDS = 10000
ATTACK_RATIO = 0.1 # 10% of records will be attacks
START_TIME = datetime(2025, 4, 1, 0, 0, 0)
TIME_INCREMENT_SECONDS = 0.5 # Average time between records

# Possible values
PROTOCOLS = ['TCP', 'UDP', 'ICMP']
COMMON_PORTS = [80, 443, 502, 20000, 19999, 102] # Common web/SCADA ports
ATTACK_TYPES = ['Scan', 'DoS', 'Injection'] # Simple attack types for labeling

# Generate IP addresses (mix of private and public for simulation)
def generate_ips(n):
    ips = []
    for _ in range(n // 2):
        ips.append(str(ipaddress.IPv4Address(random.randint(0xC0A80000, 0xC0A8FFFF)))) # 192.168.x.x
    for _ in range(n - (n // 2)):
         ips.append(str(ipaddress.IPv4Address(random.randint(0x0A000000, 0xEFFFFFFF)))) # Mix of public ranges
    random.shuffle(ips)
    return ips

src_ips = generate_ips(NUM_RECORDS)
dst_ips = generate_ips(NUM_RECORDS)

# Generate timestamps
timestamps = [START_TIME + timedelta(seconds=i * TIME_INCREMENT_SECONDS + random.uniform(-0.2, 0.2)) for i in range(NUM_RECORDS)]

# Generate other features
src_ports = np.random.randint(1024, 65535, NUM_RECORDS)
dst_ports = np.random.choice(COMMON_PORTS + list(range(1024, 2048)), NUM_RECORDS) # Mix common and others
protocols = np.random.choice(PROTOCOLS, NUM_RECORDS, p=[0.6, 0.3, 0.1]) # TCP more common
packet_counts = np.random.randint(1, 100, NUM_RECORDS)
byte_counts = packet_counts * np.random.randint(40, 1500) # Bytes roughly proportional to packets

# Generate labels
num_attacks = int(NUM_RECORDS * ATTACK_RATIO)
labels = ['Normal'] * (NUM_RECORDS - num_attacks) + random.choices(ATTACK_TYPES, k=num_attacks)
random.shuffle(labels)

# Adjust features for attacks (simple simulation)
for i in range(NUM_RECORDS):
    if labels[i] == 'Scan':
        packet_counts[i] = random.randint(1, 5) # Scans often have few packets
        byte_counts[i] = packet_counts[i] * random.randint(40, 100)
        dst_ports[i] = random.randint(1, 1024) # Scan common low ports
    elif labels[i] == 'DoS':
        packet_counts[i] = random.randint(500, 5000) # DoS has many packets
        byte_counts[i] = packet_counts[i] * random.randint(60, 200)
        protocols[i] = random.choice(['UDP', 'ICMP']) # Often UDP or ICMP floods
    elif labels[i] == 'Injection':
         byte_counts[i] = random.randint(500, 3000) # Injection might have larger payloads
         dst_ports[i] = random.choice([80, 443, 502]) # Target common service ports

# Create DataFrame
df = pd.DataFrame({
    'timestamp': timestamps,
    'src_ip': src_ips,
    'dst_ip': dst_ips,
    'src_port': src_ports,
    'dst_port': dst_ports,
    'protocol': protocols,
    'packet_count': packet_counts,
    'byte_count': byte_counts,
    'label': labels
})

# Save to CSV
output_path = '../data/raw/mock_scada_data.csv'
df.to_csv(output_path, index=False)

print(f"Generated {NUM_RECORDS} mock records and saved to {output_path}")
print(f"Label distribution:\n{df['label'].value_counts()}")
