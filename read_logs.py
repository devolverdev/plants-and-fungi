def show_errors(filename="logs.txt"):
    print("📜 Error Log:")
    with open(filename) as f:
        for line in f:
            if "ERROR" in line or "❌" in line:
                print(line.strip())

if __name__ == "__main__":
    show_errors()

