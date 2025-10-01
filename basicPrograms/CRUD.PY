from tabulate import tabulate
import mysql.connector as mys
import pandas as pd
from datetime import datetime
# 🟢 Connect to MySQL
con = mys.connect(
    host="localhost",  # 🔁 Your MySQL host
    user="root",  # 👤 Your MySQL user
    password="115829955@Ak",  # 🔑 Your password
    database="sales_tools"  # 🗃️ Your database name
)
if con:
    print("✅ MySQL Connected Successfully!")
else:
    print("❌ Connection Error!")

# 🔼 Insert Function
def insert():
    MATERAL = input("Enter MATERIAL NAME: ")
    QTY = input("Enter QUANTITY: ")
    MATERIAL_TYPE = input("Enter MATERIAL TYPE: ")
    choice = input("Enter date manually? (y/n): ").lower()
    if choice == 'y':
        DATED = input("Enter DATE (YYYY-MM-DD): ")
    else:
        DATED = datetime.now().strftime("%Y-%m-%d")
    res = con.cursor()
    sql = "INSERT INTO sales_data (MATERAL, QTY, MATERIAL_TYPE, DATED) VALUES (%s, %s, %s, %s)"
    user = (MATERAL, QTY, MATERIAL_TYPE, DATED)
    res.execute(sql, user)
    con.commit()
    print("✅ Data Inserted Successfully.")

# 🛠️ Update Function
def update():
    ID = input("Enter ID to update: ")
    MATERAL = input("Enter New MATERIAL NAME: ")
    QTY = input("Enter New QUANTITY: ")
    MATERIAL_TYPE = input("Enter New MATERIAL TYPE: ")
    DATED = input("Enter New DATE (YYYY-MM-DD): ")
    res = con.cursor()
    sql = "UPDATE sales_data SET MATERAL=%s, QTY=%s, MATERIAL_TYPE=%s, DATED=%s WHERE id=%s"
    user = (MATERAL, QTY, MATERIAL_TYPE, DATED, ID)
    res.execute(sql, user)
    con.commit()
    print("✅ Data Updated Successfully.")

# 👁️ View All Data
def view():
    res = con.cursor()
    sql = "SELECT id, MATERAL, QTY, MATERIAL_TYPE, DATED FROM sales_data"
    res.execute(sql)
    result = res.fetchall()
    print("\n📋 All Records:")
    print(tabulate(result, headers=["ID", "MATERIAL", "QTY", "MATERIAL_TYPE", "DATED"], tablefmt="heavy_outline"))

# 🔍 View by ID (Optional)
def view_by_id():
    ID = input("Enter ID to search: ")
    res = con.cursor()
    sql = "SELECT id, MATERAL, QTY, MATERIAL_TYPE, DATED FROM sales_data WHERE id=%s"
    res.execute(sql, (ID,))
    result = res.fetchall()
    if result:
        print(tabulate(result, headers=["ID", "MATERIAL", "QTY", "MATERIAL_TYPE", "DATED"], tablefmt="fancy_outline"))
    else:
        print("⚠️ No record found with that ID.")

# ❌ Delete Record
def delete():
    ID = input("Enter ID to delete: ")
    res = con.cursor()
    sql = "DELETE FROM sales_data WHERE id=%s"
    res.execute(sql, (ID,))
    con.commit()
    print("🗑️ Record Deleted Successfully.")

# 📤 Export to Excel
def export_to_excel():
    res = con.cursor()
    sql = "SELECT id, MATERAL, QTY, MATERIAL_TYPE, DATED FROM sales_data"
    res.execute(sql)
    result = res.fetchall()
    # Column names
    columns = ["ID", "MATERIAL", "QTY", "MATERIAL_TYPE", "DATED"]
    df = pd.DataFrame(result, columns=columns)
    # Timestamp for file name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"sales_data_export_{timestamp}.xlsx"
    df.to_excel(filename, index=False)
    print(f"📁 Data Exported to '{filename}' Successfully.")
def export_to_html():
    res = con.cursor()
    sql = "SELECT id, MATERAL, QTY, MATERIAL_TYPE, DATED FROM sales_data"
    res.execute(sql)
    result = res.fetchall()
    # Column names
    columns = ["ID", "MATERIAL", "QTY", "MATERIAL_TYPE", "DATED"]
    df = pd.DataFrame(result, columns=columns)
# 🚪 Exit
def Exit():
    print("👋 Exiting program. Goodbye!")
    quit()

# 🔁 Menu Loop
while True:
    print("\n=== 🧾 SALES DATABASE MENU ===")
    print("1. INSERT DATA")
    print("2. UPDATE DATA")
    print("3. VIEW ALL DATA")
    print("4. VIEW BY ID")
    print("5. DELETE DATA")
    print("6. EXPORT TO EXCEL")
    print("7. EXPORT TO HTML")
    print("8. EXIT")
    try:
        action = int(input("👉 Enter your choice (1-7): "))
    except ValueError:
        print("⚠️ Please enter a valid number!")
        continue
    if action == 1:
        insert()
    elif action == 2:
        update()
    elif action == 3:
        view()
    elif action == 4:
        view_by_id()
    elif action == 5:
        delete()
    elif action == 6:
        export_to_excel()
    elif action == 7:
        export_to_html()
    elif action == 8:
        Exit()
    else:
        print("❌ Invalid option! Please select between 1 and 7.")
 
 