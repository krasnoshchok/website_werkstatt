from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Translations dictionary
translations = {
    'de': {
        'company_name': 'AutoRSZ',
        'nav_services': 'Unsere Leistungen',
        'nav_gallery': 'Unsere Galerie',
        'nav_contact': 'Unsere Kontakte',
        'hero_title': 'Ihr zuverlässiger Partner für alle Autoreparaturen',
        'hero_subtitle': 'Professioneller Service für Ihr Fahrzeug',
        'hero_cta': 'Termin vereinbaren',
        'services_title': 'Unsere Leistungen',
        'service_oil': 'Ölwechsel',
        'service_oil_desc': 'Regelmäßiger Ölwechsel mit hochwertigen Ölen für optimale Motorleistung',
        'service_filters': 'Filterwechsel',
        'service_filters_desc': 'Austausch aller Filter: Luft-, Öl-, Kraftstoff- und Innenraumfilter',
        'service_engine': 'Motorprüfung',
        'service_engine_desc': 'Umfassende Motordiagnose mit modernster Technologie',
        'service_climate': 'Klimaanlagenservice',
        'service_climate_desc': 'Wartung und Reparatur Ihrer Klimaanlage für optimalen Komfort',
        'service_brakes': 'Bremsenservice',
        'service_brakes_desc': 'Sicherheitsprüfung und Austausch von Bremsbelägen und -scheiben',
        'service_tires': 'Reifenservice',
        'service_tires_desc': 'Reifenwechsel, Auswuchten und Einlagerung',
        'gallery_title': 'Unsere Galerie',
        'contact_title': 'Kontaktieren Sie uns',
        'contact_address': 'Adresse',
        'contact_phone': 'Telefon',
        'contact_email': 'E-Mail',
        'contact_hours': 'Öffnungszeiten',
        'contact_hours_weekdays': 'Mo-Fr: 8:00 - 18:00',
        'contact_hours_saturday': 'Sa: 9:00 - 14:00',
        'contact_hours_sunday': 'So: Geschlossen',
        'footer_rights': 'Alle Rechte vorbehalten'
    },
    'en': {
        'company_name': 'AutoRSZ',
        'nav_services': 'Our Services',
        'nav_gallery': 'Our Gallery',
        'nav_contact': 'Our Contacts',
        'hero_title': 'Your Reliable Partner for All Car Repairs',
        'hero_subtitle': 'Professional Service for Your Vehicle',
        'hero_cta': 'Book Appointment',
        'services_title': 'Our Services',
        'service_oil': 'Oil Change',
        'service_oil_desc': 'Regular oil changes with high-quality oils for optimal engine performance',
        'service_filters': 'Filter Replacement',
        'service_filters_desc': 'Replacement of all filters: air, oil, fuel, and cabin filters',
        'service_engine': 'Engine Check',
        'service_engine_desc': 'Comprehensive engine diagnostics with state-of-the-art technology',
        'service_climate': 'Air Conditioning Service',
        'service_climate_desc': 'Maintenance and repair of your air conditioning for optimal comfort',
        'service_brakes': 'Brake Service',
        'service_brakes_desc': 'Safety inspection and replacement of brake pads and discs',
        'service_tires': 'Tire Service',
        'service_tires_desc': 'Tire change, balancing, and storage',
        'gallery_title': 'Our Gallery',
        'contact_title': 'Contact Us',
        'contact_address': 'Address',
        'contact_phone': 'Phone',
        'contact_email': 'Email',
        'contact_hours': 'Opening Hours',
        'contact_hours_weekdays': 'Mon-Fri: 8:00 AM - 6:00 PM',
        'contact_hours_saturday': 'Sat: 9:00 AM - 2:00 PM',
        'contact_hours_sunday': 'Sun: Closed',
        'footer_rights': 'All rights reserved'
    }
}


@app.route('/')
def index():
    lang = request.args.get('lang', 'de')
    return render_template('index.html', t=translations.get(lang, translations['de']), lang=lang)


