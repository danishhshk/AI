# Function to gather partner information
def get_partner_info(partner_number):
    print(f"Partner {partner_number} Details:")
    partner_info = {}
    partner_info["Name"] = input("Full Name: ")
    partner_info["Gender"] = input("Gender (Son/Daughter) of Father's Name: ")
    partner_info["Address Line 1"] = input("Address Line 1: ")
    partner_info["Address Line 2"] = input("Address Line 2: ")
    partner_info["City"] = input("City: ")
    partner_info["State"] = input("State: ")
    partner_info["Pin Code"] = input("Pin Code: ")
    return partner_info

# Function to gather partnership details
def get_partnership_details():
    partnership_details = {}
    partnership_details["Date"] = input("Date of Partnership (Date, Month, Year): ")
    partnership_details["Business Activity"] = input("Description of Business Activity Proposed: ")
    partnership_details["Principal Place"] = input("Principal Place of Business: ")
    partnership_details["Duration"] = input("Duration of Partnership: ")
    partnership_details["Capital"] = input("Initial Capital of the Firm (Total Partners Contribution): ")
    return partnership_details

# Function to gather witness information
def get_witness_info(witness_number):
    print(f"Witness {witness_number} Details:")
    witness_info = {}
    witness_info["Name"] = input("Full Name: ")
    witness_info["Address Line 1"] = input("Address Line 1: ")
    witness_info["Address Line 2"] = input("Address Line 2: ")
    witness_info["City"] = input("City: ")
    witness_info["State"] = input("State: ")
    witness_info["Pin Code"] = input("Pin Code: ")
    return witness_info

