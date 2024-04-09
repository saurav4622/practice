import openpyxl
import pyautogui
import time

def read_excel_and_add_contacts(file_path):
    # Load the Excel workbook
    workbook = openpyxl.load_workbook(file_path)
    
    # Assuming data is in the first sheet (you can modify this if needed)
    sheet = workbook.active
    
    # Iterate through rows starting from the second row (assuming the first row contains headers)
    for row in sheet.iter_rows(min_row=2, values_only=True):
        name, phone_number = row

        # Open contacts app (modify this based on your operating system and application)
        # For example, on Windows, you can use the following:
        # pyautogui.hotkey('winleft', 's')
        # pyautogui.write('contacts')
        # pyautogui.press('enter')

        # Simulate typing the name
        pyautogui.write(name)
        time.sleep(1)  # Add a delay to allow the application to respond

        # Press Enter to create a new contact
        pyautogui.press('enter')
        time.sleep(1)

        # Simulate typing the phone number
        pyautogui.write(phone_number)
        time.sleep(1)

        # Press Enter to save the contact
        pyautogui.press('enter')
        time.sleep(1)

        # Go back to the contacts list (modify this based on your application)
        # For example, on Windows:
        # pyautogui.hotkey('ctrl', 'esc')
        # pyautogui.write('contacts')
        # pyautogui.press('enter')

    # Close the workbook
    workbook.close()

if __name__ == "__main__":
    # Replace 'your_excel_file.xlsx' with the path to your Excel file
    read_excel_and_add_contacts(C:\Users\SOURABH\OneDrive\Desktop\SPORTS 2K24 TEAMS.xlsx)
