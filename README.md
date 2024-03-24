# Inventory Management System
This project is a comprehensive inventory management system implemented in Python, designed to facilitate efficient management of products, user authentication, and essential CRUD (Create, Read, Update, Delete) operations.

#### Video Demo
URL: https://www.youtube.com/watch?v=8n2_2vdgfD0

## Features
### User Authentication
Secure Login: Users can authenticate themselves through a username and password.

Role-based Access: Differentiates between administrator and cashier roles to provide appropriate access levels.
### Product Management
Product Listing: Allows users to view a comprehensive list of products, including details such as name, price, tax, stock level, and alert threshold.

Alert System: Monitors product stock levels and alerts users when stock falls below a predefined threshold.

Update Operations: Provides functionalities for adding new products, updating existing product information, and adjusting stock levels.
### Checkout Process
Sales Operations: Facilitates the sale of products, allowing users to add items to a virtual cart, calculate the total price including tax, and generate receipts.

Payment Options: Supports both cash and card payments, with automatic change calculation for cash transactions.

Return Handling: Enables users to process returns, updating stock levels accordingly.
### Settings Management
Currency Configuration: Allows administrators to set the currency type used for transactions.

Company Name Customization: Provides the flexibility to customize the company name displayed on receipts.
### User Management
User Monitoring: Enables administrators to monitor registered users and their respective roles.

User Registration: Allows administrators to register new users, assigning them appropriate roles and login credentials.

User Deletion: Provides functionality to delete user accounts when necessary, with appropriate permissions.
## How to Use
Login: Users need to authenticate themselves using their username and password.

Navigation: Upon successful login, users can navigate through various functionalities such as product management, checkout process, settings configuration, and user management.

Perform Operations: Users can perform operations such as adding/updating products, processing sales/returns, configuring settings, and managing user accounts.

Logout: After completing tasks, users can securely logout from the system to ensure data privacy and security.
## Requirements
Python 3.x

JSON module (included in Python standard library)
