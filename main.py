import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import matplotlib.pyplot as plt
import pandas as pd

products = []
prices = []
file_name = ''

# This function saves the file name enetered by the user 
def saveInput():
    global file_name_entry
    global file_name
    file_name = file_name_entry.get("1.0", "end-1c")  
    messagebox.showinfo("Message", f"File name saved: {file_name}.xlsx") 

# This function retrives the data from the humblebundle website using selenium and webdrivers
def retriveData():
    url = "https://www.humblebundle.com/store/search?sort=bestselling&genre=vr&hmb_source=navbar"
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    driver.get(url)
    driver.implicitly_wait(10)

    global products
    global prices

    elementHTML = driver.find_element("class name", "entities-list")
    children_element = elementHTML.find_elements("class name", "entity-block-container")

    for child in children_element:

        title = child.find_element("class name", "entity-title").get_attribute('innerText')
        products.append(title)

        price = child.find_element("class name", "price").get_attribute('innerText')
        prices.append(price)

    if products != [] and prices != []:
        messagebox.showinfo("Message", "Data was successfully retrived!")
    else:
        messagebox.showerror("Error", "There was an error in retriving the data!")

    return products, prices
    
# This function display into another windows the products and prices retrived from the website 
def displayMatrix():
    matrix = []
    for i in range(len(products)):
        matrix.append([products[i], prices[i][1:]])
    
    matrix_window = tk.Toplevel(root)
    matrix_window.title("Matrix Display")

    matrix_label = tk.Label(matrix_window, text="Matrix Display", font = ('Verdana', 18))
    matrix_label.pack()

    matrix_text = tk.Text(matrix_window, font = ('Verdana', 10))
    for i in range(len(products)):
        matrix_text.insert(tk.END, f"{products[i]} - {prices[i]}\n")
    matrix_text.pack()

#This function display a bar graph with the products and prices using matplotlib and pandas
def displayGraph():
    products_series = pd.Series(products)
    cleaned_prices = [float(price[1:]) for price in prices]
    prices_series = pd.Series(cleaned_prices)
    dict = {"Products" : products_series, "Prices" : prices_series}
    df = pd.DataFrame(dict)

    df.plot.bar(x='Products', y='Prices')
    plt.xlabel('Products')
    plt.ylabel('Prices')
    plt.title('Product Prices')
    plt.show()

#This function saves the excel file to a directory chosen by the user, using pandas and os
def saveExcelFile():
    products_series = pd.Series(products)
    cleaned_prices = [float(price[1:]) for price in prices]
    prices_series = pd.Series(cleaned_prices)
    dict = {"Products" : products_series, "Prices" : prices_series}
    df = pd.DataFrame(dict)

    directory_path = filedialog.askdirectory()
    full_file_path = os.path.join(directory_path, file_name + '.xlsx')
    df.to_excel(full_file_path, index = False)

    if os.path.exists(full_file_path):
        messagebox.showinfo("Message", f"File saved successfully: {full_file_path}")
    else:
        messagebox.showerror("Error", "Failed to save the file.")


#Tkinter Interface
root = tk.Tk()
root.geometry("800x500") 
root.title("Data Retrival Project")

label1 = tk.Label(root, text = "Data Retrival Project", font = ('Verdana', 20))
label1.pack()

label2 = tk.Label(root, text = "by Cezara Maria Zamfir", font = ('Verdana', 12))
label2.pack(pady= 10)

label3 = tk.Label(root, text = "This app retrives the products and prices from the HumbleBundle website.", font = ('Verdana', 10))
label3.pack(pady = (10, 10))

button1 = tk.Button(root, text = "Retrive Data", width = 20, font = ('Verdana', 13), background = 'white', command = retriveData)
button1.pack(pady = (20,5))

button2 = tk.Button(root, text = "Display Graph", width = 20, font = ('Verdana', 13), background = 'white', command = displayGraph)
button2.pack(pady = 5)

button3 = tk.Button(root, text = "Display Matrix", width = 20, font = ('Verdana', 13), background = 'white', command = displayMatrix)
button3.pack(pady = 5)

button4 = tk.Button(root, text = "Save Excel File", width = 20, font = ('Verdana', 13), background = 'white', command = saveExcelFile)
button4.pack(pady = 5)

label4 = tk.Label(root, text = "Please give the excel in which you want to save the data a name:", font = ('Verdana', 12))
label4.pack(padx = 0, pady = (50, 12))

file_name_entry = tk.Text(root, height = 1.3, width = 20 , font = ('Verdana', 15))
file_name_entry.pack(pady = (0, 20))

save_button = tk.Button(root, text="Save File Name", width = 20, font = ('Verdana', 10), background = 'orange', command=saveInput)
save_button.pack(pady = (2, 10))

root.mainloop()

