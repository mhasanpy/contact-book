# contact-book
Concepts: Dictionaries, JSON, search algorithms
# 📇 Contact Book Application

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![JSON](https://img.shields.io/badge/Data-JSON-purple.svg)](https://www.json.org/)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A robust **command-line Contact Book** application built with Python, featuring data persistence, input validation, and full CRUD operations. This project demonstrates **object-oriented programming** and **real-world data management**.

## 🎯 Purpose

Manage personal and professional contacts efficiently with a clean CLI interface. The application validates phone numbers and emails, stores data persistently using JSON, and provides intuitive search and update functionality.

## ✨ Features

- ➕ **Add Contacts** – Store name, phone, email, and address
- 📋 **View All Contacts** – Display sorted list with quick reference
- 🔍 **Search Contacts** – Find contacts by name (partial matches supported)
- ✏️ **Update Contacts** – Modify any field while preserving existing data
- 🗑️ **Delete Contacts** – Remove contacts with confirmation prompt
- ✅ **Input Validation** – Phone number and email format checking
- 💾 **JSON Storage** – Persistent data保存在 `contacts.json`
- 🔒 **Duplicate Prevention** – No duplicate contact names allowed

## 🧠 Concepts Covered

This exercise demonstrates the following Python concepts:

| Concept | Implementation |
|---------|----------------|
| **OOP (Classes)** | `ContactBook` class encapsulates all functionality |
| **Dictionaries** | Store contacts with name as key, details as nested dict |
| **JSON Module** | Serialize/deserialize contacts to `contacts.json` |
| **Regular Expressions** | Validate phone numbers and email formats with `re` module |
| **File Handling** | `load_contacts()` and `save_contacts()` methods |
| **List Comprehensions** | Efficient contact searching with partial name matching |
| **Error Handling** | `try/except` for missing JSON file |
| **Input Validation** | Real-time format checking with user-friendly warnings |

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/mhasanpy/contact-book.git
   cd contact-book
