# JobFormMailer

FormMailer is a simple web application built with Flask that allows users to submit information through web forms. It stores the submitted data in a SQLite database and sends an email confirmation to the user upon successful form submission.

## Features

- User-friendly web form for data submission.
- Data storage in a SQLite database.
- Email confirmation sent to users after form submission.
- Easy-to-configure email settings for sending notifications.

## Getting Started

1. Clone this repository to your local machine.
2. Configure your email settings in the `app.py` file (update `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USE_SSL`, `MAIL_USERNAME`, and `MAIL_PASSWORD`).
3. Run the application with `python app.py`.
4. Access the application in your web browser at `http://localhost:5002`.

## Usage

1. Fill out the web form with your information.
2. Submit the form.
3. Check your email for a confirmation message.

## Technologies Used

- Flask
- SQLAlchemy
- Flask-Mail

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.
