# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Norbert')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("Open the file")
print("--------------------------------------")

a = open("demo.txt", "r")
print(a.read())
a.close()

print("Open the file using - with")
print("--------------------------------------")

with open("demo.txt") as myFile:
    contents = myFile.read()
    print(contents)

print("Open the file - write a new line")
print("--------------------------------------")

a = open("demo.txt", "a")
a.write("\nThis is my new message here.")
a.close()

a = open("demo.txt", "r")
print(a.read())
a.close()


print("Open the file - create a new line")
print("--------------------------------------")

# create a new file named "newFile"

# x = open("newFile", "x")
# x.close

x = open("newFile", "a")
b = 1
while b <= 4:
    x.write("\nThis is a new line in the new file." + str(b) + '\n')
    b += 1
x.close()

x=open("newFile", "r")
print(x.read())
x.close()
