import traceback

def spam():
    bacon()

def bacon():
    raise Exception("This is the error message.")

def main():
    spam()

if __name__ == "__main__":
    try:
        main()
    except:
        with open('error_info.txt', 'w') as _handler:
            _handler.write(traceback.format_exc())

        print('The traceback info was written to error_info.txt')

