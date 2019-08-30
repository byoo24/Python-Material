a_string = "this is\na string split\t\tand tabbed"
print(a_string)

raw_string = r"this is\na string split\t\tand tabbed"
print(raw_string)

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslash_string = "this is a blackslash \\followed by text"
print(backslash_string)

error_string = r"this sstring ends with \\"