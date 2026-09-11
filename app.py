
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Red Bull Racing | F1</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #050b17;
            color: white;
        }


        /* ================= NAVBAR ================= */

        nav {
            height: 80px;
            background: #06101f;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 6%;
            position: sticky;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid #18263b;
        }

        .logo {
            font-size: 25px;
            font-weight: 900;
            line-height: 0.9;
        }

        .logo .oracle {
            font-size: 15px;
            letter-spacing: 2px;
        }

        .logo .redbull {
            color: #e30613;
        }

        .logo .racing {
            color: #d6dce5;
            font-size: 12px;
            letter-spacing: 6px;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 30px;
        }

        nav a {
            text-decoration: none;
            color: white;
            font-size: 14px;
            font-weight: bold;
            transition: 0.3s;
        }

        nav a:hover {
            color: #e30613;
        }


        /* ================= HERO ================= */

        .hero {
            min-height: 650px;

            display: flex;
            align-items: center;

            padding: 70px 6%;

            background:
                linear-gradient(
                    90deg,
                    rgba(3, 8, 17, 0.98) 0%,
                    rgba(5, 15, 30, 0.88) 42%,
                    rgba(7, 20, 45, 0.35) 100%
                ),
                url("https://images.unsplash.com/photo-1503736334956-4c8f8e92946d?auto=format&fit=crop&w=1800&q=90");

            background-size: cover;
            background-position: center;
        }

        .hero-content {
            max-width: 600px;
        }

        .eyebrow {
            color: #e30613;
            font-size: 14px;
            font-weight: bold;
            letter-spacing: 4px;
            margin-bottom: 20px;
        }

        .hero h1 {
            font-size: 70px;
            line-height: 0.95;
            font-weight: 900;
            margin-bottom: 25px;
        }

        .hero h1 span {
            color: #e30613;
        }

        .hero p {
            color: #d4dae3;
            font-size: 18px;
            line-height: 1.7;
            max-width: 550px;
            margin-bottom: 35px;
        }

        .buttons {
            display: flex;
            gap: 15px;
        }

        .btn {
            display: inline-block;
            padding: 15px 28px;
            text-decoration: none;
            font-weight: bold;
            border: 2px solid #e30613;
            transition: 0.3s;
        }

        .btn-primary {
            background: #e30613;
            color: white;
        }

        .btn-primary:hover {
            background: #ff2532;
        }

        .btn-secondary {
            color: white;
            border-color: white;
        }

        .btn-secondary:hover {
            background: white;
            color: #050b17;
        }


        /* ================= PERFORMANCE BAR ================= */

        .performance {
            background: #091525;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            padding: 35px 6%;
            border-bottom: 1px solid #1c2a3e;
        }

        .performance-box {
            text-align: center;
            border-right: 1px solid #26364d;
        }

        .performance-box:last-child {
            border-right: none;
        }

        .performance h2 {
            font-size: 35px;
            color: #e30613;
        }

        .performance p {
            color: #aeb8c7;
            font-size: 13px;
            margin-top: 8px;
            letter-spacing: 1px;
        }


        /* ================= GENERAL SECTION ================= */

        section {
            padding: 80px 6%;
        }

        .section-title {
            margin-bottom: 45px;
        }

        .section-title small {
            color: #e30613;
            font-weight: bold;
            letter-spacing: 3px;
        }

        .section-title h2 {
            font-size: 45px;
            margin-top: 10px;
        }


        /* ================= CAR ================= */

        .car-section {
            background: #050b17;
        }

        .car-container {
            display: flex;
            align-items: center;
            gap: 50px;
        }

        .car-image {
            width: 55%;
        }

        .car-image img {
            width: 100%;
            border-radius: 8px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        }

        .car-info {
            width: 45%;
        }

        .car-info h3 {
            font-size: 35px;
            margin-bottom: 20px;
        }

        .car-info p {
            color: #b8c0cc;
            line-height: 1.7;
            margin-bottom: 25px;
        }

        .specs {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }

        .spec {
            background: #0c1728;
            padding: 20px;
            border-left: 3px solid #e30613;
        }

        .spec strong {
            display: block;
            font-size: 23px;
        }

        .spec span {
            color: #8f9aaa;
            font-size: 13px;
        }


        /* ================= FEATURES ================= */

        .features {
            background: #091525;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
        }

        .feature {
            background: #0d192b;
            padding: 30px;
            border: 1px solid #1b2b43;
            transition: 0.3s;
        }

        .feature:hover {
            transform: translateY(-7px);
            border-color: #e30613;
        }

        .feature-icon {
            font-size: 40px;
            margin-bottom: 20px;
        }

        .feature h3 {
            margin-bottom: 12px;
            font-size: 21px;
        }

        .feature p {
            color: #9fa9b8;
            line-height: 1.6;
            font-size: 15px;
        }


        /* ================= DRIVERS ================= */

        .drivers {
            background: #050b17;
        }

        .driver-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
        }

        .driver {
            background: #0c1728;
            border: 1px solid #1c2b41;
            overflow: hidden;
        }

        .driver-image {
            height: 300px;
            background:
                linear-gradient(
                    135deg,
                    #0a1b39,
                    #101927
                );

            display: flex;
            align-items: center;
            justify-content: center;

            font-size: 100px;
        }

        .driver-info {
            padding: 25px;
        }

        .driver-number {
            color: #e30613;
            font-size: 18px;
            font-weight: bold;
        }

        .driver h3 {
            font-size: 28px;
            margin: 8px 0;
        }

        .driver p {
            color: #9fa9b8;
        }


        /* ================= RACE ================= */

        .race {
            background:
                linear-gradient(
                    120deg,
                    #07152c,
                    #0a0f19
                );
            text-align: center;
        }

        .race-box {
            max-width: 900px;
            margin: auto;
            padding: 50px;
            border: 1px solid #26374e;
            background: #0b1627;
        }

        .race-box h3 {
            font-size: 38px;
            margin-bottom: 15px;
        }

        .race-location {
            color: #e30613;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 25px;
        }

        .race-details {
            display: flex;
            justify-content: center;
            gap: 50px;
            color: #b8c0cc;
        }


        /* ================= NEWS ================= */

        .news {
            background: #091525;
        }

        .news-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
        }

        .news-card {
            background: #0d192b;
            border: 1px solid #1b2b43;
        }

        .news-top {
            height: 180px;
            background:
                linear-gradient(
                    135deg,
                    #0d2c55,
                    #1b1018
                );

            display: flex;
            justify-content: center;
            align-items: center;

            font-size: 65px;
        }

        .news-content {
            padding: 25px;
        }

        .news-content small {
            color: #e30613;
            font-weight: bold;
        }

        .news-content h3 {
            margin: 10px 0;
            font-size: 21px;
        }

        .news-content p {
            color: #9da7b6;
            line-height: 1.5;
        }


        /* ================= FOOTER ================= */

        footer {
            background: #03070e;
            padding: 50px 6%;
            border-top: 1px solid #1c2b40;
        }

        .footer-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .footer-logo {
            font-size: 25px;
            font-weight: bold;
        }

        .footer-logo span {
            color: #e30613;
        }

        .social {
            display: flex;
            gap: 20px;
        }

        .social a {
            color: #c3cbd6;
            text-decoration: none;
        }

        .social a:hover {
            color: #e30613;
        }

        .copyright {
            margin-top: 35px;
            color: #687487;
            text-align: center;
            font-size: 13px;
        }


        /* ================= MOBILE ================= */

        @media (max-width: 900px) {

            nav {
                padding: 15px 5%;
            }

            nav ul {
                gap: 12px;
            }

            nav a {
                font-size: 12px;
            }

            .hero {
                text-align: center;
                padding: 80px 5%;
            }

            .hero h1 {
                font-size: 48px;
            }

            .buttons {
                justify-content: center;
            }

            .performance {
                grid-template-columns: 1fr 1fr;
                gap: 25px;
            }

            .performance-box {
                border-right: none;
            }

            .car-container {
                flex-direction: column;
            }

            .car-image,
            .car-info {
                width: 100%;
            }

            .feature-grid {
                grid-template-columns: 1fr 1fr;
            }

            .driver-grid {
                grid-template-columns: 1fr;
            }

            .news-grid {
                grid-template-columns: 1fr;
            }

            .race-details {
                flex-direction: column;
                gap: 15px;
            }

            .footer-content {
                flex-direction: column;
                gap: 25px;
            }
        }


        @media (max-width: 600px) {

            nav {
                height: auto;
                flex-direction: column;
                gap: 15px;
                padding: 20px;
            }

            nav ul {
                flex-wrap: wrap;
                justify-content: center;
            }

            .hero h1 {
                font-size: 40px;
            }

            .hero p {
                font-size: 16px;
            }

            .buttons {
                flex-direction: column;
            }

            .performance {
                grid-template-columns: 1fr;
            }

            .feature-grid {
                grid-template-columns: 1fr;
            }

            .section-title h2 {
                font-size: 35px;
            }

            .specs {
                grid-template-columns: 1fr;
            }
        }

    </style>

