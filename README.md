# Quiz App

A modern, feature-rich quiz application built with Django and Tailwind CSS. Create quizzes, take tests, track your progress, and manage events—all with a beautiful, responsive interface that supports dark mode.

## Features

### 🎯 Quiz Management

- **Create Your Own Quizzes**: Users can create custom quizzes with multiple choice questions via an intuitive interface
- **Take Quizzes**: Interactive quiz-taking experience with real-time scoring
- **View Results**: Detailed results showing correct/incorrect answers and scores
- **Quiz History**: Track all your quiz attempts with detailed statistics (attempts count, average score, percentage)
- **Personal Dashboard**: View and manage your own quizzes and events in one place
- **User Ownership**: All quizzes and events are linked to their creators

### 👤 User Authentication

- User registration and login system
- Secure authentication with Django's built-in auth
- Protected routes for authenticated users

### 📅 Events Management

- **Create Events**: Users can create and manage their own events with date, location, and description
- **View Event Details**: Browse event information with date, location, and full description
- **Event Listing**: View all available events in a organized list
- **User Ownership**: Track which user created each event

### 🎨 Modern UI/UX

- **Modern Design**: Clean, intuitive interface with a modern color palette
- **Dark Mode Support**: Explicit dark mode support for comfortable viewing
- **Responsive Design**: Mobile-friendly layout that adapts to all screen sizes
- **Interactive Effects**: Smooth hover transitions, button animations, and layout shifts
- **Consistent Components**: Unified styling for buttons, cards, headers, and more

## Screenshots

<!-- Add your screenshots here. You can use the following format:
![Screenshot Description](screenshots/screenshot-name.png)
-->

### Home Page

<img width="1757" height="932" alt="Screenshot 2025-11-30 215616" src="https://github.com/user-attachments/assets/c25277ac-0a6c-4f6d-a671-9eceb767b956" />

### Quiz List

<img width="1919" height="930" alt="Screenshot 2025-11-30 215734" src="https://github.com/user-attachments/assets/d27a7a0d-bd70-4a20-8a78-0bdd85282f23" />

### Quiz Taking Interface

<img width="1919" height="931" alt="Screenshot 2025-11-30 215851" src="https://github.com/user-attachments/assets/8e522135-b81b-4b98-a561-363f5002a1b2" />

### Quiz Results

<img width="1918" height="929" alt="image" src="https://github.com/user-attachments/assets/19997e8d-c2a6-4a81-a57c-012f2ee08935" />

### Dashboard

<img width="1919" height="896" alt="Screenshot 2025-11-30 215829" src="https://github.com/user-attachments/assets/67aa68db-cd04-452e-b191-fb0423c5b568" />

### Events Page

<img width="1918" height="931" alt="Screenshot 2025-11-30 220031" src="https://github.com/user-attachments/assets/c35a2409-4784-4e41-82a8-7719eca87f15" />

### Create Quiz Interface

<img width="1919" height="932" alt="Screenshot 2025-11-30 215943" src="https://github.com/user-attachments/assets/81d96fc0-e25b-4a21-99f3-4ed88adccd9f" />

### Create Event Interface

<img width="1919" height="927" alt="Screenshot 2025-11-30 220002" src="https://github.com/user-attachments/assets/efd4ab04-82a9-4883-86b2-ebb0a2eb5cc2" />

### Quiz History with Statistics

<img width="1919" height="931" alt="Screenshot 2025-11-30 221013" src="https://github.com/user-attachments/assets/472b743d-5ec4-42ed-9bbd-90f0de2e0bf3" />

## Tech Stack

- **Backend**: Django 4.2.7
- **Frontend**: Tailwind CSS (via django-tailwind)
- **Database**: SQLite (default, easily configurable for PostgreSQL/MySQL)
- **Forms**: django-widget-tweaks for enhanced form rendering
- **Styling**: Custom Tailwind CSS theme

## Project Structure

