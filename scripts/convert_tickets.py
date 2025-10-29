# convert_tickets.py
import xml.etree.ElementTree as ET
import pandas as pd
import os

def convert_xml_to_csv(xml_file_path, csv_file_path):
    """
    Convert XML ticket data to CSV format for the TicketDataAnalysis project
    """
    try:
        print("Starting XML to CSV conversion...")
        
        # Parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        
        print("✓ XML file parsed successfully")
        
        # Extract data from results
        data = []
        for result in root.find('results'):
            row = {}
            for field in result:
                key = field.attrib['key']
                value = field.text if field.text else ''
                row[key] = value
            data.append(row)
        
        # Create DataFrame
        df = pd.DataFrame(data)
        
        print(f"✓ Processed {len(df)} ticket records")
        
        # Define expected columns
        expected_columns = ['status', 'subject', 'ticketClassification_categories', 
                          'owner_last_name', 'org_accountid', 'group_id', 
                          'closed', 'assignedTsr', 'org_serviceLevel']
        
        # Add missing columns with empty values
        for col in expected_columns:
            if col not in df.columns:
                df[col] = ''
        
        # Reorder columns
        df = df[expected_columns]
        
        # Save to CSV
        df.to_csv(csv_file_path, index=False)
        
        print(f"✓ CSV file saved successfully!")
        print(f"📁 Location: {csv_file_path}")
        
        # Display summary statistics
        print("\n📊 Data Summary:")
        print(f"   Total tickets: {len(df)}")
        print(f"   Status distribution:")
        status_counts = df['status'].value_counts()
        for status, count in status_counts.items():
            print(f"     - {status}: {count}")
        
        print(f"   Columns: {', '.join(df.columns)}")
        
        return df
        
    except FileNotFoundError:
        print(f"❌ Error: XML file not found at {xml_file_path}")
        return None
    except Exception as e:
        print(f"❌ Error converting XML to CSV: {e}")
        return None

def main():
    print("=" * 60)
    print("   TICKET DATA CONVERSION TOOL")
    print("   Scripts Folder Edition")
    print("=" * 60)
    
    # Define file paths - all files are in scripts folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    xml_file_path = os.path.join(current_dir, "Rawfileticket.txt")
    csv_file_path = os.path.join(current_dir, "..", "data", "ticket_data.csv")
    
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)
    print(f"✓ Data directory ready: {os.path.dirname(csv_file_path)}")
    
    # Check if XML file exists
    if not os.path.exists(xml_file_path):
        print(f"❌ XML file not found at: {xml_file_path}")
        print(f"📁 Current directory: {current_dir}")
        print(f"📁 Files in current directory: {os.listdir(current_dir)}")
        return
    
    print(f"✓ Found XML file: {xml_file_path}")
    
    # Convert XML to CSV
    print(f"\n🔄 Converting XML to CSV...")
    df = convert_xml_to_csv(xml_file_path, csv_file_path)
    
    if df is not None:
        print("\n🎉 Conversion completed successfully!")
        print("\n➡️  Next steps:")
        print("   1. Run analysis: python analyze_tickets.py")
        print("   2. Check the 'reports' folder for visualizations")
        print("   3. Commit to Git: git add ../data/ticket_data.csv")
        print("   4. Push: git commit -m 'Add ticket data'; git push")

if __name__ == "__main__":
    main()