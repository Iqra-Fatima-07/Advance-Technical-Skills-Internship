def power_set(s, index=0, current=""):
    if index == len(s):
        print(f"'{current}'")
        return

    power_set(s, index + 1, current + s[index])
    power_set(s, index + 1, current)

power_set("ABC")