```
quiz_app/
├── quiz_app/              # Main Django project directory
│   ├── settings.py        # Django settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── quiz/                  # Quiz application
│   ├── models.py         # Database models (Quiz, Question, Answer, etc.)
│   ├── views.py          # View functions
│   ├── urls.py           # Quiz app URLs
│   ├── forms.py          # Form definitions
│   ├── admin.py          # Admin configuration
│   ├── templates/         # HTML templates
│   │   ├── auth/         # Authentication templates
│   │   ├── quizzes/      # Quiz-related templates
│   │   └── events/       # Event templates
│   └── fixtures/         # Sample data fixtures
├── theme/                 # Tailwind CSS theme
│   └── static_src/       # Tailwind source files
├── static/               # Static files (CSS, JS, images)
├── templates/            # Base templates
├── requirements.txt      # Python dependencies
└── manage.py            # Django management script
```

## Quick Start

Get the Quiz App up and running in minutes!

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)
- Node.js and npm (for Tailwind CSS)

### Setup Instructions

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd Quiz-app
   ```

2. **Create and activate a virtual environment**

   On Windows:

   ```bash
   python -m venv myvenv
   myvenv\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   python3 -m venv myvenv
   source myvenv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   cd quiz_app
   pip install -r requirements.txt
   ```

4. **Install Node.js dependencies (for Tailwind CSS)**

   Make sure you have Node.js installed, then:

   ```bash
   python manage.py tailwind install
   ```

5. **Build Tailwind CSS**

   ```bash
   python manage.py tailwind build
   ```

6. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

7. **Create a superuser (optional, for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

8. **Load sample data (optional)**

   ```bash
   python manage.py loaddata quiz/fixtures/quiz_data.json
   python manage.py loaddata quiz/fixtures/events.json
   ```

9. **Run the development server**

   ```bash
   python manage.py runserver
   ```

10. **Access the application**
    - Open your browser and navigate to `http://127.0.0.1:8000/`
    - Admin panel: `http://127.0.0.1:8000/admin/` (if superuser created)

## Usage

### For Users

1. **Register/Login**: Create an account or log in to access quiz features
2. **Create Quizzes**: Build your own quizzes with multiple choice questions at `/quizzes/create-quiz/`
3. **Create Events**: Organize events with date, location, and description at `/quizzes/create-event/`
4. **Browse Quizzes**: View available quizzes on the quiz list page
5. **Take a Quiz**: Click on a quiz to start taking it (login required)
6. **View Results**: After submission, see your score and detailed results with correct/incorrect answers
7. **Check History**: View all your past quiz attempts with statistics (attempts, average score, percentage)
8. **View Dashboard**: Access your personal dashboard to see all your quizzes and events
9. **View Events**: Browse upcoming events and their details

### For Administrators

1. **Access Admin Panel**: Log in at `/admin/` with superuser credentials
2. **Manage All Quizzes**: Create, edit, and delete any quiz in the system
3. **Add Questions**: Add multiple choice or text-based questions to quizzes using inline editing
4. **Set Correct Answers**: Mark correct answers for automatic grading
5. **View Submissions**: Monitor all user submissions and answers
6. **Manage Events**: Create and manage all events in the system
7. **User Management**: Manage user accounts and permissions

**Admin Features**:

- Inline editing for Questions and Answers within Quiz admin
- Search and filter functionality for all models
- Read-only fields for timestamps and scores
- Organized fieldsets for better data management

## Database Models

- **Quiz**: Stores quiz information (title, description, created_by user, timestamps)
- **Question**: Questions belonging to quizzes (supports MCQ and text types)
- **Answer**: Possible answers for questions (with correct answer flag)
- **UserSubmission**: User quiz attempts with scores, linked to both User and Quiz
- **UserAnswer**: Individual answers submitted by users for each question
- **Event**: Event information (title, date, location, description, created_by user)

### Key Relationships

- Each Quiz and Event is linked to a User via `created_by` field
- UserSubmission links to both the Quiz and the User who took it
- Questions belong to Quizzes, Answers belong to Questions
- UserAnswers belong to UserSubmissions and Questions

## Configuration

### Environment Variables

For production, consider setting:

- `SECRET_KEY`: Django secret key (currently in settings.py)
- `DEBUG`: Set to `False` in production
- `ALLOWED_HOSTS`: Add your domain name
- `DATABASE_URL`: For production database (PostgreSQL recommended)

### Database

The project uses SQLite by default. To use PostgreSQL or MySQL:

1. Install the database adapter:

   ```bash
   pip install psycopg2  # For PostgreSQL
   # or
   pip install mysqlclient  # For MySQL
   ```

2. Update `settings.py` with your database configuration

## API Documentation

### Create Quiz API

