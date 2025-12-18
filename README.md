# Django Projects Collection

This repository contains two Django applications: a **Music Player** and a **Tweet App**, both with modern, responsive designs.

## 📁 Project Structure

```
├── project/
│   ├── MusicPlayer/          # Music Player Django Project
│   │   ├── App/              # Music player application
│   │   │   ├── models.py     # Song model
│   │   │   ├── views.py      # Music player views
│   │   │   ├── templates/    # HTML templates
│   │   │   └── static/       # CSS, JS, images
│   │   └── manage.py
│   └── tweet/                # Tweet App Django Project
│       ├── first/            # Tweet application
│       │   ├── models.py     # Tweet model
│       │   ├── views.py      # Tweet CRUD views
│       │   ├── forms.py      # Tweet forms
│       │   └── templates/    # HTML templates
│       └── manage.py
└── README.md
```

---

## 🎵 Music Player App

A beautiful music player with pagination, audio controls, and modern styling.

### Features
- **Song Management**: Upload songs with images, audio files, and metadata
- **Audio Player**: MediaElement.js integration with play/pause, progress bar, volume control
- **Pagination**: Navigate between songs (1 song per page)
- **Responsive Design**: Dark theme with gradient backgrounds
- **Admin Panel**: Add/edit songs through Django admin

### Technologies Used
- Django 5.2.7
- MediaElement.js for audio playback
- Bootstrap & custom CSS
- SQLite database
- Font Awesome icons

### Setup Instructions

1. **Navigate to Music Player**
   ```bash
   cd project
   ```

2. **Install Dependencies**
   ```bash
   pip install django pillow
   ```

3. **Run Migrations**
   ```bash
   py manage.py makemigrations
   py manage.py migrate
   ```

4. **Create Superuser**
   ```bash
   py manage.py createsuperuser
   ```

5. **Start Server**
   ```bash
   py manage.py runserver
   ```

6. **Add Songs**
   - Visit: `http://127.0.0.1:8000/admin/`
   - Login and add songs with images and audio files

7. **View Music Player**
   - Visit: `http://127.0.0.1:8000/`

### Music Player Features
- **Song Model Fields**:
  - Title, Artist, Duration
  - Album cover image
  - Audio file upload
  - Optional streaming URL
  - Lyrics (optional)

- **Player Controls**:
  - Play/Pause button
  - Progress bar with seek
  - Volume control
  - Previous/Next navigation
  - Time display

---

## 🐦 Tweet App

A Twitter-like social media application with CRUD operations and modern UI.

### Features
- **Tweet Management**: Create, read, update, delete tweets
- **Image Upload**: Attach photos to tweets
- **User Authentication**: Tweet ownership and permissions
- **Responsive Design**: Purple gradient theme with card layouts
- **Modern UI**: Bootstrap 5 with custom styling

### Technologies Used
- Django 5.2.7
- Bootstrap 5.3.8
- Font Awesome icons
- SQLite database
- Custom CSS with gradients

### Setup Instructions

1. **Navigate to Tweet App**
   ```bash
   cd project/tweet
   ```

2. **Install Dependencies**
   ```bash
   pip install django pillow
   ```

3. **Run Migrations**
   ```bash
   py manage.py makemigrations
   py manage.py migrate
   ```

4. **Create Superuser**
   ```bash
   py manage.py createsuperuser
   ```

5. **Start Server**
   ```bash
   py manage.py runserver
   ```

6. **Access Application**
   - Home: `http://127.0.0.1:8000/`
   - All Tweets: `http://127.0.0.1:8000/tweets/`
   - Create Tweet: `http://127.0.0.1:8000/create/`

### Tweet App Features
- **Tweet Model Fields**:
  - Text content
  - Photo upload
  - User association
  - Timestamp

- **CRUD Operations**:
  - Create new tweets with text and images
  - View all tweets in card layout
  - Edit existing tweets (owner only)
  - Delete tweets (owner only)

- **UI Components**:
  - Gradient navbar with navigation
  - Card-based tweet display
  - Styled forms with validation
  - Responsive grid layout
  - Hover effects and animations

---

## 🎨 Design Features

### Music Player Design
- **Dark Theme**: Black background with purple accents
- **Gradient Elements**: Smooth color transitions
- **Card Layout**: Centered music player container
- **Custom Controls**: Styled audio player with MediaElement.js
- **Typography**: Clean fonts with proper hierarchy

### Tweet App Design
- **Purple Gradient Background**: Modern diagonal gradient
- **Blue Gradient Navbar**: Professional navigation bar
- **White Content Cards**: Clean, rounded containers
- **Hover Effects**: Interactive elements with smooth transitions
- **Form Styling**: Custom input fields with focus states
- **Icon Integration**: Font Awesome icons throughout

---

## 🚀 Quick Start

### Music Player
```bash
cd project
py manage.py runserver
# Visit: http://127.0.0.1:8000/
```

### Tweet App
```bash
cd project/tweet
py manage.py runserver
# Visit: http://127.0.0.1:8000/
```

---

## 📝 Notes

- Both applications use SQLite for development
- Media files are stored in `media/` directories
- Static files (CSS/JS) are in respective `static/` folders
- Both apps include admin panel integration
- Responsive design works on mobile and desktop

---

## 🛠️ Troubleshooting

### Common Issues

1. **Static files not loading**
   ```bash
   py manage.py collectstatic
   ```

2. **Media files not displaying**
   - Check `MEDIA_URL` and `MEDIA_ROOT` in settings
   - Ensure media URLs are configured in main `urls.py`

3. **Audio not playing**
   - Check browser console for JavaScript errors
   - Ensure MediaElement.js libraries are loading
   - Verify audio file format (MP3 recommended)

4. **Database errors**
   ```bash
   py manage.py makemigrations
   py manage.py migrate
   ```

---

## 📄 License

This project is for educational purposes. Feel free to use and modify as needed.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

**Enjoy building with Django! 🎉**