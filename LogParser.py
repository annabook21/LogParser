def parse_vpc_flow_logs(log_file_path):
    reject_ips = set()  # Using a set to avoid duplicate IPs
    reject_lines = []   # List to hold lines with rejected traffic
    
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            parts = line.split()  # Assuming space-separated values
            
            # Check if this line is a REJECT entry
            if 'REJECT' in parts:
                src_ip = parts[3]  # Assuming <srcaddr> is at index 3
                dst_ip = parts[4]  # Assuming <dstaddr> is at index 4
                reject_ips.update([src_ip, dst_ip])
                reject_lines.append(line)
                
    # Return the set of IPs and the list of rejected traffic lines
    return reject_ips, reject_lines

def save_reject_lines_to_file(reject_lines, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for line in reject_lines:
            output_file.write(line)

# Replace 'your_log_file.log' with the path to your actual log file
log_file_path = 'sample.log'
output_file_path = 'rejected_traffic.txt'

reject_ips, reject_lines = parse_vpc_flow_logs(log_file_path)
print("Rejected IPs:", reject_ips)
save_reject_lines_to_file(reject_lines, output_file_path)
print(f"Rejected traffic lines saved to {output_file_path}")
