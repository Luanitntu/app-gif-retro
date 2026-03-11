#!/usr/bin/env python3
"""
Log Management Utility
View, analyze, and manage application logs
"""

import os
import sys
from pathlib import Path
from datetime import datetime

class LogViewer:
    """Utility to view and analyze logs"""
    
    def __init__(self):
        self.log_dir = Path(__file__).parent / "GifViewerData" / "logs"
        self.app_log = self.log_dir / "app.log"
        self.error_log = self.log_dir / "error.log"
    
    def ensure_logs_exist(self):
        """Check if logs directory exists"""
        if not self.log_dir.exists():
            print(f"❌ Logs directory not found: {self.log_dir}")
            print("Run the application first to generate logs.")
            return False
        return True
    
    def view_app_log(self, lines=50):
        """View application log (last N lines)"""
        if not self.app_log.exists():
            print(f"❌ App log not found: {self.app_log}")
            return
        
        print("\n" + "="*70)
        print(f"📋 APPLICATION LOG - Last {lines} Lines")
        print("="*70 + "\n")
        
        with open(self.app_log, 'r') as f:
            all_lines = f.readlines()
            show_lines = all_lines[-lines:] if len(all_lines) > lines else all_lines
            for line in show_lines:
                self._colorize_line(line)
    
    def view_error_log(self):
        """View error log"""
        if not self.error_log.exists():
            print(f"✅ No errors found (error.log doesn't exist)")
            return
        
        print("\n" + "="*70)
        print("❌ ERROR LOG")
        print("="*70 + "\n")
        
        with open(self.error_log, 'r') as f:
            lines = f.readlines()
            if not lines:
                print("✅ No errors recorded\n")
            else:
                for line in lines:
                    self._colorize_line(line)
    
    def search_logs(self, keyword):
        """Search for keyword in logs"""
        if not self.app_log.exists():
            print(f"❌ Log file not found: {self.app_log}")
            return
        
        print(f"\n" + "="*70)
        print(f"🔍 SEARCH RESULTS FOR: '{keyword}'")
        print("="*70 + "\n")
        
        found = 0
        with open(self.app_log, 'r') as f:
            for line in f:
                if keyword.lower() in line.lower():
                    self._colorize_line(line)
                    found += 1
        
        print(f"\n📊 Found {found} matching lines\n")
    
    def view_last_session(self):
        """View last session starting from latest 'Started'"""
        if not self.app_log.exists():
            print(f"❌ Log file not found: {self.app_log}")
            return
        
        print("\n" + "="*70)
        print("📅 LAST SESSION")
        print("="*70 + "\n")
        
        with open(self.app_log, 'r') as f:
            lines = f.readlines()
            
            # Find the last "Started" line
            start_idx = 0
            for i in range(len(lines)-1, -1, -1):
                if "Started" in lines[i]:
                    start_idx = i
                    break
            
            # Show from that point
            for line in lines[start_idx:]:
                self._colorize_line(line)
    
    def get_stats(self):
        """Get log file statistics"""
        if not self.log_dir.exists():
            return
        
        print("\n" + "="*70)
        print("📊 LOG STATISTICS")
        print("="*70 + "\n")
        
        total_size = 0
        file_count = 0
        
        print("Log Files:")
        for log_file in sorted(self.log_dir.glob("*.log*")):
            size = log_file.stat().st_size
            total_size += size
            file_count += 1
            size_mb = size / (1024*1024)
            size_kb = (size % (1024*1024)) / 1024
            
            icon = "📝" if log_file.suffix == ".log" else "📦"
            print(f"  {icon} {log_file.name:<20} {size_kb:>8.1f} KB")
        
        total_mb = total_size / (1024*1024)
        print(f"\nTotal: {file_count} files, {total_mb:.1f} MB")
        print()
    
    def clear_old_logs(self, keep_current=True):
        """Clear old rotated logs"""
        if not self.log_dir.exists():
            print("No logs directory found")
            return
        
        print("\n" + "="*70)
        print("🗑️  CLEARING OLD LOGS")
        print("="*70 + "\n")
        
        removed = 0
        for log_file in self.log_dir.glob("*.log.*"):
            try:
                log_file.unlink()
                print(f"  🗑️  Removed: {log_file.name}")
                removed += 1
            except Exception as e:
                print(f"  ❌ Failed to remove {log_file.name}: {e}")
        
        print(f"\n✅ Removed {removed} old log files\n")
    
    @staticmethod
    def _colorize_line(line):
        """Print line with color based on log level"""
        # Simple coloring based on level
        if " ERROR " in line or " CRITICAL " in line:
            print(f"❌ {line.rstrip()}")
        elif " WARNING " in line:
            print(f"⚠️  {line.rstrip()}")
        elif " INFO " in line:
            print(f"ℹ️  {line.rstrip()}")
        elif " DEBUG " in line:
            print(f"🔧 {line.rstrip()}")
        else:
            print(f"   {line.rstrip()}")

def main():
    """Main menu"""
    viewer = LogViewer()
    
    if not viewer.ensure_logs_exist():
        sys.exit(1)
    
    while True:
        print("\n" + "="*70)
        print("📋 LOG VIEWER - GIF Viewer Application")
        print("="*70)
        print("\n1. View Application Log (last 50 lines)")
        print("2. View Application Log (last 100 lines)")
        print("3. View Error Log")
        print("4. View Last Session")
        print("5. Search Logs")
        print("6. Show Log Statistics")
        print("7. Clear Old Logs")
        print("8. Exit\n")
        
        choice = input("Select option (1-8): ").strip()
        
        if choice == "1":
            viewer.view_app_log(50)
        elif choice == "2":
            viewer.view_app_log(100)
        elif choice == "3":
            viewer.view_error_log()
        elif choice == "4":
            viewer.view_last_session()
        elif choice == "5":
            keyword = input("Enter search keyword: ").strip()
            if keyword:
                viewer.search_logs(keyword)
        elif choice == "6":
            viewer.get_stats()
        elif choice == "7":
            confirm = input("Clear old rotated logs? (y/n): ").strip().lower()
            if confirm == 'y':
                viewer.clear_old_logs()
        elif choice == "8":
            print("\nGoodbye! 👋\n")
            break
        else:
            print("\n❌ Invalid option\n")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Command line mode
        viewer = LogViewer()
        command = sys.argv[1].lower()
        
        if command == "view":
            lines = int(sys.argv[2]) if len(sys.argv) > 2 else 50
            viewer.view_app_log(lines)
        elif command == "errors":
            viewer.view_error_log()
        elif command == "session":
            viewer.view_last_session()
        elif command == "search":
            if len(sys.argv) > 2:
                viewer.search_logs(sys.argv[2])
        elif command == "stats":
            viewer.get_stats()
        elif command == "clean":
            viewer.clear_old_logs()
        else:
            print(f"Unknown command: {command}")
            print("\nUsage: python log_viewer.py [view|errors|session|search|stats|clean] [args]")
    else:
        # Interactive menu mode
        main()
