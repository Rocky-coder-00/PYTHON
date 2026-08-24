def str_test(str1):
    x = {"UCASE": 0, "LCASE": 0}

    for i in str1:
        if i.isupper():
            x["UCASE"] += 1

        elif i.islower():
            x["LCASE"] += 1

        else:
            pass

    print("Original String :", str1)
    print("No. of UPPER CASE characters :", x["UCASE"])
    print("No. of LOWER CASE characters :", x["LCASE"])


str_test("i am learning Functions")

