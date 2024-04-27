# Data Retrieval Project

This project is designed to retrieve product information, specifically products and prices, from the [HumbleBundle](https://www.humblebundle.com/store/search?sort=bestselling&genre=vr&hmb_source=navbar) website. It provides a simple interface for retrieving, displaying, and saving the data in various formats.

## Table of Contents

- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Usage](#usage)
  
## Introduction

This project utilizes Python and various libraries to interact with the HumbleBundle website, retrieve product information, and perform basic data operations such as displaying the data, generating graphs, and saving the data to an Excel file.
![image](https://github.com/cezaramariazamfir/DataRetrivalProject/assets/102034759/cafecd86-5dbf-4f73-97cd-1f4d3076925c)


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

4. **Optional: Click the "Display Matrix" button to view the product information in a separate window.**

   This will open a new window displaying the retrieved product information in a matrix format.

5. **Enter a name for the Excel file in the provided text box.**

   Provide a desired name for the Excel file where you want to save the retrieved data.

6. **Click the "Save File Name" button to save the entered file name.**

   This will save the entered file name for later use when saving the data.

7. **Click the "Save Excel File" button to save the retrieved product information to an Excel file.**

   This will prompt you to select a directory where you want to save the Excel file. Once the file is saved, a message will indicate whether the operation was successful.

