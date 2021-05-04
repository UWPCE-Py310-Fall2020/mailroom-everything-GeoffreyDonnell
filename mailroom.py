"""
Write a small command-line script called mailroom.py. This script should be executable.
The script should accomplish the following goals:

It should have a data structure that holds a list of your donors and a history of the amounts they have donated.
This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
You can store that data structure in the global namespace.

The script should prompt the user (you) to choose from a menu of 3 actions:
“Send a Thank You”, “Create a Report” or “quit”.
"""

donor_data = [('Tony Stark', [10]),
              ('Steven Rogers', [10, 20]),
              ('Bruce Wayne', [20, 30, 40]),
              ('Clark Kent', [50]),
              ('Geoffrey Donnell', [60, 70])]


def check_donation():
    # Function created to check and ensure valid inputs are given for donations
    invalid = True
    while invalid == True:
        new_donation = input('How much is this donation: ')
        try:
            new_donation = float(new_donation)
        except ValueError:
            print('You need to enter a valid numerical value.')
        else:
            new_donation = float(new_donation)
            round_donation = round(new_donation, 2)
            difference = round_donation - new_donation
            if new_donation <=0:
              print('You need to enter a value greater than zero.')
              new_donation = check_donation() # Start this script over
            if difference != 0:
              print('You need to enter valid monetary value in the form of 0.00')
              new_donation = check_donation()
            invalid = False

    return new_donation


def display_donors():
    """
    Function that will print the list of donors
    """

    print('\n')
    for step in range(0, len(donor_data)):
        print(donor_data[step][0])
    print('\n')


def generate_donor_list():
    """
    Function that will generate a donor_list to check against
    to see if the input from user entering an existing donor
    """
    donor_list = [''] * len(donor_data)
    for step in range(0, len(donor_data)):
        donor_list[step] = donor_data[step][0]
    return donor_list


def current_donor(donor_name, new_donation):
    """" For donors that are already on file the function adds the new donation to their history"""
    # Loops to determine where in the list the donor is and their corresponding donations
    for step in range(0, len(donor_data)):
        if donor_data[step][0] == donor_name:  # if statement to find where to add the new donation
            donor_data[step][1].append(new_donation)
    return donor_data


def add_new_donor_to_database(donor_name, new_donation):
    """For donors not on the list adds them to the list"""
    new_donor = (donor_name, [new_donation])
    donor_data.append(new_donor)
    return donor_data


def draft_email(donor_name, donor_amount):
    donor_amount = '{:.2f}'.format(donor_amount)
    print(f'\nEmail to: {donor_name.replace(" ", "")}@gmail.com')
    print('Subject: Donation Received')
    print(f'\nThank you {donor_name} for your generous donation of ${donor_amount}! \n'
          f'We greatly appreciate your support to our cause. \n'
          f'Best regards,\n'
          f'Staff Member\n')
    return f'Thank you {donor_name} for your generous donation of ${donor_amount}.'


def generate_report_data():
    # Need to declare empty lists to store values that will be calculated
    print(f'This is from the generate report data function \n {donor_data}')
    no_donors = int(len(donor_data))
    print(f'This is the number of donors {no_donors}')
    donation_freq = [0] * no_donors
    donation_total = [0] * no_donors
    donation_average = [0] * no_donors
    # Finds the average and number of donations
    for index in range(0, no_donors):
        donation_total[index] = sum(donor_data[index][1])
        donation_freq[index] = len(donor_data[index][1])
        donation_average[index] = float(donation_total[index] / donation_freq[index])
    return no_donors, donation_total, donation_freq, donation_average


def print_report():
    no_donors, donation_total, donation_freq, donation_average = generate_report_data()
    # Formatting and Printing for Header
    header = ['Donor Name', 'Total Given', 'Number Gifts', 'Average Gifts']
    header_format = '{:18}|{:16}|{:16}|{:20}|'
    print('\n')
    print(header_format.format(*header))
    print('-' * int(len(header_format.format(*header))))  # dividing line for the report

    # Formatting and Printing for Donor List
    donor_format = '{:18}|${:15.2f}|{:16}|${:19.2f}|'

    for step in range(0, no_donors):
        print(donor_format.format(donor_data[step][0],
                                  float(donation_total[step]),
                                  int(donation_freq[step]),
                                  float(donation_average[step])))
    menu()  # after report is generated we will go back to the menu
    pass


def letter_options():
    donor_name = input("Please enter the full name of the donor (case sensitive) or type L for a list of donors: ")
    if donor_name == 'L':
        display_donors()
        letter_options()
    donor_list = generate_donor_list()
    if donor_name in donor_list:
        print('Yay this donor has given us more money!')
        new_donation = check_donation()
        current_donor(donor_name, new_donation)
        draft_email(donor_name, new_donation)
        menu()
    else:
        print('Yay we have a new donor!')
        new_donation = check_donation()
        add_new_donor_to_database(donor_name, new_donation)
        draft_email(donor_name, new_donation)
        menu()
    pass


def menu():
    # This function will be the one that runs everytime and will point to other functions to complete
    # the three tasks. (1) Generate a report (2) generate a report (3) or quit.

    print('\nWelcome to the Automated Mail Room System (AMRS).\n'
          'Please select from the three options below \n'
          'by entering the value contained in the ()\n'
          '(1) Generate a Report\n'
          '(2) Send a Thank You\n'
          '(3) Quit the program')
    choice = (input('What would you like to do? Enter value: '))

    while choice not in ['1', '2', '3']:
        choice = (input('Invalid value. Please enter a valid choice: 1, 2, or 3: '))

    if choice == '1':
        print_report()
    if choice == '2':
        letter_options()
    if choice == '3':
        print("\n Thanks for using AMRS, Goodbye!")
        quit()
    return


if __name__ == '__main__':
    menu()
