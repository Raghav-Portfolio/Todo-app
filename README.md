If you want to create an executable file in python, follow the mentioned steps:
1 Create a virtual environment. 
2. pip install pyinstaller
3. Type the following command in the terminal: ‘pyinstaller --onefile   --windowed --clean executable-gui.py’
Windowed: ensures that the executable doesn’t display a command line
Clean: it will clean up any version of the file that might have been created before

Once the file has run, it will create two new folders: "build" and "dist".
"Dist" has the desktop app which can be used directly. Moroever, it also contains the "todos" text file which tracks real time changes in the app.
