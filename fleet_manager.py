def main():

    names, ranks, divs, ids = init_database()
    
    
    def init_database():
        names =["Jonathan Archer", "Phillip Boyce", "Dolim", "Alonzo Freeman", "Hemmer"]
        ranks = ["Captain", "Lt. Commander", "Commander", "Admiral", "Lieutenant"]
        divs = ["command", "medicine", "council", "flaag", "engineering"]
        ids = [41092, 53906, 80941, 28569, 79136]
        

        return names, ranks, divs, ids
    
    def display_menu():
        full_name = input("Enter full name: ")
        print("\n--- MENU ---")
        print(f"User logged in as: {full_name}")
        print("1. Display Roster")
        print("2. Add Member")
        print("3. Remove Member")
        print("4. Update Rank")
        print("5. Search Crew")
        print("6. Filter by Division")
        print("7. Calculate Payroll")
        print("8. Count Officers")
        print("9. Exit")

        return input("Select option: ")
    
    def add_member():
        name = input("Name: ")
        rank = input("Rank: ")
        div = input("Division: ")
        id_num = int(input("ID: "))

        valid_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Admiral"]

        if id_num in ids: 
            print("ID already exists. Member not added.")
            return
        
        names.append(name)
        ranks.append(rank)
        divs.append(div)
        ids.append(id_num)
        
        
        print("member added.")


    def remove_member():
        remove_id = int(input("ID to remove: "))

        if remove_id not in ids:
            print("ID not found. No member removed.")
            return
        
        index = ids.index(remove_id)

        names.pop(index)
        ranks.pop(index)
        divs.pop(index)
        ids.pop(index)

        print("Member removed.")

        





main()


         




main()