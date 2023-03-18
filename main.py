# Import the necessary libraries and modules
from App import App
import pygame


def main():
    # Create an instance of the MainAppClass
    app = App(1920, 1080, "Luminous Forces v0.1")
    app.run()


# Check if the script is being executed directly, and if so, call the main function
if __name__ == "__main__":
    main()
