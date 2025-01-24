import os 
import sys
import datetime
from dotenv import load_dotenv

DEBUG = False

class Logger:
    def __init__(self):
        """Initializes the Logger class"""
        load_dotenv()
        self.log_path = os.getenv('LOG_PATH')
        self.log_database = os.getenv('LOG_DATABASE')
        self.debug = DEBUG
        
    def log(self, message, function, user, print_message=DEBUG, error=False, default=True):
        """Logs a message to the log file and or console."""
        # Verify the log path exists
        if self.debug:
            print_message = True

        if default:
            try:
                if not os.path.exists(self.log_path):
                    os.makedirs(self.log_path)
            except Exception as e:
                print(f"Error: {e}")
                print(f"Error: Unable to create log directory. Please check you're .ENV File Exiting...")
                sys.exit(1)
            # Create the log file
            try:
                log_file = f"{self.log_path}/SystemLog{datetime.datetime.now().date()}.txt"
                if not os.path.exists(log_file):
                    with open(log_file, 'w') as file:
                        file.write(f"System Log File | Date: {datetime.datetime.now().date()}\n")
            except Exception as e:
                print(f"Error: {e}")
                print(f"Error: Unable to create log file. Exiting...")
                sys.exit(1)

            # Create the log message
            if error:
                log_message = f"ERROR: [{datetime.datetime.now()}][{function}][{user}] {message}"
                print_message = True
            else:
                log_message = f"[{datetime.datetime.now()}][{function}][{user}] {message}"
            if print_message:
                print(log_message)
            
            # Write the log message to the log file
            try:
                with open(log_file, 'a') as file:
                    file.write(f"{log_message}\n")
            except Exception as e:
                print(f"Error: {e}")
                print(f"Error: Unable to write to log file. Exiting...")
                sys.exit(1)
        
        # Log to a seperate log file
        else:
            try:
                if not os.path.exists(self.log_path):
                    os.makedirs(self.log_path)
            except Exception as e:
                print(f"Error: {e}")
                print(f"Error: Unable to create log directory. Exiting...")
                sys.exit(1)
            # Create the log file
            try:
                log_file = f"{self.log_path}/System_Command_LOG{datetime.datetime.now().date()}.txt"
                if not os.path.exists(log_file):
                    with open(log_file, 'w') as file:
                        file.write(f"Command Execution And Uncaught Error Log File | Date: {datetime.datetime.now().date()}\n")
            except Exception as e:
                print(f"Error: {e}")
                print(f"Error: Unable to create log file. Exiting...")
                sys.exit(1)

            # Create the log message
            if error:
                log_message = f"ERROR: [{datetime.datetime.now()}][{function}][{user}] {message}"
            else:
                log_message = f"[{datetime.datetime.now()}][{function}][{user}] {message}"
            if print_message:
                print(log_message)
            
            try:
                with open(log_file, 'a') as file:
                    file.write(f"{log_message}\n")
            except Exception as e:
                print(f"Error: {e}")
                print(f"Error: Unable to write to log file. Exiting...")
                sys.exit(1)



        
        
        