@app.route('/change_language/<lang>')
def change_language(lang):
    if lang in translations:
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'})


if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')

    # Create the HTML template
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="{{ lang }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ t.company_name }}</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
        }

        /* Navigation */
        nav {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            padding: 1rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: bold;
            color: white;
            text-decoration: none;
        }

        .nav-menu {
            display: flex;
            list-style: none;
            gap: 2rem;
            align-items: center;
        }

        .nav-menu a {
            color: white;
            text-decoration: none;
            transition: all 0.3s;
            padding: 0.5rem 1rem;
            border-radius: 5px;
        }

        .nav-menu a:hover {
            background: rgba(255,255,255,0.2);
            transform: translateY(-2px);
        }

        .language-switcher {
            display: flex;
            gap: 0.5rem;
        }

        .lang-btn {
            padding: 0.3rem 0.8rem;
            background: rgba(255,255,255,0.2);
            border: 1px solid white;
            color: white;
            cursor: pointer;
            border-radius: 3px;
            transition: all 0.3s;
        }

        .lang-btn:hover, .lang-btn.active {
            background: white;
            color: #1e3c72;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.4)), 
                        url('https://lh3.googleusercontent.com/p/AF1QipNi_nV8zOCA_EKFUg9Dl73PLEpq7uP9MwROuBpV=s1360-w1360-h1020');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: white;
            margin-top: 70px;
            position: relative;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, 
                rgba(30, 60, 114, 0.8) 0%, 
                rgba(42, 82, 152, 0.6) 50%, 
                rgba(30, 60, 114, 0.8) 100%);
            z-index: 1;
        }

        .hero-content {
            position: relative;
            z-index: 2;
        }

        .hero-content h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            animation: fadeInUp 1s;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }

        .hero-content p {
            font-size: 1.5rem;
            margin-bottom: 2rem;
            animation: fadeInUp 1s 0.2s both;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        }

        .cta-button {
            display: inline-block;
            padding: 1rem 2rem;
            background: #ff6b6b;
            color: white;
            text-decoration: none;
            border-radius: 50px;
            font-size: 1.2rem;
            transition: all 0.3s;
            animation: fadeInUp 1s 0.4s both;
            box-shadow: 0 5px 15px rgba(255,107,107,0.4);
        }

        .cta-button:hover {
            background: #ff5252;
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(255,107,107,0.6);
        }

        /* Sections */
        section {
            padding: 4rem 0;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        h2 {
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 3rem;
            color: #1e3c72;
        }

        /* Services */
        #services {
            background: #f8f9fa;
        }

        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .service-card {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: all 0.3s;
            text-align: center;
        }

        .service-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.15);
        }

        .service-icon {
            width: 80px;
            height: 80px;
            margin: 0 auto 1rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
        }

        .service-card h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: #2a5298;
        }

        /* Gallery */
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
        }

        .gallery-item {
            height: 250px;
            background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
            overflow: hidden;
            position: relative;
            cursor: pointer;
            transition: all 0.3s;
        }

        .gallery-item:hover {
            transform: scale(1.05);
        }

        .gallery-placeholder {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.2rem;
        }

        /* Contact */
        #contact {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
        }

        #contact h2 {
            color: white;
        }

        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
        }

        .contact-item {
            text-align: center;
        }

        .contact-item h3 {
            font-size: 1.3rem;
            margin-bottom: 1rem;
        }

        /* Footer */
        footer {
            background: #1a1a1a;
            color: white;
            text-align: center;
            padding: 2rem 0;
        }

        /* Animations */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Responsive */
        @media (max-width: 768px) {
            .nav-menu {
                flex-direction: column;
                gap: 1rem;
            }

            .hero-content h1 {
                font-size: 2rem;
            }

            .hero-content p {
                font-size: 1.2rem;
            }

            .hero {
                background-attachment: scroll;
            }
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav>
        <div class="nav-container">
            <a href="#" class="logo">{{ t.company_name }}</a>
            <ul class="nav-menu">
                <li><a href="#services" onclick="smoothScroll('services')">{{ t.nav_services }}</a></li>
                <li><a href="#gallery" onclick="smoothScroll('gallery')">{{ t.nav_gallery }}</a></li>
                <li><a href="#contact" onclick="smoothScroll('contact')">{{ t.nav_contact }}</a></li>
                <li class="language-switcher">
                    <button class="lang-btn {% if lang == 'de' %}active{% endif %}" onclick="changeLanguage('de')">DE</button>
                    <button class="lang-btn {% if lang == 'en' %}active{% endif %}" onclick="changeLanguage('en')">EN</button>
                </li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <h1>{{ t.hero_title }}</h1>
            <p>{{ t.hero_subtitle }}</p>
            <a href="#contact" class="cta-button" onclick="smoothScroll('contact')">{{ t.hero_cta }}</a>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services">
        <div class="container">
            <h2>{{ t.services_title }}</h2>
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon">🛢️</div>
                    <h3>{{ t.service_oil }}</h3>
                    <p>{{ t.service_oil_desc }}</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">🔧</div>
                    <h3>{{ t.service_filters }}</h3>
                    <p>{{ t.service_filters_desc }}</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">🔍</div>
                    <h3>{{ t.service_engine }}</h3>
                    <p>{{ t.service_engine_desc }}</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">❄️</div>
                    <h3>{{ t.service_climate }}</h3>
                    <p>{{ t.service_climate_desc }}</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">🚗</div>
                    <h3>{{ t.service_brakes }}</h3>
                    <p>{{ t.service_brakes_desc }}</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">⚙️</div>
                    <h3>{{ t.service_tires }}</h3>
                    <p>{{ t.service_tires_desc }}</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Gallery Section -->
    <section id="gallery">
        <div class="container">
            <h2>{{ t.gallery_title }}</h2>
            <div class="gallery-grid">
                <div class="gallery-item">
                    <div class="gallery-placeholder">Workshop 1</div>
                </div>
                <div class="gallery-item">
                    <div class="gallery-placeholder">Workshop 2</div>
                </div>
                <div class="gallery-item">
                    <div class="gallery-placeholder">Service Area</div>
                </div>
                <div class="gallery-item">
                    <div class="gallery-placeholder">Equipment</div>
                </div>
                <div class="gallery-item">
                    <div class="gallery-placeholder">Team</div>
                </div>
                <div class="gallery-item">
                    <div class="gallery-placeholder">Reception</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <div class="container">
            <h2>{{ t.contact_title }}</h2>
            <div class="contact-grid">
                <div class="contact-item">
                    <h3>{{ t.contact_address }}</h3>
                    <p>Bahnhofstraße 121, 74321 Bietigheim-Bissingen<br>Deutschland</p>
                </div>
                <div class="contact-item">
                    <h3>{{ t.contact_phone }}</h3>
                    <p>+49 162 436 24 70</p>
                </div>
                <div class="contact-item">
                    <h3>{{ t.contact_email }}</h3>
                    <p>info@auto-rsz.de</p>
                </div>
                <div class="contact-item">
                    <h3>{{ t.contact_hours }}</h3>
                    <p>{{ t.contact_hours_weekdays }}<br>
                    {{ t.contact_hours_saturday }}<br>
                    {{ t.contact_hours_sunday }}</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <p>&copy; 2025 {{ t.company_name }}. {{ t.footer_rights }}.</p>
        </div>
    </footer>

    <script>
        function smoothScroll(targetId) {
            event.preventDefault();
            const element = document.getElementById(targetId);
            const navHeight = document.querySelector('nav').offsetHeight;
            const targetPosition = element.offsetTop - navHeight;

            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }

        function changeLanguage(lang) {
            window.location.href = '/?lang=' + lang;
        }
    </script>
</body>
</html>''')

    app.run(debug=True)