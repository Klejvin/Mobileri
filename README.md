 🛋️ Craft Wood – Advanced Furniture Showcase & E-Commerce Platform

Craft Wood is a high-performance, feature-rich web platform designed specifically for furniture manufacturers and interior showrooms. Built with **Python and Django**, this solution seamlessly bridges the gap between digital product discovery, custom interior requests, and direct e-commerce sales. It features a robust, scalable backend architecture paired with an elegant, responsive frontend tailored for high-end visual showcase.


 🛋️ Product Catalog & Custom Showcase
- **Dynamic Interior Catalog:** Categorized management for Living Room, Bedroom, Office, and Custom Woodwork.
- **High-Resolution Image Processing:** Automated image optimization and gallery rendering using Pillow to showcase wood textures and furniture details smoothly.
- **Custom Dimensions & Variants:** Support for custom sizing, wood finishes (Oak, Walnut, MDF), and fabric options per product.

 🛍️ Client Experience & Consultation
- **Session-Based Cart:** A sophisticated cart system tracking selected furniture items across guest and user sessions.
- **Custom Quote & Inquiry System:** Integrated inquiry workflow allowing clients to request custom dimension quotes or schedule interior consultations directly from product pages.
- **Wishlist & Favorites:** Enables clients to curate personal interior moodboards and favorite item lists.
- **Global Context Processors:** Instant navbar updates for cart item counts, saved favorites, and furniture categories across all pages.

 🔐 Security & Client Communication
- **Authentication Suite:** Secure registration, login, and user profile management with Django’s built-in security protocols.
- **Automated Email Notifications:** SMTP integration to automatically send consultation booking confirmations, order receipts, and custom quote updates.
- **Password Recovery:** Secure, token-based "Forgot Password" system.

 📱 Modern Frontend & UI/UX
- **Mobile-First & Elegant UI:** Responsive layout built with Bootstrap 5, custom CSS3, and modern typography tailored for luxury furniture showcase.
- **Interactive Visuals:** JavaScript (ES6) components for interactive product galleries, image zoom, and modal inquiries without full page reloads.

---

 🛠️ Technical Stack

- **Framework:** Django
- **Language:** Python 3.x
- **Frontend:** HTML5, CSS3, JavaScript (ES6+), Bootstrap 5
- **Database:** PostgreSQL (Production) / SQLite (Development)
- **Image Processing:** Pillow
- **Development Environment:** VS Code, Git, Virtualenv

---

 📂 Project Architecture

```text
├── core/                # Project settings, URL routing, and WSGI/ASGI configuration
├── catalog/             # Models for Furniture Products, Categories, Finishes, and Slugs
├── users/               # Authentication
├── templates/           # Modular HTML structure (Base, Navbar, Footer, Modals)
├── static/              # Custom CSS, JavaScript UI scripts, and brand assets
└── media/               # High-resolution product images, wood samples, and gallery uploads
