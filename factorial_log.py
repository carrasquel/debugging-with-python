import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug(f'i is {i}, total is {total}')
    logging.debug('End of factorial (%s%%)' % (n))
    return total

if __name__ == "__main__":
    print(factorial(5))
    logging.debug('End of program')

