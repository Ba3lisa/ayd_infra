import requests, os

DJANGO_ENDPOINT = os.getenv("DJANGO_ENDPOINT", "http://127.0.0.1:5000")

###################### LOGGING CONFIGURATION ######################
import logging.config
import logging
logger_file = f'{os.getenv("LOGGER_DIR", "/logs")}/CJ.log'
if not os.path.exists(logger_file):
    with open(logger_file, 'w') as f:
        pass
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': logger_file
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['file']
        }
    }
})
##################################################################

def main():
    print("RIP CJ (Carl Johnson) 2004-2004")
    print("How can I help ?")
    print("Type 'help' to see the list of commands")
    while True:
        try:
            user_input = input(">>> ")
            if user_input == "q":
                print("Goodbye")
                logging.info("Goodbye")
                break
            response = requests.post(f"{DJANGO_ENDPOINT}/bot/", json={"user_input": user_input})
            print(response.json()["message"])
            logging.info(f"User input: {user_input}")
            logging.info(f"Bot response: {response.json()['message']}")
        except KeyboardInterrupt:
            print("Bye bye")
            logging.info("Bye bye")
            break
        except Exception as e:
            print(e)
            logging.error(f"Error in main.py: {e}")
    

if __name__ == "__main__":
    main()
    


