# assigns four raw format strings to the variable formatter
formatter = "%r %r %r %r"

# assigns the integers 1 through four to the format strings called by the variable formatter
# prints the value assigned to the variable formatter to the command line
print formatter % (1, 2, 3, 4)
# assigns the strings one through four to the format strings called by the variable formatter
# prints the value assigned to the variable formatter to the command line
print formatter % ("one", "two", "three", "four")
# assigns the boolean values True False False True to the format strings called by the variable formatter
# prints the value assigned to the variable formatter to the command line
print formatter % (True, False, False, True)
# assigns the value formatter to the format strings called by the variable formatter
# prints the value assigned to the variable formatter to the command line
print formatter % (formatter, formatter, formatter, formatter)
# assigns four lines of string to the format strings called by the variable formatter
# prints the value assigned to the variable formatter to the command line
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