# Main function to generate the deed of partnership
def generate_deed_of_partnership():
    # Gather partner information for all four partners
    partners = []
    for i in range(1, 5):
        partner_info = get_partner_info(i)
        partners.append(partner_info)

    # Gather partnership details
    partnership_details = get_partnership_details()

    # Gather witness information for both witnesses
    witnesses = []
    for i in range(1, 3):
        witness_info = get_witness_info(i)
        witnesses.append(witness_info)

    # Generate the deed of partnership document
    deed_of_partnership = f""" \n \n \n \n \n \n \n \n \n \n \n \n 
Deed of Partnership

This deed of partnership is made on {partnership_details['Date']} between:
1. {partners[0]['Name']}, {partners[0]['Gender']} of {partners[0]['Address Line 1']}, residing at {partners[0]['Address Line 2']}, {partners[0]['City']}, {partners[0]['State']}, {partners[0]['Pin Code']} hereinafter referred to as FIRST PARTNER. \n
2. {partners[1]['Name']}, {partners[1]['Gender']} of {partners[1]['Address Line 1']}, residing at {partners[1]['Address Line 2']}, {partners[1]['City']}, {partners[1]['State']}, {partners[1]['Pin Code']} hereinafter referred to as SECOND PARTNER. \n
3. {partners[2]['Name']}, {partners[2]['Gender']} of {partners[2]['Address Line 1']}, residing at {partners[2]['Address Line 2']}, {partners[2]['City']}, {partners[2]['State']}, {partners[2]['Pin Code']} hereinafter referred to as THIRD PARTNER. \n
4. {partners[3]['Name']}, {partners[3]['Gender']} of {partners[3]['Address Line 1']}, residing at {partners[3]['Address Line 2']}, {partners[3]['City']}, {partners[3]['State']}, {partners[3]['Pin Code']} hereinafter referred to as FOURTH PARTNER. \n

Whereas, the parties hereto have agreed to commence business in partnership and it is expedient to have a written instrument of partnership. Now, this partnership deed witnesses as follows:

1. BUSINESS ACTIVITY
 The parties hereto have mutually agreed to carry on the business of {partnership_details['Business Activity']}.

2. PLACE OF BUSINESS
The principal place of the partnership business will be situated at {partnership_details['Principal Place']}

3. DURATION OF PARTNERSHIP
The duration of the partnership will be {partnership_details['Duration']}.

4. CAPITAL OF THE FIRM
Initially, the capital of the firm shall be Rs. {partnership_details['Capital']}.

5. PROFIT SHARING RATIO
The profit or loss of the firm shall be shared equally among all the partners and transferred to the partners' current accounts.

6. MANAGEMENT
The {partners[0]['Name']} of the firm shall be the Managing Partner, and he will look after all the day-to-day transactions of the firm and any legal activities in the name of the firm, and the remaining partners shall cooperate to do so.

7. OPERATION OF BANK ACCOUNTS
The firm shall open a current account in the name of [Partnership Firm Name] at any bank, and such an account shall be operated by {partners[0]['Name']} and {partners[1]['Name']} jointly as declared from time to time to the Banks.

8. BORROWING
The written consent of all Partners will be required for the partnership to avail credit facilities from any financial institution.

9. ACCOUNTS
The firms shall regularly maintain, in the ordinary course of business, true and correct accounts of all its transactions and also of all its assets and liabilities, the property books of accounts, which shall ordinarily be kept at the firm’s place of business. The accounting year shall be the financial year from 1st April onwards, and the balance sheet shall be properly audited, and the same shall be signed by all the Partners. Every Partner shall have access to the books and the right to verify their correctness.

10. RETIREMENT
If any partner shall at any time during the subsistence of the partnership, be desirous of retiring from the firm, it shall be competent for him to do so, provided he shall give at least one calendar month notice of his intention of doing so. The remaining partners shall pay to the retiring partner or his legal representatives of the deceased partner, the purchase money of his share in the assets of the firm.

11. DEATH OF PARTNER
In the event of the death of any partners, one of the legal representatives of the deceased partner shall become the partner of the firm, and in the event the legal representatives show their denial to join the firm, they shall be paid the part of the purchase amount calculated as on the date of the death of the partner.

12. ARBITRATION
Whenever there be any difference of opinion or any dispute between the partners, the partners shall refer the same to an arbitration of one person. The decision of the arbitration so nominated shall be final and binding on all partners, such arbitration proceedings shall be governed by the Indian Arbitration Act, which is in force.

In witness whereof, this deed of partnership is signed, sealed, and delivered this {partnership_details['Date']} at {witnesses[0]['City']}, {witnesses[0]['State']}:

FIRST PARTNER

{partners[0]['Address Line 1']}\t 
{partners[0]['Address Line 2']}\t 
{partners[0]['City']}, {partners[0]['State']}, {partners[0]['Pin Code']}\t

SECOND PARTNER
{partners[1]['Address Line 1']}
{partners[1]['Address Line 2']}
{partners[1]['City']}, {partners[1]['State']}, {partners[1]['Pin Code']}

THIRD PARTNER

{partners[2]['Address Line 1']}\t
{partners[2]['Address Line 2']}\t
{partners[2]['City']}, {partners[2]['State']}, {partners[2]['Pin Code']}\t

FOURTH PARTNER
{partners[3]['Address Line 1']}
{partners[3]['Address Line 2']}
{partners[3]['City']}, {partners[3]['State']}, {partners[3]['Pin Code']}

WITNESS ONE

{witnesses[0]['Address Line 1']}\t
{witnesses[0]['Address Line 2']}\t
{witnesses[0]['City']}, {witnesses[0]['State']}, {witnesses[0]['Pin Code']}\t

WITNESS TWO 
{witnesses[1]['Address Line 1']}
{witnesses[1]['Address Line 2']}
{witnesses[1]['City']}, {witnesses[1]['State']}, {witnesses[1]['Pin Code']}
"""

    return deed_of_partnership

# Generate and print the deed of partnership
deed = generate_deed_of_partnership()
print(deed)

from fpdf import FPDF

# Create a class that inherits from FPDF
class PDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.background_added = False  # Initialize the background_added flag to False

    def header(self):
        if not self.background_added:
            # Add the background image on the first page only
            self.image('background.jpg', x=0, y=0, w=210, h=297)  # Adjust x, y, w, and h as needed
            self.background_added = True  # Set the flag to True

        # Header
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, " ", align="C", ln=True)

    def footer(self):
        # Footer
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    def chapter_title(self, title):
        # Chapter title
        self.add_page()  # Add a new page for each chapter (without background)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, 0, 1)

    def chapter_body(self, body):
        # Chapter body
        self.set_font("Arial", "", 12)
        # Output the modified body text with non-Latin-1 characters replaced
        self.multi_cell(0, 10, body.encode('latin-1', 'replace').decode('latin-1'))
        self.ln()

# Create a PDF object
pdf = PDF()

# Add the content to the PDF
pdf.chapter_title(" ")

# Replace non-Latin-1 characters
body_text = deed.replace('\u2019', "'")

# Add the modified text to the PDF
pdf.chapter_body(deed)

# Output the PDF to a file
pdf.output("partnership_deed.pdf")


