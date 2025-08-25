def analyze_csv():
    file_path = input("Enter the path to the CSV file: ").strip()
    total_rows = 0
    empty_rows = 0
    total_words = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                total_rows += 1
                stripped_line = line.strip()
                if not stripped_line:
                    empty_rows += 1
                    continue
                fields = [field.strip() for field in stripped_line.split(',')]
                for field in fields:
                    if field:
                        total_words += len(field.split())
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    print(f"Total Rows: {total_rows}")
    print(f"Empty Rows: {empty_rows}")
    print(f"Total Words: {total_words}")

analyze_csv()