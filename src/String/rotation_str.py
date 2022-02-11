

def rotationalCipher(input, rotation_factor):
    # Write your code here
    ret = ""
    for c in input:
        if ord(c)>=ord("a") and ord(c)<=ord("z"):
            new_val = ord(c)+rotation_factor
            if new_val>ord("z"):
                mod = new_val%ord("z")
                new_val = ord("a")+mod
            c = chr(new_val)
        elif ord(c)>=ord("A") and ord(c)<=ord("Z"):
            new_val = ord(c)+rotation_factor
            if new_val>ord("Z"):
                mod = new_val%ord("Z")
                new_val = ord("A")+mod
            c = chr(new_val)
        elif ord(c)>=ord("0") and ord(c)<=ord("9"):
            new_val = ord(c)+rotation_factor
            if new_val>ord("9"):
                mod = new_val%ord("9")
                new_val = ord("0")+mod
            c = chr(new_val)
        ret += c

    return ret

if __name__ == "__main__":
    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotationalCipher(input_1, rotation_factor_1)
    print(output_1)
    if output_1==expected_1:
        print(True)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotationalCipher(input_2, rotation_factor_2)
    if output_2==expected_2:
        print(True)