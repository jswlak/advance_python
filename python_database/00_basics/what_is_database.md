# 🧠 What is a Database?

A **database** is an organized collection of data stored electronically, designed to make data easy to access, manage, and update.

---

## 📘 Example

| Data Type      | Example                     |
|----------------|-----------------------------|
| Customer Data  | Name, Email, Phone          |
| Inventory      | Product, Quantity, Price    |
| Transactions   | Date, Amount, Customer      |

Instead of storing data in random files like `customers.txt`, databases help manage **structured data efficiently**.

---

## 💡 Why Use a Database?

- 🔹 To store large amounts of data efficiently  
- 🔹 To prevent data duplication  
- 🔹 To enable quick search and retrieval  
- 🔹 To ensure data integrity and relationships  
- 🔹 To support multiple users simultaneously  

---

## 🏷️ Database Terminology

| Term           | Meaning |
|----------------|----------|
| **Table**          | A collection of related data (like an Excel sheet) |
| **Row (Record)**   | One entry in a table |
| **Column (Field)** | A property of data (e.g., Name, Email) |
| **Primary Key**    | Unique identifier for each row |
| **Query**          | Command to interact with the database |

---

## 🧩 Types of Databases

### 1. Relational Database (RDBMS)
- Stores data in **tables with relationships**.  
- Example: **MySQL, PostgreSQL, SQLite**  
- Uses **SQL (Structured Query Language)**.

### 2. NoSQL Database
- Stores data in **documents, key-value pairs, or graphs**.  
- Example: **MongoDB, Firebase, Cassandra**  
- Designed for **unstructured or semi-structured data**.

---

## 🌍 Popular Database Systems

| Type        | Examples                   | Description                |
|--------------|----------------------------|-----------------------------|
| **Relational** | MySQL, PostgreSQL, SQLite | Table-based, strict schema |
| **NoSQL**      | MongoDB, CouchDB          | JSON-like, flexible        |
| **In-Memory**  | Redis                    | Fast, temporary storage    |
| **Cloud**      | Firebase, AWS DynamoDB    | Managed services           |

---

## 🐍 Databases in Python

Python provides libraries to connect with databases easily:

- `sqlite3` — built-in for local relational DB  
- `mysql.connector`, `psycopg2` — for MySQL/PostgreSQL  
- `pymongo` — for MongoDB  

### Example:

```python
import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
conn.commit()
conn.close()

✅ Summary

Database = structured data storage system

Two main types: Relational (SQL) and Non-relational (NoSQL)

SQL helps manage data in relational databases

Python provides tools like sqlite3 for database programming