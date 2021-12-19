import math

def parse_header(bits_iter):
    version = "".join(next(bits_iter) for _ in range(3))
    type_id = "".join(next(bits_iter) for _ in range(3))
    return int(version, 2), int(type_id, 2), 6

def parse_value(bits_iter):
    value_bits = []
    more = True
    while more:
        bits = "".join(next(bits_iter) for _ in range(5))
        value_bits.append(bits[1:])
        more = bits[0] == '1'
    bits_consumed = 5*len(value_bits)
    return int("".join(value_bits), 2), bits_consumed

def calculate_value(packet_type, values_list):
    if packet_type == 0:
        return sum(values_list)
    elif packet_type == 1:
        return math.prod(values_list)
    elif packet_type == 2:
        return min(values_list)
    elif packet_type == 3:
        return max(values_list)
    elif packet_type == 5:
        assert len(values_list) == 2
        return int(values_list[0] > values_list[1])
    elif packet_type == 6:
        assert len(values_list) == 2
        return int(values_list[0] < values_list[1])
    elif packet_type == 7:
        assert len(values_list) == 2
        return int(values_list[0] == values_list[1])


def parse(bits_iter, con=0):
    version, packet_type, cons = parse_header(bits_iter)
    print('version', version)
    con += cons
    if packet_type == 4:  # it's a value
        value, consumed = parse_value(bits_iter)
        print('value', value)
        return version, packet_type, value, con+consumed

    else:  # it's an operator
        length_type_id = next(bits_iter)
        con += 1
        if length_type_id == '0':
            total_length = int(''.join(next(bits_iter) for _ in range(15)), 2)
            con += 15
            total_consumed = 0
            values = []
            while total_consumed < total_length:
                version2, packet_type2, value, consumed = parse(bits_iter)
                total_consumed += consumed
                values.append(value)
            return version, packet_type, calculate_value(packet_type, values), con+total_consumed

        elif length_type_id == '1':
            subpacket_count = int(''.join(next(bits_iter) for _ in range(11)), 2)
            con += 11
            total_consumed = 0
            values = []
            for _ in range(subpacket_count):
                version2, packet_type2, value, consumed = parse(bits_iter)
                total_consumed += consumed
                values.append(value)
            return version, packet_type, calculate_value(packet_type, values), con + total_consumed
    return

#with open('16.in') as file:
#    bits = file.read().strip()
bits = input().strip()
bits = bin(int(bits, 16))[2:]
bits = bits.zfill(math.ceil(len(bits)/4)*4)
#print(bits)
print('len', len(bits))
i = iter(bits)
print(parse(i))
l = list(i)
print(len(l))
assert all(t == '0' for t in l)
