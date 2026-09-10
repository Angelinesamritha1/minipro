from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Angeline Paws - Dog Website</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: #fffaf5;
            color: #263238;
        }

        /* Navigation Bar */
        nav {
            background: white;
            padding: 20px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        }

        .logo {
            font-size: 28px;
            font-weight: bold;
        }

        .logo span {
            color: #c45b25;
        }

        nav a {
            text-decoration: none;
            color: #333;
            margin-left: 30px;
            font-size: 16px;
        }

        nav a:hover {
            color: #c45b25;
        }

        /* Hero Section */
        .hero {
            min-height: 500px;
            display: flex;
            align-items: center;
            padding: 60px 8%;
            background: #f7eadb;
        }

        .hero-text {
            width: 50%;
        }

        .hero-text .small-title {
            font-size: 15px;
            letter-spacing: 3px;
            font-weight: bold;
            margin-bottom: 15px;
        }

        .hero-text h1 {
            font-size: 55px;
            margin-bottom: 20px;
        }

        .hero-text h1 span {
            color: #c45b25;
        }

        .hero-text p {
            font-size: 20px;
            line-height: 1.6;
            margin-bottom: 30px;
        }

        .button {
            display: inline-block;
            background: #c45b25;
            color: white;
            padding: 15px 30px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
        }

        .button:hover {
            background: #9f461d;
        }

        /* Dog Image */
        .dog {
            width: 50%;
            text-align: center;
        }

        .dog img {
            width: 90%;
            max-width: 500px;
            border-radius: 25px;
        }

        /* Why Dogs Section */
        .section {
            padding: 60px 8%;
            text-align: center;
        }

        .section h2 {
            font-size: 40px;
            margin-bottom: 40px;
        }

        .cards {
            display: flex;
            justify-content: space-between;
            gap: 25px;
        }

        .card {
            background: white;
            padding: 30px;
            border-radius: 15px;
            flex: 1;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .card h3 {
            margin: 15px 0;
            font-size: 22px;
        }

        .card p {
            color: #666;
            line-height: 1.5;
        }

        .icon {
            font-size: 45px;
        }

        /* About Section */
        .about {
            background: #f7eadb;
            padding: 60px 8%;
            text-align: center;
        }

        .about h2 {
            font-size: 40px;
            margin-bottom: 20px;
        }

        .about p {
            max-width: 800px;
            margin: auto;
            font-size: 18px;
            line-height: 1.7;
        }

        /* Footer */
        footer {
            background: #263238;
            color: white;
            text-align: center;
            padding: 30px;
        }

        footer h3 {
            font-size: 25px;
            margin-bottom: 10px;
        }

        /* Mobile */
        @media (max-width: 800px) {

            nav {
                flex-direction: column;
                gap: 15px;
            }

            nav a {
                margin-left: 10px;
                margin-right: 10px;
            }

            .hero {
                flex-direction: column;
                text-align: center;
            }

            .hero-text,
            .dog {
                width: 100%;
            }

            .dog {
                margin-top: 30px;
            }

            .hero-text h1 {
                font-size: 40px;
            }

            .cards {
                flex-direction: column;
            }
        }
    </style>
</head>

<body>

    <!-- Navigation -->
    <nav>

        <div class="logo">
            🐾 Angel<span>Paws</span>
        </div>

        <div>
            <a href="/">Home</a>
            <a href="#about">About</a>
            <a href="#dogs">Dogs</a>
            <a href="#contact">Contact</a>
        </div>

    </nav>


    <!-- Hero Section -->
    <section class="hero">

        <div class="hero-text">

            <p class="small-title">
                HAPPIER DOGS • BRIGHTER DAYS
            </p>

            <h1>
                Welcome to <span>Angel Paws</span> 🐾
            </h1>

            <p>
                A small place for big dog lovers.
                Discover cute dogs, useful tips and
                learn how to keep them happy and healthy.
            </p>

            <a class="button" href="#dogs">
                Explore Dogs →
            </a>

        </div>


        <div class="dog">

            <img
                src="https://images.unsplash.com/photo-1552053831-71594a27632d?auto=format&fit=crop&w=800&q=80"
                alt="Cute Dog">

        </div>

    </section>


    <!-- Why Dogs -->
    <section class="section" id="dogs">

        <h2>
            Why Dogs? 🐶
        </h2>

        <div class="cards">

            <div class="card">

                <div class="icon">🐾</div>

                <h3>
                    Loyal Companions
                </h3>

                <p>
                    Dogs are always there for you,
                    no matter what.
                </p>

            </div>


            <div class="card">

                <div class="icon">❤️</div>

                <h3>
                    Better Health
                </h3>

                <p>
                    Dogs can help reduce stress
                    and keep you active.
                </p>

            </div>


            <div class="card">

                <div class="icon">😊</div>

                <h3>
                    More Happiness
                </h3>

                <p>
                    A happy dog can brighten
                    your entire day.
                </p>

            </div>


            <div class="card">

                <div class="icon">🏠</div>

                <h3>
                    A Loving Home
                </h3>

                <p>
                    Every dog deserves a safe
                    and caring home.
                </p>

            </div>

        </div>

    </section>


    <!-- About Section -->
    <section class="about" id="about">

        <h2>
            About Angel Paws 🐶
        </h2>

        <p>
            Angel Paws is a simple website created
            for people who love dogs. Our goal is to
            share the happiness, friendship and
            love that dogs bring into our lives.
        </p>

    </section>


    <!-- Footer -->
    <footer id="contact">

        <h3>
            🐾 Angel Paws
        </h3>

        <p>
            Dogs make life better ❤️
        </p>

        <br>

        <p>
            © 2026 Angel Paws. All rights reserved.
        </p>

    </footer>

</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
