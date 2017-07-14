nums = [233614, 177763, 52231, 654321]
for num in nums:
    num_string = str(num)
    done = False
    for i, c in enumerate(num_string):
        if i+2 < len(num_string) and num_string[i] > num_string[i+1] and num_string[i+1] > num_string[i+2]:
            print(num_string[:i+1] + num_string[i+2:])
            done = True
            break
    if not done:
        lsd = num_string[-1]
        s_lsd = num_string[-2]
        if lsd > s_lsd:
            print(num_string[:-2]+lsd)
        else:
            print(num_string[:-1])
