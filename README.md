I want to make a command line interface for interacting with files within a specific folder on my computer. 

The directory is `/Users/deanputney/brary/Mobile\ Documents/iCloud~com~deanputney~Stardate/Documents/Transcriptions` which you could shorten to `$HOME/Library/Mobile\ Documents/iCloud~com~deanputney~Stardate/Documents/Transcriptions`. 

What I want the command line interface to do is to find files and output their contents based on some variable input. So for example, `stardate 1d` would output all the files from the last day. `stardate 7d` or `stardate 1w` would output all the files from the last month. The files can be simply concatenated with `\n\n` between the contents of each file. This command should use the titles of the files to do this filtering, NOT the created or updated at timestamps.

There should also be arguments to handle including metadata in the output. For example, each file has the date it was saved as the title. If you include a flag to include metadata (you can choose a flag), the output should show the date time from the file name before each file's contents.

Lastly, I want to package this as a homebrew package. So please do whatever is necessary to make that work.