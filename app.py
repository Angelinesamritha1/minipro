```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
<head>

    <title>F1 Racing - Red Bull Racing</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: #0b0f1a;
            color: white;
        }

        /* NAVIGATION */

        nav {
            background: #071d49;
            padding: 20px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 3px 15px rgba(0,0,0,0.4);
        }

        .logo {
            font-size: 28px;
            font-weight: bold;
        }

        .logo span {
            color: #e10600;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 30px;
            font-weight: bold;
            font-size: 15px;
        }

        nav a:hover {
            color: #e10600;
        }


        /* HERO */

        .hero {
            min-height: 600px;
            padding: 70px 8%;
            display: flex;
            align-items: center;

            background:
                linear-gradient(
                    90deg,
                    #05070d 0%,
                    #071d49 55%,
                    #b40000 100%
                );
        }

        .hero-text {
            width: 50%;
        }

        .small-title {
            color: #e10600;
            letter-spacing: 4px;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .hero h1 {
            font-size: 60px;
            line-height: 1.1;
            margin-bottom: 25px;
        }

        .hero h1 span {
            color: #e10600;
        }

        .hero p {
            font-size: 19px;
            line-height: 1.7;
            color: #d7d7d7;
            margin-bottom: 30px;
        }

        .button {
            display: inline-block;
            background: #e10600;
            color: white;
            padding: 15px 30px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: 0.3s;
        }

        .button:hover {
            background: #ff2b25;
            transform: translateY(-3px);
        }


        /* CAR IMAGE */

        .car {
            width: 50%;
            text-align: center;
        }

        .car img {
            width: 100%;
            max-width: 650px;
            border-radius: 15px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.5);
        }


        /* STATS */

        .stats {
            background: #111827;
            padding: 45px 8%;

            display: flex;
            justify-content: space-between;
            text-align: center;
        }

        .stat {
            flex: 1;
        }

        .stat h2 {
            font-size: 40px;
            color: #e10600;
        }

        .stat p {
            color: #bbbbbb;
            margin-top: 8px;
        }


        /* SECTION */

        .section {
            padding: 70px 8%;
            text-align: center;
        }

        .section h2 {
            font-size: 42px;
            margin-bottom: 45px;
        }


        /* CARDS */

        .cards {
            display: flex;
            gap: 25px;
        }

        .card {
            background: #151b29;
            padding: 35px;
            border-radius: 12px;
            flex: 1;
            text-align: left;
            border: 1px solid #252c3c;
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-8px);
            border-color: #e10600;
        }

        .card .icon {
            font-size: 45px;
            margin-bottom: 15px;
        }

        .card h3 {
            font-size: 23px;
            margin-bottom: 12px;
        }

        .card p {
            color: #b9b9b9;
            line-height: 1.6;
        }


        /* DRIVER */

        .driver {
            background: #071d49;
            padding: 70px 8%;
            display: flex;
            align-items: center;
            gap: 50px;
        }

        .driver-image {
            width: 45%;
        }

        .driver-image img {
            width: 100%;
            border-radius: 15px;
        }

        .driver-info {
            width: 55%;
        }

        .driver-info h2 {
            font-size: 45px;
            margin-bottom: 20px;
        }

        .driver-info span {
            color: #e10600;
        }

        .driver-info p {
            font-size: 18px;
            line-height: 1.7;
            color: #d1d1d1;
        }


        /* RACE */

        .race {
            padding: 70px 8%;
            text-align: center;
            background: #0e1421;
        }

        .race-box {
            max-width: 800px;
            margin: auto;
            background: #151b29;
            padding: 40px;
            border-radius: 15px;
            border-left: 6px solid #e10600;
        }

        .race-box h2 {
            font-size: 35px;
            margin-bottom: 15px;
        }

        .race-box p {
            color: #bbbbbb;
            font-size: 18px;
            margin: 10px;
        }


        /* CHAMPIONSHIP */

        .championship {
            padding: 70px 8%;
            text-align: center;
        }

        .championship h2 {
            font-size: 40px;
            margin-bottom: 20px;
        }

        .championship p {
            max-width: 750px;
            margin: auto;
            color: #bbbbbb;
            line-height: 1.7;
            font-size: 18px;
        }


        /* FOOTER */

        footer {
            background: #05070d;
            text-align: center;
            padding: 40px;
            border-top: 1px solid #252c3c;
        }

        footer h3 {
            font-size: 27px;
            margin-bottom: 12px;
        }

        footer span {
            color: #e10600;
        }

        footer p {
            color: #999;
        }


        /* MOBILE */

        @media (max-width: 800px) {

            nav {
                flex-direction: column;
                gap: 15px;
            }

            nav a {
                margin: 0 8px;
            }

            .hero {
                flex-direction: column;
                text-align: center;
            }

            .hero-text,
            .car {
                width: 100%;
            }

            .hero h1 {
                font-size: 42px;
            }

            .car {
                margin-top: 40px;
            }

            .stats {
                flex-direction: column;
                gap: 30px;
            }

            .cards {
                flex-direction: column;
            }

            .driver {
                flex-direction: column;
                text-align: center;
            }

            .driver-image,
            .driver-info {
                width: 100%;
            }

        }

    </style>

</head>

<body>


    <!-- NAVIGATION -->

    <nav>

        <div class="logo">
            🏁 F1<span>RACING</span>
        </div>

        <div>

            <a href="/">Home</a>
            <a href="#car">F1 Car</a>
            <a href="#driver">Driver</a>
            <a href="#race">Race</a>

        </div>

    </nav>


    <!-- HERO -->

    <section class="hero">

        <div class="hero-text">

            <p class="small-title">
                FORMULA 1 • SPEED • PRECISION
            </p>

            <h1>
                RACE BEYOND<br>
                <span>THE LIMIT.</span>
            </h1>

            <p>
                Experience the speed, technology and
                adrenaline of Formula 1 racing.
                Explore the world of high-performance
                cars, legendary drivers and incredible races.
            </p>

            <a class="button" href="#car">
                Explore F1 →
            </a>

        </div>


        <div class="car" id="car">

            <img
                src="https://images.unsplash.com/photo-1503736334956-4c8f8e92946d?auto=format&fit=crop&w=1000&q=80"
                alt="Formula 1 Racing Car">

        </div>

    </section>


    <!-- STATS -->

    <section class="stats">

        <div class="stat">
            <h2>350+</h2>
            <p>KM/H TOP SPEED</p>
        </div>

        <div class="stat">
            <h2>1000+</h2>
            <p>HORSEPOWER</p>
        </div>

        <div class="stat">
            <h2>24</h2>
            <p>RACES</p>
        </div>

        <div class="stat">
            <h2>20</h2>
            <p>DRIVERS</p>
        </div>

    </section>


    <!-- F1 FEATURES -->

    <section class="section">

        <h2>
            The World of F1 🏎️
        </h2>

        <div class="cards">


            <div class="card">

                <div class="icon">🏎️</div>

                <h3>
                    F1 Machines
                </h3>

                <p>
                    Cutting-edge Formula 1 cars are built
                    for incredible speed, aerodynamics
                    and precision.
                </p>

            </div>


            <div class="card">

                <div class="icon">⚡</div>

                <h3>
                    Extreme Speed
                </h3>

                <p>
                    F1 cars combine powerful engines,
                    advanced technology and lightweight
                    construction.
                </p>

            </div>


            <div class="card">

                <div class="icon">🏆</div>

                <h3>
                    Championship
                </h3>

                <p>
                    Drivers and teams compete throughout
                    the season to become Formula 1 champions.
                </p>

            </div>


            <div class="card">

                <div class="icon">🔧</div>

                <h3>
                    Engineering
                </h3>

                <p>
                    Every detail matters, from aerodynamics
                    to tyre strategy and race setup.
                </p>

            </div>

        </div>

    </section>


    <!-- DRIVER -->

    <section class="driver" id="driver">

        <div class="driver-image">

            <img
                src="https://images.unsplash.com/photo-1547744179-9e5f2e5c5c9d?auto=format&fit=crop&w=900&q=80"
                alt="F1 Driver">

        </div>


        <div class="driver-info">

            <h2>
                Born to <span>Race.</span>
            </h2>

            <p>
                Formula 1 drivers compete at the highest
                level of motorsport. They need incredible
                concentration, physical fitness and
                lightning-fast reactions.
            </p>

            <br>

            <p>
                Every lap is a battle between driver,
                machine and track.
            </p>

        </div>

    </section>


    <!-- NEXT RACE -->

    <section class="race" id="race">

        <h2>
            🏁 Race Weekend
        </h2>

        <div class="race-box">

            <h2>
                Formula 1 Grand Prix
            </h2>

            <p>
                🌍 The Ultimate Racing Experience
            </p>

            <p>
                🏎️ Practice • Qualifying • Race
            </p>

            <p>
                ⚡ Speed • Strategy • Competition
            </p>

        </div>

    </section>


    <!-- CHAMPIONSHIP -->

    <section class="championship">

        <h2>
            Chase the Championship 🏆
        </h2>

        <p>
            Formula 1 is more than just speed.
            It is a combination of engineering,
            teamwork, strategy and driver skill.
            Every race brings new challenges and
            another opportunity to fight for victory.
        </p>

    </section>


    <!-- FOOTER -->

    <footer>

        <h3>
            🏁 F1<span>RACING</span>
        </h3>

        <p>
            Speed. Precision. Passion.
        </p>

        <br>

        <p>
            © 2026 F1 Racing Fan Website
        </p>

    </footer>


</body>
</html>
'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
