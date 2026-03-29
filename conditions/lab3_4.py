def process_data_guarded(data):
    if not data:
        print("No data provided.")
        return # stops the function here.
    
    if not isinstance(data, list):
        print(f"Invalid value type for data provided {type(data)} required list.")
        return # stops the function here.
    
    count = len(data)
    print(f"Processing {count} items...")
    print("Processed")      
    print(data)

process_data_guarded("ABC")
process_data_guarded(10)
process_data_guarded([10, 20, 30])