#!/usr/bin/env python3
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

def get_files_in_time_range(directory, time_range, reverse_sort=False):
    """
    Get files in the directory that match the time range in their filenames.
    
    Args:
        directory: The directory to search in
        time_range: The time range to filter files by
        reverse_sort: If True, sort newest first; if False, sort oldest first (chronological)
    """
    now = datetime.now()
    # Normalize 'now' to start of the day for consistent comparisons
    now_date = datetime(now.year, now.month, now.day)
    files = []
    
    for filename in os.listdir(directory):
        # Extract date from filename (assuming format "Stardate Log YYYY-MM-DD at HH.MM.SS.txt")
        match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
        if not match:
            continue
            
        file_date_str = match.group(1)
        file_date = datetime.strptime(file_date_str, "%Y-%m-%d")
        
        # Calculate days between dates (including the current day)
        days_diff = (now_date - file_date).days
        
        # If days_diff is within the time range (inclusive), include the file
        if days_diff <= time_range.days:
            files.append(os.path.join(directory, filename))
    
    # Sort files by date (chronological by default, newest first if reverse_sort=True)
    files.sort(key=lambda x: os.path.basename(x), reverse=reverse_sort)
    return files

def main():
    parser = argparse.ArgumentParser(description="Search files in a specific directory and output their contents.")
    parser.add_argument("time_range", nargs="?", help="Time range to filter files (e.g., '1d', '7d', '1w')", type=parse_time_range)
    parser.add_argument("--metadata", action="store_true", help="Include metadata with file dates")
    parser.add_argument("--path", action="store_true", help="Output the fully qualified path to the directory")
    parser.add_argument("--ls", action="store_true", help="List all files in the directory")
    parser.add_argument("--reverse", "-r", action="store_true", help="Sort files in reverse chronological order (newest first)")
    parser.add_argument("--test", action="store_true", help=argparse.SUPPRESS)  # Hidden option for testing
    args = parser.parse_args()
    
    # Set up directory path
    if args.test:
        # Use test directory for testing purposes
        directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data")
    else:
        # Use iCloud directory
        home = os.path.expanduser("~")
        directory = os.path.join(home, "Library", "Mobile Documents", "iCloud~com~deanputney~Stardate", "Documents", "Transcriptions")
    
    # Check if directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory not found: {directory}", file=sys.stderr)
        sys.exit(1)
    
    # Handle --path flag
    if args.path:
        print(directory)
        return
    
    # Handle --ls argument
    if args.ls:
        for filename in os.listdir(directory):
            print(os.path.join(directory, filename))
        return
    
    # Handle time range
    if args.time_range:
        files = get_files_in_time_range(directory, args.time_range, args.reverse)
    else:
        files = [os.path.join(directory, f) for f in os.listdir(directory)]
        # Sort files if no time range provided
        if files:
            files.sort(key=lambda x: os.path.basename(x), reverse=args.reverse)
    
    # Output results
    for file_path in files:
        with open(file_path, "r") as f:
            content = f.read()
            
            if args.metadata:
                # Extract date from filename
                filename = os.path.basename(file_path)
                match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
                if match:
                    file_date_str = match.group(1)
                    
                    # Extract time if available
                    time_match = re.search(r'at (\d{2})\.(\d{2})\.(\d{2})', filename)
                    if time_match:
                        hours = time_match.group(1)
                        minutes = time_match.group(2)
                        seconds = time_match.group(3)
                        file_date = datetime.strptime(f"{file_date_str} {hours}:{minutes}:{seconds}", "%Y-%m-%d %H:%M:%S")
                    else:
                        file_date = datetime.strptime(file_date_str, "%Y-%m-%d")
                    
                    print(f"[{file_date.strftime('%Y-%m-%d %H:%M:%S')}]")
            
            print(content)
            print("\n\n")
    
if __name__ == "__main__":
    main()
