#!/usr/bin/env python3
"""
Ticket Data Analysis Script
Analyzes helpdesk ticket data for insights and trends
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

def load_data():
    \"\"\"Load ticket data from CSV file\"\"\"
    try:
        # This will be updated when you add your actual CSV file
        df = pd.read_csv('data/ticket_data.csv')
        print(f"Loaded data with {len(df)} rows and {len(df.columns)} columns")
        return df
    except FileNotFoundError:
        print("CSV file not found. Please add your ticket data to data/ticket_data.csv")
        return None

def analyze_ticket_status(df):
    \"\"\"Analyze distribution of ticket statuses\"\"\"
    if df is not None and 'status' in df.columns:
        status_counts = df['status'].value_counts()
        print("\nTicket Status Distribution:")
        print(status_counts)
        
        # Create visualization
        plt.figure(figsize=(10, 6))
        status_counts.plot(kind='bar')
        plt.title('Ticket Status Distribution')
        plt.xlabel('Status')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('reports/status_distribution.png')
        plt.close()
        
        return status_counts
    return None

def main():
    \"\"\"Main analysis function\"\"\"
    print("Starting Ticket Data Analysis...")
    
    # Ensure reports directory exists
    os.makedirs('reports', exist_ok=True)
    os.makedirs('data', exist_ok=True)
    
    # Load data
    df = load_data()
    
    if df is not None:
        # Perform various analyses
        analyze_ticket_status(df)
        
        # Add more analysis functions here
        print("\nAnalysis complete! Check the 'reports' folder for visualizations.")
    else:
        print("\nPlease add your CSV data file to the 'data' folder.")
        print("The file should be named 'ticket_data.csv'")

if __name__ == "__main__":
    main()
