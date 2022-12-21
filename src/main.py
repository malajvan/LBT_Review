import logging
import data_collection

def main():
    logging.basicConfig(filename='logger.log', level=logging.INFO)
    logging.info('Started')
    data_collection.retrieve_data()
    logging.info('Finished')

if __name__ == '__main__':
    main()