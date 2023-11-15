# Sasquatch Sightings Web App

Welcome to the Sasquatch Sightings Web App! This web application allows users to log and view sightings of Sasquatches.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [What I Learned](#whatilearned)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

The Sasquatch Sightings Web App is a Flask-based web application that enables users to document and share their encounters with Sasquatches. Users can create accounts, log sightings, view details of each sighting, edit their own sightings, and delete sightings they have reported.

## Features

- **User Authentication:** Users can create accounts and log in securely.
- **Sighting Management:** Users can create, edit, and delete their own Sasquatch sightings.
- **Viewing Sightings:** Users can view a list of all Sasquatch sightings reported by the community.
- **Detailed Information:** Each sighting includes information such as location, number of Sasquatches, and a description of the event.

## Installation

To run the Sasquatch Sightings Web App locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/GavinEwart/sasquatch-websightings.git
   cd sasquatch-sightings-web-app
   
2. Add clone into your VScode and open in an integrated terminal

3. Install the required dependencies by running the following command in your project directory:
   ```sh
   pipenv install

4. Start your shell
   ```sh
   pipenv shell

5. Start the Flask application:
   ```sh
   python server.py
  
6. Open your web browser and navigate to http://localhost:5000.

## What I Learned <a name="whatilearned"></a>

In the process of developing this Sasquatch Sighting Tracker web application, I gained valuable insights and skills:

- **Code Reusability:** Explored techniques for code reuse, leveraging functionalities from previous projects to streamline development while maintaining the ability to create new and innovative features.

- **Web Application Development:** Deepened my understanding of web application development using Flask, a web framework for Python, to create dynamic and interactive features.

- **Database Integration:** Implemented MySQL database integration to store and manage Sasquatch sightings, enhancing data persistence and retrieval capabilities.

- **User Authentication:** Incorporated user authentication features, allowing users to securely log in, register accounts, and ensure secure access to personalized data.

- **Dynamic HTML Rendering:** Utilized Jinja templating in Flask to dynamically render HTML pages based on user input and data retrieved from the database.

- **Form Handling:** Managed form submissions effectively, validating and processing user input to ensure data integrity and user-friendly interactions.

## Usage

1. **Create an Account:**
   - Navigate to the web app and sign up for a new account.

2. **Log In:**
   - Log in using your credentials.

3. **Report a Sighting:**
   - Once logged in, you can report a new Sasquatch sighting, providing details about the location, number of Sasquatches, and the event itself.

4. **View and Manage Sightings:**
   - You can view all sightings on the homepage, edit your own sightings, and delete sightings you've reported.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.
