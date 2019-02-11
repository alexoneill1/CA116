def callme04(x):
    try:
        y = 1/x
    except ValueError:
        print('In exception handler')
    else:
        print('Reached end of try')
    finally:
        print('Exiting the function')
    return y

print(callme04(1))
print(callme04(0))
