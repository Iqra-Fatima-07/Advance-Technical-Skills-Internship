def permute(s, path=""):

    if len(s) == 0:
        print(path)
        return

    for i in range(len(s)):

        picked = s[i]

        remainder = s[:i] + s[i+1:]

        permute(remainder, path + picked)


permute("ABC")
