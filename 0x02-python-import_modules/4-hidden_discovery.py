#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    a = dir(hidden_4)
    for i in range(len(a) - 3, len(a)):
        print(a[i])
