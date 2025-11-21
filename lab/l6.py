def parse_address(address):
    part = address.split(",")
    if len(part) != 4:
        raise ValueError("Invalid address format")
    return { "street": part[0].strip(), "city": part[1].strip(), "state": part[2].strip(), "zip": part[3].strip() }
print(parse_address("123 Main St, Springfield, IL, 62704"))