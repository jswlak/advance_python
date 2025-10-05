# 🔄 Relational vs NoSQL Databases

Databases come in two main families — **Relational (SQL)** and **Non-Relational (NoSQL)**.  
Each has different structures, rules, and best-fit use cases.

---

## 🧩 1. Relational Databases (SQL)

### 🧠 Definition

A **Relational Database Management System (RDBMS)** stores data in **tables (rows and columns)**, and relationships between tables are defined using **keys**.

---

### 📘 Example

A simple “Shop” database may have two tables —

**Customers**

| id | name | city   |
|----|------|---------|
| 1  | Riya | Delhi   |
| 2  | Aarav| Mumbai  |

**Orders**

| id | customer_id | product | price |
|----|--------------|----------|--------|
| 1  | 1            | Shoes    | 1200   |
| 2  | 2            | Watch    | 2000   |

➡️ Here, `customer_id` in **Orders** refers to `id` in **Customers** — this is a **relationship**.

---

### ⚙️ Characteristics

| Feature        | Description |
|----------------|--------------|
| **Structure**  | Data stored in fixed schemas (tables, columns) |
| **Language**   | Uses SQL (Structured Query Language) |
| **Relationships** | Supports foreign keys and joins |
| **Transactions** | Follows ACID properties (Atomicity, Consistency, Isolation, Durability) |
| **Examples**   | MySQL, PostgreSQL, SQLite, Oracle, SQL Server |

---

### ✅ Pros
- Strong data consistency  
- Complex queries with joins  
- Easy to maintain data integrity  
- Ideal for structured data  

### ❌ Cons
- Less flexible for unstructured data  
- Harder to scale horizontally (across servers)  
- Requires predefined schema  

---

## 🌐 2. NoSQL Databases

### 🧠 Definition

**NoSQL** stands for “Not Only SQL”.  
These databases store data in **non-tabular formats** — document, key-value, wide-column, or graph — and are more flexible.

---

### 📘 Example: *MongoDB (Document-based)*

```json
{
  "id": 1,
  "name": "Riya",
  "city": "Delhi",
  "orders": [
    { "product": "Shoes", "price": 1200 },
    { "product": "Bag", "price": 800 }
  ]
}

---

➡️ All related data lives inside one document, instead of multiple tables.

---

## 🧩 Types of NoSQL Databases

| Type         | Example               | Description |
|---------------|-----------------------|--------------|
| **Document**  | MongoDB, CouchDB      | JSON-like documents |
| **Key-Value** | Redis, DynamoDB       | Simple key-value pairs |
| **Wide-Column** | Cassandra, HBase    | Data stored in columns instead of rows |
| **Graph**     | Neo4j                 | Nodes and relationships for network-like data |

---

## ⚙️ Characteristics

| Feature       | Description |
|----------------|-------------|
| **Structure**  | Dynamic, schema-less |
| **Scalability** | Horizontally scalable (easier to scale out) |
| **Consistency** | Often uses “eventual consistency” instead of strict ACID |
| **Speed**       | Very fast for large, distributed data |
| **Examples**    | MongoDB, Redis, Cassandra, Firebase |

---

## ✅ Pros

- Flexible schema (store any structure)  
- Easier to scale horizontally  
- Better performance for huge or distributed data  
- Great for unstructured or rapidly changing data  

---

## ❌ Cons

- Weaker consistency (in some systems)  
- Limited complex querying  
- No universal query language like SQL  

---

## ⚖️ Comparison Summary

| Feature          | Relational (SQL)                     | NoSQL                                |
|------------------|--------------------------------------|--------------------------------------|
| **Data Model**   | Tables with rows and columns         | Documents, key-value, graphs         |
| **Schema**       | Fixed, predefined                    | Dynamic, flexible                    |
| **Query Language** | SQL                                | Varies (MongoDB Query, APIs, etc.)   |
| **Transactions** | ACID compliant                       | Often BASE (Basically Available, Soft state, Eventually consistent) |
| **Scalability**  | Vertical (bigger server)              | Horizontal (more servers)            |
| **Best For**     | Structured data, complex relationships | Large, unstructured, or rapidly changing data |

---

## 🧠 When to Use Which

| Use Case | Recommended |
|-----------|--------------|
| **Banking, Accounting** | ✅ Relational (SQL) |
| **Social media, IoT, Real-time analytics** | ✅ NoSQL |
| **ERP, CRM, Inventory apps** | ✅ SQL |
| **Big Data, Flexible schema apps** | ✅ NoSQL |

---

## ✅ Summary

- **SQL →** Structured, consistent, relational data  
- **NoSQL →** Flexible, scalable, unstructured data  

Choose based on **data structure**, **scalability**, and **consistency** needs.
