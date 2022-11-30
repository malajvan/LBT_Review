import logging
import data_collection

def main():
    logging.basicConfig(filename='logger.log', level=logging.INFO)
    logging.info('Started')
    data_collection.do()
    logging.info('Finished')

if __name__ == '__main__':
    main()