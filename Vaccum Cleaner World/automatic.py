import time

def vacuum_agent(dirt, vacuum):
    while (dirt[0] == True) or (dirt[1] == True):
        if vacuum[0] == True:
            print("\nVacuum Cleaner is in Room A\n")
            time.sleep(1)

            if dirt[0] == True:
                print("Dirt found in Room A\n")
                time.sleep(1)

                print("Cleaning Dirt in Room A.......\n")
                time.sleep(1)

                dirt[0] = False
            else:
                print("No Dirt found in Room A\n")
                time.sleep(1)

            print("Moving to Room B.....\n")
            time.sleep(1)

            vacuum[0] = False
            vacuum[1] = True

        else:
            print("\nVacuum Cleaner is in Room B\n")
            time.sleep(1)

            if dirt[1] == True:
                print("Dirt found in Room B\n")
                time.sleep(1)

                print("Cleaning Dirt in Room B.......\n")
                time.sleep(1)

                dirt[1] = False
            else:
                print("No Dirt found in Room B.....\n")
                time.sleep(1)

            print("Moving to Room A.....\n")
            time.sleep(1)

            vacuum[1] = False
            vacuum[0] = True

    print("No dirt found!! Cleaning completed.\n")

def main():
    # Room A: True means dirty
    # Room B: True means dirty
    dirt = [True, True]            # [Room A, Room B]
    vacuum = [False, True]         # Vacuum starts in Room B
    vacuum_agent(dirt, vacuum)

main()
