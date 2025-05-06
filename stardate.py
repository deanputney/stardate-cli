import os
import sys
import argparse
from datetime import datetime, timedelta
import re

def parse_time_range(time_str):
    """Parse time range string like '1d', '7d', '1w' into a timedelta."""
    if not time_str:
        return None
    
    match = re.match(r'(\d+)([dw])', time_str)
    if not match:
        raise argparse.ArgumentTypeError("Invalid time format. Use '1d', '7d', or '1w'")
    
    amount, unit = match.groups()
    amount = int(amount)
    
    if unit == 'd':
        return timedelta(days=amount)
    elif unit == 'w':
        return timedelta(weeks=amount)
    else:
        raise argparse.ArgumentTypeError("Invalid time format. Use '1d', '7d', or '1w'")

def get_files_in_time_range(directory, time_range):
    """Get files in the directory that match the time range in their filenames."""
    now = datetime.now()
    files = []
    
    for filename in os.listdir(directory):
        # Extract date from filename (assuming format "YYYY-MM-DD_...")
        match = re.match(r'(\d{4}-\d{2}-\d{2})_', filename)
        if not match:
            continue
            
        file_date_str = match.group(1)
        file_date = datetime.strptime(file_date_str, "%Y-%m-%d")
        
        if now - file_date <= time_range:
            files.append(os.path.join(directory, filename))
    
    return files

def main():
    parser = argparse.ArgumentParser(description="Search files in a specific directory and output their contents.")
    parser.add_argument("time_range", nargs="?", help="Time range to filter files (e.g., '1d', '7d', '1w')", type=parse_time_range)
    parser.add_argument("--metadata", action="store_true", help="Include metadata with file dates")
    parser.add_argument("--path", action="store_true", help="Output the fully qualified path to the directory")
    parser.add_argument("ls", nargs="?", const=True, help="List all files in the directory")
    args = parser.parse_args()
    
    # Set up directory path
    home = os.path.expanduser("~")
    directory = os.path.join(home, "Library", "Mobile Documents", "iCloud~com~deanputney~Stardate", "Documents", "Transcriptions")
    
    # Handle --path flag
    if args.path:
        print(directory)
        return
    
    # Handle 'ls' argument
    if args.ls:
        for filename in os.listdir(directory):
            print(os.path.join(directory, filename))
        return
    
    # Handle time range
    if args.time_range:
        files = get_files_in_time_range(directory, args.time_range)
    else:
        files = [os.path.join(directory, f) for f in os.listdir(directory)]
    
    # Output results
    for file_path in files:
        with open(file_path, "r") as f:
            content = f.read()
            
            if args.metadata:
                # Extract date from filename
                filename = os.path.basename(file_path)
                match = re.match(r'(\d{4}-\d{2}-\d{2})_', filename)
                if match:
                    file_date_str = match.group(1)
                    file_date = datetime.strptime(file_date_str, "%Y-%m-%d")
                    print(f"[{file_date.strftime('%Y-%m-%d %H:%M:%S')}]")
            
            print(content)
            print("\n\n")
    
if __name__ == "__main__":
    main()
