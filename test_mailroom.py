



'''
I need to add global variables

 '''




from mailroom import new_donor
from mailroom import current_donor


# Global variables to be used to run assert tests
donor_list = ['Donor1','DonorA']
donation_history = [[10000], [200, 300]]


def test_new_donor():
    '''Test to verify we are adding a new donor to donor list '''
    assert new_donor('New Donor', 1200)
    donor_list == ['Donor1','DonorA','New Donor']
    donation_history ==  [[10000], [200, 300], [1200]]

def test_current_donor():
    assert current_donor('Donor1', 20)
    donation_history == [[10000, 20], [200, 300]]
    
