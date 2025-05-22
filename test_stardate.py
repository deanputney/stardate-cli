#!/usr/bin/env python3
import unittest
import os
import shutil
import re
from datetime import datetime, timedelta
import tempfile

# Import functions from stardate.py
from stardate import get_files_in_time_range, parse_time_range

class TestStardate(unittest.TestCase):
    def setUp(self):
        # Create a temporary test directory
        self.test_dir = tempfile.mkdtemp()
        
        # Get current date
        self.now = datetime.now()
        
        # Create test files with different dates - normalize to start of day
        self.now_normalized = datetime(self.now.year, self.now.month, self.now.day)
        dates = [
            self.now_normalized,  # Today
            self.now_normalized - timedelta(days=1),  # Yesterday
            self.now_normalized - timedelta(days=7),  # 1 week ago
            self.now_normalized - timedelta(days=30),  # 1 month ago
        ]
        
        self.test_files = []
        for date in dates:
            date_str = date.strftime("%Y-%m-%d")
            time_str = date.strftime("%H.%M.%S")
            file_path = os.path.join(self.test_dir, f"Stardate Log {date_str} at {time_str}.txt")
            with open(file_path, "w") as f:
                f.write(f"Test file for {date_str}")
            self.test_files.append(file_path)
    
    def tearDown(self):
        # Remove the temporary test directory
        shutil.rmtree(self.test_dir)
    
    def test_parse_time_range(self):
        # Test days
        self.assertEqual(parse_time_range("1d"), timedelta(days=1))
        self.assertEqual(parse_time_range("7d"), timedelta(days=7))
        self.assertEqual(parse_time_range("30d"), timedelta(days=30))
        
        # Test weeks
        self.assertEqual(parse_time_range("1w"), timedelta(weeks=1))
        self.assertEqual(parse_time_range("2w"), timedelta(weeks=2))
        
        # Test invalid formats
        with self.assertRaises(Exception):
            parse_time_range("1m")  # Invalid unit
        
        with self.assertRaises(Exception):
            parse_time_range("d")  # Missing number
    
    def test_get_files_in_time_range(self):
        # Test 0 day range (should return only today)
        zero_day_files = get_files_in_time_range(self.test_dir, timedelta(days=0))
        self.assertEqual(len(zero_day_files), 1)
        
        # Test 1 day range (should return today and yesterday)
        one_day_files = get_files_in_time_range(self.test_dir, timedelta(days=1))
        self.assertEqual(len(one_day_files), 2)
        
        # Test 7 day range (should return today, yesterday, and 1 week ago)
        week_files = get_files_in_time_range(self.test_dir, timedelta(days=7))
        self.assertEqual(len(week_files), 3)
        
        # Test 30 day range (should return all files)
        month_files = get_files_in_time_range(self.test_dir, timedelta(days=30))
        self.assertEqual(len(month_files), 4)
        
        # Test default sorting (chronological order - oldest first)
        oldest_date = re.search(r'(\d{4}-\d{2}-\d{2})', os.path.basename(month_files[0])).group(1)
        self.assertEqual(
            oldest_date,
            (self.now_normalized - timedelta(days=30)).strftime("%Y-%m-%d")
        )
        
    def test_reversed_sorting(self):
        # Test reverse sorting (newest first)
        month_files = get_files_in_time_range(self.test_dir, timedelta(days=30), reverse_sort=True)
        
        # First file should be the newest (today)
        newest_date = re.search(r'(\d{4}-\d{2}-\d{2})', os.path.basename(month_files[0])).group(1)
        self.assertEqual(
            newest_date,
            self.now_normalized.strftime("%Y-%m-%d")
        )
        
        # Last file should be the oldest (30 days ago)
        oldest_date = re.search(r'(\d{4}-\d{2}-\d{2})', os.path.basename(month_files[-1])).group(1)
        self.assertEqual(
            oldest_date,
            (self.now_normalized - timedelta(days=30)).strftime("%Y-%m-%d")
        )

if __name__ == "__main__":
    unittest.main()