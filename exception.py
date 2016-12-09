while True:
    try:
        number = int(input('What is your fav number?'))
        print(18/number)
        break
    except ValueError:
        print('Please input a number')
    except ZeroDivisionError:
        print('Please don\'t input zero')
    except:
        break
    finally:
        print('lol')
