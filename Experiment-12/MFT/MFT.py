def main():
    # Input the total memory available and block size
    ms = int(input("Enter the total memory available (in Bytes) -- "))
    bs = int(input("Enter the block size (in Bytes) -- "))

    # Calculate the number of blocks and external fragmentation
    nob = ms // bs
    ef = ms - nob * bs

    # Input the number of processes
    n = int(input("\nEnter the number of processes -- "))

    mp = []

    # Input the memory required for each process
    for i in range(n):
        mem_req = int(input(f"Enter memory required for process {i+1} (in Bytes)-- "))
        mp.append(mem_req)

    print(f"\nNo. of Blocks available in memory--{nob}")
    print("\nPROCESS\tMEMORY REQUIRED\tALLOCATED\tINTERNAL FRAGMENTATION")

    tif = 0  # Total internal fragmentation
    p = 0    # Number of allocated processes

    # Allocation process
    for i in range(n):
        print(f"\n{i+1}\t\t{mp[i]}", end="")
        if mp[i] > bs:
            print("\t\tNO\t\t---")
        else:
            print(f"\t\tYES\t{bs - mp[i]}")
            tif += bs - mp[i]
            p += 1

        # If all blocks are used, stop allocation
        if p >= nob:
            break

    if p < n:
        print("\nMemory is Full, Remaining Processes cannot be accommodated")

    print(f"\n\nTotal Internal Fragmentation is {tif}")
    print(f"Total External Fragmentation is {ef}")

if __name__ == "__main__":
    main()
