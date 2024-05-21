# [GyA Form](https://recluta-form.onrender.com/)

The Movies APP is a platform designed to view information about the most popular, highest-rated, and upcoming movies. The information is obtained from TheMovieDB API.

## Table of Contents

- [GyA Form](#gya-form)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Postgresql Database](#postgresql-database)
  - [Features](#features)
  - [Deployment](#deployment)
  - [Copyright](#copyright)

## Introduction

Seguros Gutierrez y Arredondo was seeking an effective way to improve their prospect acquisition process. To achieve this goal, they hired me to develop a data capture form using Django and PostgreSQL. This form not only facilitates the collection of potential client information but also optimizes the distribution of this data to various recruitment teams, significantly enhancing team efficiency and lead management.

## Getting Started

To get started with "GyA Form", follow these simple steps:

> [!TIP]
> Ensure you have Python and pip installed on your machine.

### Prerequisites

> [!IMPORTANT]
Before you begin, make sure you have the following installed:

- Python (preferably the latest stable version)
- pip (Python package installer)
- PostgreSQL (for the database)

### Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/JorgeSarricolea/GyA-Form/
```

2. Navigate to the project directory:

```
cd GyA-Form
```

3. Create and activate a virtual environment:

```
# Create a virtual environment
python -m venv env

# Activate the virtual environment

# On Windows
env\Scripts\activate

# On macOS/Linux
source env/bin/activate
```

4. Install the required packages:

```
pip install -r requirements.txt
```

### PostgreSQL Database:

1. Make sure PostgreSQL is running on your machine.
2. Create a database for the project.
3. Update the DATABASES setting in settings.py with your database credentials.
  
4. Apply database migrations:

```
python manage.py makemigrations
python manage.py migrate
```

5. Run the development server:

```
python manage.py runserver
```

## Features

Some of the key features of this project include:

- **Prospect Models:** The application uses Django's powerful ORM to define models for capturing and managing prospect data. This ensures that all data is stored in a structured and easily accessible manner in a PostgreSQL database.

- **Bootstrap Integration:** The application is fully responsive, leveraging Bootstrap to ensure a seamless user experience across various devices and screen sizes. This makes it easy for prospects to fill out the form whether they are using a desktop, tablet, or mobile device.

- **Email Logic for Recruitment Teams:** The application includes a sophisticated email distribution logic. When a prospect submits their information, emails are automatically sent to different members of the recruitment team based on predefined criteria.


## Deployment

The application is deployed on [Render](https://render.com/), ensuring reliable performance and scalability. Both the Django server and the PostgreSQL database are hosted on Render, providing a robust environment for the application's day-to-day operations.

## Copyright

This project was created by [Jorge Sarricolea](https://jorgesarricolea.com). if you have any specific code questions or would like to chat about programming, feel free to contact me on [WhatsApp](https://wa.me/529381095593).
