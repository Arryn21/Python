def calculate_usable_ips(subnet_mask_length):
    total_addresses = 2 ** (32 - subnet_mask_length)
    usable_ips = total_addresses - 2
    return usable_ips


def calculate_network_and_broadcast(subnet_mask_length):
    total_addresses = 2 ** (32 - subnet_mask_length)
    network_address = 0  # In decimal, the network address has all zeros in the host portion
    broadcast_address = total_addresses - 1  # In decimal, the broadcast address has all ones in the host portion
    return network_address, broadcast_address


def main():
    try:
        subnet_mask_length = int(input("Enter the subnet mask length (0-32): "))
        if 0 <= subnet_mask_length <= 32:
            usable_ips = calculate_usable_ips(subnet_mask_length)
            network_address, broadcast_address = calculate_network_and_broadcast(subnet_mask_length)

            print(f"Number of usable IPs in the subnet: {usable_ips}")
            print(f"Network Address: {network_address}")
            print(f"Broadcast Address: {broadcast_address}")
        else:
            print("Subnet mask length must be in the range of 0-32.")
    except ValueError:
        print("Please enter a valid integer for the subnet mask length.")


if __name__ == "__main__":
    main()
