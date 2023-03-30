import sys

# Leave these lines untouched
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Your code here
def main():
    char = str(sys.argv[1])
    counter = 0

    records = sys.stdin.readlines()
    records_new = []
    for record in records:
        record_new = record.replace(char, "")
        records_new.append(record_new)
        counter += record.count(char)
    
    sys.stdout.writelines(records_new)
    sys.stderr.write(str(counter))
    

    # while (True):
    #     record = str(sys.stdin.readline().rstrip("\n")) 
    #     if record == "": 
    #         break
    #     record_new = record.replace(char, "")
    #     counter += record.count(char)
    #     sys.stdout.write(record_new)
    #     sys.stdout.write("\n")

    # sys.stderr.write(str(counter))

if __name__ == "__main__":
    main()
