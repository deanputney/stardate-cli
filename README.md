I want to make a command line interface for interacting with files within a specific folder on my computer. 

The directory is `/Users/deanputney/brary/Mobile\ Documents/iCloud~com~deanputney~Stardate/Documents/Transcriptions` which you could shorten to `$HOME/Library/Mobile\ Documents/iCloud~com~deanputney~Stardate/Documents/Transcriptions`. 

What I want the command line interface to do is to find files and output their contents based on some variable input. So for example, `stardate 1d` would output all the files from the last day. `stardate 7d` or `stardate 1w` would output all the files from the last month. The files can be simply concatenated with `\n\n` between the contents of each file. This command should use the titles of the files to do this filtering, NOT the created or updated at timestamps.

There should also be arguments to handle including metadata in the output. For example, each file has the date it was saved as the title. If you include a flag to include metadata (you can choose a flag), the output should show the date time from the file name before each file's contents.

## Installation

You can install stardate-cli using Homebrew:

```bash
brew tap deanputney/stardate
brew install stardate
```

## Usage

```bash
# Show help
stardate --help

# Show all files from the last day
stardate 1d

# Show all files from the last week with metadata
stardate --metadata 1w

# List all files in the directory
stardate --ls

# Output the path to the directory
stardate --path

# Sort files in reverse chronological order (newest first)
stardate --reverse 1d
```

## Creating a Release

To create a new release:

1. Update the version number in `create_release.sh`
2. Run `./create_release.sh` to create the tarball
3. Create a new release on GitHub and upload the tarball
4. Update the SHA256 hash in `Formula/stardate.rb`