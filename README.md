# Data Retrieval Project

This project is designed to retrieve product information, specifically products and prices, from the [PuraVida](https://www.puravidabracelets.com/collections/earrings) website. It provides a simple interface for retrieving, displaying, and saving the data in various formats.

## Table of Contents

- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Usage](#usage)
  
## Introduction

This project utilizes Python and various libraries to interact with the PuraVida website, retrieve product information, and perform basic data operations such as displaying the data, generating graphs, and saving the data to an Excel file.


![image](https://github.com/user-attachments/assets/050e91c2-e70d-46f5-87ac-7e566f65a5ea)







## Dependencies

The following libraries are required to run the project:

- `tkinter`: For creating the graphical user interface (GUI).
- `selenium`: For web scraping and interacting with web elements.
- `webdriver_manager`: For managing web drivers required by Selenium.
- `matplotlib`: For generating graphs.
- `pandas`: For data manipulation and saving data to Excel files.

These dependencies can be installed via `pip`, for example:

```bash
pip install tkinter selenium webdriver_manager matplotlib pandas
```

## Usage

To use the project:

1. **Run the Python script `main.py`.**
   
   This will start the application and open the graphical user interface (GUI).

2. **Click the "Retrieve Data" button to fetch product information from the HumbleBundle website.**

   This will initiate the data retrieval process. Once completed, a message will indicate whether the data was successfully retrieved.

3. **Optional: Click the "Display Graph" button to visualize the product prices in a bar graph.**

   This will generate and display a bar graph showing the prices of the retrieved products.


   ![image](https://github.com/user-attachments/assets/5ccf1c54-87a1-4a0b-9f89-229c872e754f)


5. **Optional: Click the "Products Display" button to view the product information in a separate window.**

   This will open a new window displaying the retrieved products' information.

   
   ![image](https://github.com/user-attachments/assets/4283af13-7726-4458-ae28-24f372d870df)


6. **Enter a name for the Excel file in the provided text box.**

   Provide a desired name for the Excel file where you want to save the retrieved data.

7. **Click the "Save File Name" button to save the entered file name.**

   This will save the entered file name for later use when saving the data.

8. **Click the "Save Excel File" button to save the retrieved product information to an Excel file.**

   This will prompt you to select a directory where you want to save the Excel file. Once the file is saved, a message will indicate whether the operation was successful.


   ![image](https://github.com/user-attachments/assets/0f879ee1-1df2-440d-a50e-6c5b2b4eaed7)