</head>


<body>


    <!-- NAVIGATION -->

    <nav>

        <div class="logo">

            <div class="oracle">
                ORACLE
            </div>

            <div class="redbull">
                Red Bull
            </div>

            <div class="racing">
                RACING
            </div>

        </div>


        <ul>

            <li>
                <a href="#home">HOME</a>
            </li>

            <li>
                <a href="#car">CAR</a>
            </li>

            <li>
                <a href="#drivers">DRIVERS</a>
            </li>

            <li>
                <a href="#race">RACE</a>
            </li>

            <li>
                <a href="#news">NEWS</a>
            </li>

        </ul>

    </nav>


    <!-- HERO -->

    <section class="hero" id="home">

        <div class="hero-content">

            <div class="eyebrow">
                ORACLE RED BULL RACING
            </div>

            <h1>
                FASTER<br>
                STRONGER<br>
                <span>TOGETHER.</span>
            </h1>

            <p>
                Welcome to the world of Formula 1.
                Experience speed, precision, engineering
                and the relentless pursuit of victory.
            </p>

            <div class="buttons">

                <a href="#car" class="btn btn-primary">
                    EXPLORE THE CAR →
                </a>

                <a href="#drivers" class="btn btn-secondary">
                    OUR DRIVERS
                </a>

            </div>

        </div>

    </section>


    <!-- PERFORMANCE -->

    <div class="performance">

        <div class="performance-box">

            <h2>350+</h2>
            <p>KM/H TOP SPEED</p>

        </div>


        <div class="performance-box">

            <h2>1000+</h2>
            <p>HORSEPOWER</p>

        </div>


        <div class="performance-box">

            <h2>24</h2>
            <p>GRAND PRIX</p>

        </div>


        <div class="performance-box">

            <h2>2.6s</h2>
            <p>0–100 KM/H</p>

        </div>

    </div>


    <!-- CAR -->

    <section class="car-section" id="car">

        <div class="section-title">

            <small>THE MACHINE</small>

            <h2>Built To Dominate.</h2>

        </div>


        <div class="car-container">

            <div class="car-image">

                <img
                    src="https://images.unsplash.com/photo-1503736334956-4c8f8e92946d?auto=format&fit=crop&w=1200&q=90"
                    alt="Formula 1 Racing Car">

            </div>


            <div class="car-info">

                <h3>
                    Formula 1 Engineering
                </h3>

                <p>
                    Every part of an F1 car is designed
                    around one goal — maximum performance.
                    Aerodynamics, power, tyres and strategy
                    work together to create one of the fastest
                    racing machines on the planet.
                </p>


                <div class="specs">

                    <div class="spec">
                        <strong>1000+</strong>
                        <span>HORSEPOWER</span>
                    </div>

                    <div class="spec">
                        <strong>350+</strong>
                        <span>KM/H</span>
                    </div>

                    <div class="spec">
                        <strong>798 KG</strong>
                        <span>MINIMUM WEIGHT</span>
                    </div>

                    <div class="spec">
                        <strong>1.5G+</strong>
                        <span>HIGH SPEED BRAKING</span>
                    </div>

                </div>

            </div>

        </div>

    </section>


    <!-- FEATURES -->

    <section class="features">

        <div class="section-title">

            <small>THE F1 WORLD</small>

            <h2>More Than Racing.</h2>

        </div>


        <div class="feature-grid">


            <div class="feature">

                <div class="feature-icon">
                    🏎️
                </div>

                <h3>
                    Aerodynamics
                </h3>

                <p>
                    Advanced aerodynamic design generates
                    downforce while keeping the car fast
                    and efficient.
                </p>

            </div>


            <div class="feature">

                <div class="feature-icon">
                    ⚡
                </div>

                <h3>
                    Power
                </h3>

                <p>
                    Hybrid power units deliver incredible
                    acceleration and performance.
                </p>

            </div>


            <div class="feature">

                <div class="feature-icon">
                    🧠
                </div>

                <h3>
                    Strategy
                </h3>

                <p>
                    Teams constantly analyze tyres,
                    weather and race data to make
                    critical decisions.
                </p>

            </div>


            <div class="feature">

                <div class="feature-icon">
                    🔧
                </div>

                <h3>
                    Pit Crew
                </h3>

                <p>
                    A professional pit crew can change
                    all four tyres in just a few seconds.
                </p>

            </div>


        </div>

    </section>


    <!-- DRIVERS -->

    <section class="drivers" id="drivers">

        <div class="section-title">

            <small>THE DRIVERS</small>

            <h2>Born To Race.</h2>

        </div>


        <div class="driver-grid">


            <div class="driver">

                <div class="driver-image">
                    🏁
                </div>

                <div class="driver-info">

                    <div class="driver-number">
                        DRIVER 01
                    </div>

                    <h3>
                        Max Verstappen
                    </h3>

                    <p>
                        Speed. Focus. Precision.
                        A championship-winning driver
                        known for his aggressive racing style.
                    </p>

                </div>

            </div>


            <div class="driver">

                <div class="driver-image">
                    🏎️
                </div>

                <div class="driver-info">

                    <div class="driver-number">
                        DRIVER 11
                    </div>

                    <h3>
                        Sergio Pérez
                    </h3>

                    <p>
                        Experience, consistency and race
                        craft developed through years at
                        the highest level of motorsport.
                    </p>

                </div>

            </div>


        </div>

    </section>


    <!-- RACE -->

    <section class="race" id="race">

        <div class="section-title">

            <small>RACE WEEKEND</small>

            <h2>Feel The Speed.</h2>

        </div>


        <div class="race-box">

            <h3>
                FORMULA 1 GRAND PRIX
            </h3>

            <div class="race-location">
                🏁 SPEED • STRATEGY • VICTORY
            </div>


            <div class="race-details">

                <div>
                    <strong>PRACTICE</strong>
                    <br>
                    Prepare the car
                </div>

                <div>
                    <strong>QUALIFYING</strong>
                    <br>
                    Fight for pole
                </div>

                <div>
                    <strong>RACE</strong>
                    <br>
                    Chase victory
                </div>

            </div>

        </div>

    </section>


    <!-- NEWS -->

    <section class="news" id="news">

        <div class="section-title">

            <small>LATEST</small>

            <h2>Inside F1.</h2>

        </div>


        <div class="news-grid">


            <div class="news-card">

                <div class="news-top">
                    🏎️
                </div>

                <div class="news-content">

                    <small>F1 TECHNOLOGY</small>

                    <h3>
                        Engineering For Speed
                    </h3>

                    <p>
                        Discover how engineers turn
                        advanced technology into
                        racing performance.
                    </p>

                </div>

            </div>


            <div class="news-card">

                <div class="news-top">
                    🏆
                </div>

                <div class="news-content">

                    <small>CHAMPIONSHIP</small>

                    <h3>
                        The Fight For Victory
                    </h3>

                    <p>
                        Every point matters throughout
                        the Formula 1 championship season.
                    </p>

                </div>

            </div>


            <div class="news-card">

                <div class="news-top">
                    ⚡
                </div>

                <div class="news-content">

                    <small>RACE DAY</small>

                    <h3>
                        Speed Meets Strategy
                    </h3>

                    <p>
                        From tyre strategy to pit stops,
                        every decision can change a race.
                    </p>

                </div>

            </div>


        </div>

    </section>


    <!-- FOOTER -->

    <footer>

        <div class="footer-content">

            <div class="footer-logo">

                <span>RED BULL</span>
                RACING

            </div>


            <div class="social">

                <a href="#">
                    YouTube
                </a>

                <a href="#">
                    Instagram
                </a>

                <a href="#">
                    X
                </a>

                <a href="#">
                    Facebook
                </a>

            </div>

        </div>


        <div class="copyright">

            © 2026 F1 Racing Fan Website.
            Created for educational purposes.

        </div>

    </footer>


</body>

</html>
'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
