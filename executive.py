'''
Name: Sophia Medallada
Project: Personal Information Records
'''
def menu():
    print('Main Menu')
    print('1. Add')
    print('2. Update')
    print('3. Delete')
    print('4. Exit')

def add():
    ssd = input('Social Security Number: ')
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    address = input('Address: ')
    city = input('City: ')
    state = input('State: ')
    zip_code = input('Zip code: ')
    personal_rec = f"{ssd}, {first_name}, {last_name}, {address}, {city}, {state}, {zip_code}\n"
    add_file = open('records.txt', 'a')
    add_file.write(personal_rec)
    print('Information added in successfully!')

def update():
    found = False
    ss_num = input('Enter your social security number: ')
    file_read = open('records.txt', 'r')
    info = file_read.readlines()
    for line in info:
        record = line.split(',')
        if record[0] == ss_num:
            found = True
            print('Current Information:')
            print(f'Social Security Number: {record[0]} ')
            print(f"First Name: {record[1]}")
            print(f"Last Name: {record[2]}")
            print(f"Address: {record[3]}")
            print(f"City: {record[4]}")
            print(f"State: {record[5]}")
            print(f"Zip Code: {record[6]}")
            option = input("Do you want to update? (yes/no): ")
            if option.lower() == 'yes':
                update = input("Enter your new information by commas: ")
                info.remove(line)
                new_update = update + '\n'
                info.append(f"{new_update}\n")
                write_file = open('records.txt', 'w')
                write_file.writelines(info)
                print('Information updated')
        if not found:
            print('No records found from the social security number')

def delete():
    found = False
    ss_num_delete = input('Enter your social security number: ')
    file = open('records.txt', 'r')
    info = file.readlines()
    for line in info:
        record = line.split(',')
        if record[0] == ss_num_delete:
            found = True
            print('Current Information:')
            print(f'Social Security Number:{record[0]} ')
            print(f"First Name:{record[1]}")
            print(f"Last Name:{record[2]}")
            print(f"Address:{record[3]}")
            print(f"City:{record[4]}")
            print(f"State:{record[5]}")
            print(f"Zip Code:{record[6]}")
            option_delete = input("Do you want to delete? (yes/no): ")
            if option_delete.lower() == 'yes':
                info.remove(line)
                write_file = open('records.txt', 'w')
                write_file.writelines(info)
                print('Information deleted')
        if not found:
            print('No records found from the social security number')

while True:
    menu()
    choice = int(input('Enter a number: '))
    if choice == 1:
        add()
    elif choice == 2:
        update()
    elif choice == 3:
        delete()
    elif choice == 4:
        print('Exiting the program')
        break
    else:
        print('Invalid choice. Please enter a number from 1-4')
