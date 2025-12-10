# 🚀 Flipr - Modern Dark Theme Frontend

A stunning, modern dark-themed landing page with beautiful animations and image-based layout for your Django project.

## ✨ Features

### 🎨 Design
- **Dark Theme**: Sleek dark background with vibrant cyan and purple accents
- **Modern Layout**: Image-focused landing page design
- **Responsive**: Fully responsive on mobile, tablet, and desktop
- **Smooth Animations**: Scroll animations, hover effects, and transitions
- **Gradient Elements**: Beautiful gradient text and backgrounds

### 📱 Sections
1. **Navigation Bar**: Sticky navbar with smooth scroll links
2. **Hero Section**: Eye-catching hero with gradient text and CTAs
3. **Features Section**: Showcase your key selling points with icons
4. **About Section**: Image with description
5. **Projects Gallery**: Grid layout for project showcase
6. **Client Testimonials**: Showcase happy clients with images
7. **Contact Form**: Beautiful form for customer inquiries
8. **Newsletter Signup**: Email subscription form
9. **Footer**: Links and social media integration

### 🎯 Interactive Features
- Smooth scroll navigation
- Hover animations on cards and buttons
- Form validation with visual feedback
- AOS (Animate On Scroll) animations
- Ripple effects on button clicks
- Navbar scroll detection
- Real-time form field validation
- Responsive menu for mobile devices

## 🛠️ Technical Stack

- **HTML5**: Semantic markup
- **CSS3**: Custom dark theme with CSS variables
- **JavaScript**: Vanilla JS for interactivity
- **Bootstrap 5**: Grid and responsive utilities
- **Font Awesome 6**: Icon library
- **AOS**: Scroll animation library
- **Django**: Backend framework

## 📁 Project Structure

```
myapp/
├── static/
│   ├── css/
│   │   └── style.css          # Custom CSS utilities and animations
│   ├── js/
│   │   └── main.js            # Interactive JavaScript
│   └── images/
│       ├── about.jpg.jpg
│       └── (project/client images)
└── templates/
    └── index.html             # Main landing page
```

## 🎨 Color Palette

| Color | Hex Value | Usage |
|-------|-----------|-------|
| Primary Cyan | `#00d4ff` | Main accent, buttons, text |
| Secondary Purple | `#7c3aed` | Gradient, accents |
| Accent Pink | `#ff006e` | Hover states, highlights |
| Dark Background | `#0f0f1e` | Main background |
| Card Background | `#1a1a2e` | Card backgrounds |
| Light Text | `#e8e8f0` | Primary text |

## 📦 Dependencies

All dependencies are loaded from CDN:

```html
<!-- Bootstrap 5.3.2 -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Font Awesome 6.4.0 -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<!-- AOS 2.3.4 -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
```

## 🚀 Getting Started

### 1. Ensure Images are in the Correct Location

Place your images in the appropriate folders:

```bash
# Static images
myapp/static/images/about.jpg.jpg

# Project images (uploaded via Django admin)
media/projects/

# Client images (uploaded via Django admin)
media/clients/
```

### 2. Run Django Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

### 3. Add Content via Django Admin

1. Go to `http://127.0.0.1:8000/admin/`
2. Add projects with images and descriptions
3. Add clients with images and testimonials

## 🎨 Customization

### Change Colors

Edit the CSS variables in `index.html` `<style>` section or in `style.css`:

```css
:root {
    --primary: #00d4ff;        /* Change this */
    --secondary: #7c3aed;      /* Change this */
    --dark-bg: #0f0f1e;        /* Change this */
    --card-bg: #1a1a2e;        /* Change this */
    --light-text: #e8e8f0;     /* Change this */
    --accent: #ff006e;         /* Change this */
}
```

### Modify Animations

Adjust animation timing in `main.js`:

```javascript
AOS.init({
    duration: 800,      // Change duration
    offset: 100,        // Change trigger offset
    once: true,         // Change animation repeat
    easing: 'ease-out-cubic'
});
```

### Add New Sections

Follow the pattern of existing sections:

```html
<section class="your-section">
    <div class="container">
        <h2 class="section-title">Your Title</h2>
        <div class="your-grid" data-aos="fade-up">
            <!-- Content here -->
        </div>
    </div>
</section>
```

## 📱 Responsive Breakpoints

- **Desktop**: Full layout, animations enabled
- **Tablet (768px)**: Adjusted font sizes, optimized grid
- **Mobile (576px)**: Single column, touch-friendly buttons

## 🔒 Security

- CSRF protection on forms
- Django form validation
- Client-side form validation
- Secure image uploads

## 📊 Performance

- CDN-hosted libraries
- Lazy loading for images
- Debounced scroll events
- Optimized animations
- Minified CSS and JS

## 🌐 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## 📝 Form Validation

### Contact Form
- Full Name (required)
- Email (required, validated)
- Phone Number (required, validated)
- City (required)

### Newsletter Form
- Email (required, unique)

## 🔧 Troubleshooting

### Images Not Loading
1. Check if media folder exists: `media/`
2. Verify image paths in Django admin
3. Ensure MEDIA_URL and MEDIA_ROOT are configured

### Animations Not Working
1. Check if AOS library is loaded
2. Verify `data-aos` attributes are present
3. Check browser console for errors

### Form Not Submitting
1. Verify Django models are created
2. Check if forms.py is properly configured
3. Ensure CSRF token is in the form

## 📞 Support

For issues or questions:
1. Check console errors (F12)
2. Verify all files are in correct locations
3. Ensure Django server is running
4. Clear browser cache (Ctrl+Shift+Delete)

## 📄 License

This template is free to use and modify for your projects.

---

**Made with ❤️ for beautiful digital experiences**
