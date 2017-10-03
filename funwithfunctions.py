Number is 1.  This is an odd number.
Number is 2.  This is an even number.
Number is 3.  This is an odd number.
...
Number is 2000.  This is an even number.


def main():
        # Enter the high integer
        high = int(input('Enter the high integer for the range: '))
        # Enter the lower integer
        low = int(input('Enter the low integer for the range: '))
        # Enter integer to find multiples
        num = int(input('Enter the integer for the multiples: '))
        def show_multiples():
                # Find the multiples of integer
                # and print them on same line
                for x in range(high, low, -1):
                        if (x % num) == 0:
                                print(x, end=' ')
                def isEven(x):
                        count = 0
                        total = 0
                        for count in range():
                                if (x % 2) == 0:
                                        count = count + 1
                                else:
                                        count = count + 1

                        print(count, 'even numbers total to')
                        print(count, 'odd numbers total to')
                isEven(x)
        show_multiples()
main()

