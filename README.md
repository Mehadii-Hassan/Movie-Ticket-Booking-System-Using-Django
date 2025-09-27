<h1 align="center">🎬 MovieTix - Online Movie Booking System</h1>
<p align="center">
A <strong>Django</strong>-based comprehensive online movie ticket booking platform with 
<strong>real-time seat selection</strong>, <strong>payment processing</strong>, and <strong>digital ticket generation</strong>.
</p>
<hr>
<h2>⚙️ Setup Instructions</h2>
<ol>
  <li>Clone the repository</li>
  <pre><code>git clone https://github.com/your-username/movietix.git
cd movietix</code></pre>
  <li>Create virtual environment and install dependencies</li>
  <pre><code>python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux  
source venv/bin/activate

pip install -r requirements.txt</code></pre>
  <li>Set up database</li>
  <pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>
  <li>Create superuser (optional)</li>
  <pre><code>python manage.py createsuperuser</code></pre>
  <li>Load sample data (optional)</li>
  <ul>
    <li>Run <code>python manage.py shell</code></li>
    <li>Copy and paste the sample data script from documentation</li>
  </ul>
  <li>Run the development server</li>
  <pre><code>python manage.py runserver</code></pre>
  <li>Visit the application</li>
  <ul>
    <li>Main site: <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a></li>
    <li>Admin panel: <a href="http://127.0.0.1:8000/admin/">http://127.0.0.1:8000/admin/</a></li>
  </ul>
</ol>
<hr>
<h2>🧪 How It Works</h2>
<ul>
  <li>👤 <strong>User Registration/Login</strong> - Secure authentication system</li>
  <li>🎥 <strong>Movie Browsing</strong> - Browse available movies with:
    <ul>
      <li>Movie posters and details</li>
      <li>Duration, genre, and ratings</li>
      <li>Multiple showtimes</li>
      <li>Theater locations</li>
    </ul>
  </li>
  <li>💺 <strong>Interactive Seat Selection</strong> - Real-time seat booking with:
    <ul>
      <li>🟢 Available seats</li>
      <li>🔵 Selected seats</li>
      <li>🔴 Already booked seats</li>
    </ul>
  </li>
  <li>💳 <strong>Payment Processing</strong> - Multiple payment methods:
    <ul>
      <li>Credit/Debit Card</li>
      <li>Mobile Banking</li>
      <li>Online Banking</li>
    </ul>
  </li>
  <li>🎫 <strong>Digital Tickets</strong> - Download/print tickets with QR codes</li>
  <li>👨‍💼 <strong>Admin Management</strong> - Complete CRUD operations for movies, theaters, and bookings</li>
</ul>
<hr>
<h2>📂 File Structure</h2>
<pre>
movietix/
├── movietix_project/          # Main Django project settings
├── movies/                    # Movie management app
├── accounts/                  # User authentication app  
├── bookings/                  # Booking management app
├── templates/                 # HTML templates
│   ├── movies/               # Movie-related templates
│   ├── accounts/             # Authentication templates
│   └── bookings/             # Booking templates
├── static/                   # CSS, JavaScript, images
├── media/                    # Uploaded files (movie posters)
├── manage.py                 # Django management script
├── requirements.txt          # Project dependencies
├── db.sqlite3               # SQLite database
└── README.md                # Project documentation
</pre>
<hr>
<h2>✨ Key Features</h2>
<ul>
  <li>🔐 <strong>Authentication System</strong> - User registration, login, and profile management</li>
  <li>🎬 <strong>Movie Management</strong> - Admin can add/edit movies with posters and details</li>
  <li>🏛️ <strong>Theater System</strong> - Multiple theaters with customizable seat layouts</li>
  <li>⚡ <strong>Real-time Booking</strong> - Live seat availability updates</li>
  <li>💸 <strong>Payment Gateway</strong> - Integrated payment processing simulation</li>
  <li>📱 <strong>Responsive Design</strong> - Works seamlessly on all devices</li>
  <li>📊 <strong>Booking History</strong> - Users can view their booking history</li>
  <li>🎫 <strong>Ticket Generation</strong> - Professional digital tickets with download option</li>
</ul>
<hr>
<h2>🛠️ Technology Stack</h2>
<ul>
  <li><strong>Backend:</strong> Django 5.0.1</li>
  <li><strong>Database:</strong> SQLite (easily changeable to PostgreSQL/MySQL)</li>
  <li><strong>Frontend:</strong> HTML5, CSS3, JavaScript, Bootstrap 5</li>
  <li><strong>Image Processing:</strong> Pillow</li>
  <li><strong>Authentication:</strong> Django built-in auth system</li>
</ul>
<hr>
<h2>📱 Screenshots & Demo</h2>
<ul>
  <li>🏠 <strong>Home Page</strong> - Movie listings with posters</li>
  <li>🎬 <strong>Movie Details</strong> - Detailed movie information and showtimes</li>
  <li>💺 <strong>Seat Selection</strong> - Interactive theater seat map</li>
  <li>💳 <strong>Payment Page</strong> - Secure payment processing</li>
  <li>🎫 <strong>Digital Ticket</strong> - Downloadable ticket with QR code</li>
  <li>👨‍💼 <strong>Admin Dashboard</strong> - Complete management system</li>
</ul>
<hr>
<h2>🚀 Quick Start Commands</h2>
<pre><code># Clone and setup
git clone https://github.com/your-username/movietix.git
cd movietix
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt && python manage.py migrate
python manage.py runserver

# Visit: http://127.0.0.1:8000/
</code></pre>
<hr>
<h2>🙌 Credits</h2>
<p>
Created by <strong>Mehedi Hassan</strong> using <code>Django</code> and <code>Bootstrap</code>.  
Special thanks to <a href="https://www.djangoproject.com/">Django</a> for providing a powerful web framework and 
<a href="https://getbootstrap.com/">Bootstrap</a> for responsive UI components.
</p>
<hr>
<p align="center">⭐ Star this repo if you find it useful for building Django web applications!</p>