The quiz creation endpoint accepts JSON data:

**Endpoint**: `POST /quizzes/create-quiz/`

**Request Body**:

```json
{
  "title": "Quiz Title",
  "description": "Quiz Description",
  "questions": [
    {
      "text": "Question text?",
      "answers": [
        { "text": "Answer 1", "is_correct": true },
        { "text": "Answer 2", "is_correct": false },
        { "text": "Answer 3", "is_correct": false }
      ]
    }
  ]
}
```

**Response**:

- Success: `{"ok": true, "redirect": "/dashboard/"}`
- Error: `{"ok": false, "errors": ["error message"]}`

**Requirements**:

- User must be authenticated
- Quiz title is required
- At least one question is required
- Each question must have at least 2 answers
- Each question must have exactly 1 correct answer

## Development

### Running Tests

```bash
python manage.py test
```

### Collecting Static Files (for production)

```bash
python manage.py collectstatic
```

### Tailwind CSS Development

During development, run Tailwind in watch mode:

```bash
python manage.py tailwind start
```

### Database Migrations

After model changes:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Routes & Endpoints

| Route                    | Description                                | Authentication Required |
| ------------------------ | ------------------------------------------ | ----------------------- |
| `/`                      | Home page with featured quizzes and events | No                      |
| `/register/`             | User registration page                     | No                      |
| `/login/`                | User login page                            | No                      |
| `/logout/`               | User logout                                | Yes                     |
| `/quizzes/`              | List all available quizzes                 | No                      |
| `/quizzes/create-quiz/`  | Create a new quiz (JSON API)               | Yes                     |
| `/quiz/<id>/`            | Take a quiz                                | Yes                     |
| `/result/<id>/`          | View quiz result and answers               | Yes                     |
| `/history/`              | View user's quiz history with statistics   | Yes                     |
| `/dashboard/`            | Personal dashboard (your quizzes/events)   | Yes                     |
| `/quizzes/create-event/` | Create a new event                         | Yes                     |
| `/events/`               | List all events                            | No                      |
| `/events/<id>/`          | View event details                         | Yes                     |
| `/admin/`                | Django admin panel                         | Yes (Superuser)         |

## Project Status

✅ **Active Development** - The project is actively maintained and open for contributions.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines for Python code
- Write clear commit messages
- Add comments for complex logic
- Test your changes before submitting

## License

This project is open source and available under the MIT License.

## Troubleshooting

### Common Issues

**Issue**: Tailwind CSS not working

- **Solution**: Make sure Node.js is installed and run `python manage.py tailwind install` and `python manage.py tailwind build`

**Issue**: Static files not loading

- **Solution**: Run `python manage.py collectstatic` and ensure `DEBUG=True` in development

**Issue**: Database migration errors

- **Solution**: Delete `db.sqlite3` and migration files in `quiz/migrations/` (except `__init__.py`), then run `python manage.py makemigrations` and `python manage.py migrate`

## Recent Updates

### Latest Features Added

- ✅ **User Quiz Creation**: Users can now create their own quizzes via web interface
- ✅ **User Event Creation**: Users can create and manage their own events
- ✅ **Enhanced Dashboard**: Personal dashboard showing user's own quizzes and events
- ✅ **Quiz Statistics**: Quiz history now includes attempts count, average score, and percentage
- ✅ **User Ownership**: All quizzes and events are tracked with creator information
- ✅ **Improved Admin Interface**: Enhanced Django admin with inline editing for questions and answers
- ✅ **User Linking**: Quiz submissions are properly linked to user accounts

## Future Enhancements

- [ ] Timer functionality for quizzes
- [ ] Quiz categories and tags
- [ ] User profiles and avatars
- [ ] Leaderboard system
- [ ] Export quiz results to PDF
- [ ] Email notifications
- [ ] REST API endpoints for mobile apps
- [ ] Quiz sharing functionality
- [ ] Quiz editing interface for creators
- [ ] Question bank/reuse functionality
- [ ] Quiz analytics and insights

## Support

For issues, questions, or contributions, please open an issue on the GitHub repository.

## Acknowledgments

- Built with [Django](https://www.djangoproject.com/)
- Styled with [Tailwind CSS](https://tailwindcss.com/)
- Icons and UI components inspired by modern web design principles

---

**Built with ❤️ using Django and Tailwind CSS**
