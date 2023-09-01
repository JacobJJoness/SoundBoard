DigiB- Sound Manager
DigiB- Sound Manager is a simple Python application built using the Tkinter library for creating and managing a collection of sound files. It allows users to bind sound files to specific keys and play them with ease. This README provides an overview of the project and its features.

Table of Contents
Getting Started
Features
Usage
File Structure
Customization
Dependencies
Contributing
License
Getting Started
To run the DigiB- Sound Manager, you need Python installed on your system. Follow these steps to set up the project:

Clone or download this repository to your local machine.
Ensure you have the required dependencies installed (see Dependencies).
Create a folder named "sounds" in the project directory. This folder is used to store the audio files that you want to manage.
Add audio files (e.g., WAV, MP3, OGG) to the "sounds" folder.
Make sure to have a data.json file with the sound data (sample provided in the project).
Once you have set up the project, you can run it by executing main.py.


Features

Easily manage and play audio files.
Bind audio files to specific keys for quick playback.
Customizable appearance and themes.
Create, delete, and update audio files from within the application.
Responsive UI with scrollable frames for audio file management.


Usage

Launch the application by running main.py.
The main window will open, displaying a list of audio files (if any) and options to add more.
To add a new audio file, click the "+" button and follow the prompts.
Each audio file will be associated with a key, which you can use to play the corresponding sound.
Press the associated key to play the sound.


File Structure

The project is organized as follows:

main.py: The main application script.
sound_manager.py: Contains the SoundManager class responsible for managing sound files.
data.json: Stores data about the audio files and their bindings.
theme.json: Contains theme settings for the custom Tkinter elements.
sounds/: A folder to store audio files.
customtkinter/: A custom Tkinter library used for styling the UI.

Customization
You can customize the appearance of the application by modifying the theme.json file. It contains settings for various UI elements such as buttons, labels, and frames. Feel free to experiment with different color schemes and styles.

Dependencies
The following Python libraries are used in this project:

tkinter: The standard Python interface to the Tk GUI toolkit.
pygame: Used for sound playback.
shutil: Used for copying audio files.
json: Used for reading and writing data in JSON format.
os: Used for file operations.
threading: Used for handling sound playback in separate threads.
You can install these dependencies using pip if they are not already installed:

bash
Copy code
pip install pygame
Contributing
If you would like to contribute to this project or report issues, please open a GitHub issue or submit a pull request. Contributions and feedback are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

