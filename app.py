from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Off-Road Riders | Adventure Bike Event</title>

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
            background: #0d0f0f;
            color: white;
        }

        /* NAVIGATION */

        nav {
            height: 75px;
            background: #101313;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 9%;
            position: sticky;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid #292d2d;
        }

        .logo {
            font-size: 23px;
            font-weight: bold;
            letter-spacing: 1px;
        }

        .logo span {
            color: #ff7300;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 35px;
        }

        nav a {
            text-decoration: none;
            color: #ddd;
            font-weight: bold;
            font-size: 15px;
        }

        nav a:hover {
            color: #ff7300;
        }

        .nav-button {
            background: #ff7300;
            color: black !important;
            padding: 13px 25px;
            border-radius: 30px;
        }

        /* HERO */

        .hero {
            min-height: 650px;
            background:
                linear-gradient(
                    90deg,
                    rgba(5, 7, 7, 0.95) 0%,
                    rgba(5, 7, 7, 0.75) 40%,
                    rgba(5, 7, 7, 0.2) 100%
                ),
                url("https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=1800&q=90");

            background-size: cover;
            background-position: center;

            display: flex;
            align-items: center;
            padding: 80px 9%;
        }

        .hero-content {
            max-width: 650px;
        }

        .small-title {
            color: #ff7300;
            font-weight: bold;
            letter-spacing: 4px;
            margin-bottom: 20px;
            font-size: 14px;
        }

        .hero h1 {
            font-size: 70px;
            line-height: 0.95;
            text-transform: uppercase;
            margin-bottom: 25px;
        }

        .hero h1 span {
            color: #ff7300;
        }

        .hero p {
            color: #ddd;
            font-size: 19px;
            line-height: 1.7;
            max-width: 600px;
            margin-bottom: 30px;
        }

        .buttons {
            display: flex;
            gap: 15px;
        }

        .button {
            display: inline-block;
            padding: 16px 30px;
            background: #ff7300;
            color: black;
            text-decoration: none;
            font-weight: bold;
            border-radius: 5px;
        }

        .button:hover {
            background: #ff8b2b;
        }

        .button-dark {
            display: inline-block;
            padding: 16px 30px;
            border: 1px solid white;
            color: white;
            text-decoration: none;
            font-weight: bold;
            border-radius: 5px;
        }

        .button-dark:hover {
            background: white;
            color: black;
        }

        /* STATS */

        .stats {
            background: #171a1a;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            padding: 35px 9%;
            gap: 20px;
        }

        .stat {
            text-align: center;
            border-right: 1px solid #333;
        }

        .stat:last-child {
            border-right: none;
        }

        .stat h2 {
            color: #ff7300;
            font-size: 35px;
        }

        .stat p {
            color: #aaa;
            margin-top: 7px;
            text-transform: uppercase;
            font-size: 12px;
            letter-spacing: 2px;
        }

        /* SECTION */

        .section {
            padding: 90px 9%;
        }

        .section-title {
            text-align: center;
            margin-bottom: 55px;
        }

        .section-title small {
            color: #ff7300;
            font-weight: bold;
            letter-spacing: 3px;
        }

        .section-title h2 {
            font-size: 48px;
            margin-top: 12px;
        }

        .section-title p {
            color: #aaa;
            max-width: 650px;
            margin: 15px auto;
            line-height: 1.6;
        }

        /* FEATURES */

        .features {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 25px;
        }

        .feature {
            background: #171a1a;
            padding: 35px 25px;
            border-radius: 8px;
            border: 1px solid #292d2d;
            transition: 0.3s;
        }

        .feature:hover {
            transform: translateY(-8px);
            border-color: #ff7300;
        }

        .feature .icon {
            font-size: 42px;
            margin-bottom: 20px;
        }

        .feature h3 {
            margin-bottom: 12px;
        }

        .feature p {
            color: #999;
            line-height: 1.6;
        }

        /* BIKE */

        .bike-section {
            background: #121515;
        }

        .bike-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 55px;
            align-items: center;
        }

        .bike-image img {
            width: 100%;
            height: 450px;
            object-fit: cover;
            border-radius: 10px;
        }

        .bike-info h2 {
            font-size: 48px;
            margin-bottom: 20px;
        }

        .bike-info h2 span {
            color: #ff7300;
        }

        .bike-info p {
            color: #aaa;
            line-height: 1.8;
            margin-bottom: 25px;
        }

        .bike-specs {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 30px;
        }

        .spec {
            background: #1b1f1f;
            padding: 18px;
            border-left: 3px solid #ff7300;
        }

        .spec strong {
            display: block;
            font-size: 20px;
        }

        .spec span {
            color: #888;
            font-size: 13px;
        }

        /* FRIENDS */

        .riders {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
        }

        .rider {
            background: #171a1a;
            border-radius: 10px;
            overflow: hidden;
        }

        .rider img {
            width: 100%;
            height: 300px;
            object-fit: cover;
        }

        .rider-info {
            padding: 25px;
        }

        .rider-info h3 {
            font-size: 23px;
            margin-bottom: 8px;
        }

        .rider-info p {
            color: #888;
        }

        /* EVENT */

        .event {
            background:
                linear-gradient(rgba(8, 10, 10, 0.85), rgba(8, 10, 10, 0.9)),
                url("https://images.unsplash.com/photo-1503736334956-4c8f8e92946d?auto=format&fit=crop&w=1600&q=90");

            background-size: cover;
            background-position: center;
            text-align: center;
        }

        .event-box {
            max-width: 850px;
            margin: auto;
        }

        .event h2 {
            font-size: 55px;
            margin-bottom: 20px;
        }

        .event h2 span {
            color: #ff7300;
        }

        .event p {
            color: #ccc;
            line-height: 1.7;
            font-size: 18px;
            margin-bottom: 30px;
        }

        .event-details {
            display: flex;
            justify-content: center;
            gap: 50px;
            margin: 35px 0;
        }

        .detail h3 {
            color: #ff7300;
            margin-bottom: 7px;
        }

        .detail p {
            font-size: 15px;
            margin: 0;
        }

        /* GALLERY */

        .gallery {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 18px;
        }

        .gallery img {
            width: 100%;
            height: 260px;
            object-fit: cover;
            border-radius: 8px;
            transition: 0.3s;
        }

        .gallery img:hover {
            transform: scale(1.03);
        }

        /* FOOTER */

        footer {
            background: #080a0a;
            padding: 45px 9%;
            text-align: center;
            border-top: 1px solid #292d2d;
        }

        footer h2 {
            margin-bottom: 12px;
        }

        footer span {
            color: #ff7300;
        }

        footer p {
            color: #777;
        }

        /* MOBILE */

        @media (max-width: 900px) {

            nav {
                padding: 0 5%;
            }

            nav ul {
                display: none;
            }

            .hero {
                padding: 70px 7%;
            }

            .hero h1 {
                font-size: 48px;
            }

            .stats,
            .features {
                grid-template-columns: 1fr 1fr;
            }

            .bike-content {
                grid-template-columns: 1fr;
            }

            .riders {
                grid-template-columns: 1fr;
            }

            .gallery {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 600px) {

            .stats,
            .features {
                grid-template-columns: 1fr;
            }

            .stat {
                border-right: none;
                border-bottom: 1px solid #333;
                padding-bottom: 20px;
            }

            .hero h1 {
                font-size: 40px;
            }

            .section-title h2,
            .bike-info h2,
            .event h2 {
                font-size: 36px;
            }

            .event-details {
                flex-direction: column;
                gap: 20px;
            }

            .buttons {
                flex-direction: column;
            }
        }

    </style>
</head>

<body>

    <!-- NAVIGATION -->

    <nav>

        <div class="logo">
            🏔️ OFF-ROAD <span>RIDERS</span>
        </div>

        <ul>
            <li><a href="#home">HOME</a></li>
            <li><a href="#about">ABOUT</a></li>
            <li><a href="#bike">BIKES</a></li>
            <li><a href="#riders">RIDERS</a></li>
            <li><a href="#gallery">GALLERY</a></li>
        </ul>

        <a href="#event" class="nav-button">
            REGISTER
        </a>

    </nav>


    <!-- HERO -->

    <section class="hero" id="home">

        <div class="hero-content">

            <div class="small-title">
                RIDE • EXPLORE • CONNECT
            </div>

            <h1>
                OFF-ROAD<br>
                <span>BIKE EVENT</span>
            </h1>

            <p>
                Get ready for an unforgettable off-road adventure.
                Ride powerful bikes, explore challenging trails,
                and enjoy the experience with your friends.
            </p>

            <div class="buttons">

                <a href="#event" class="button">
                    REGISTER NOW →
                </a>

                <a href="#bike" class="button-dark">
                    EXPLORE BIKES
                </a>

            </div>

        </div>

    </section>


    <!-- STATS -->

    <section class="stats">

        <div class="stat">
            <h2>150+</h2>
            <p>Riders</p>
        </div>

        <div class="stat">
            <h2>50+</h2>
            <p>Off-Road Bikes</p>
        </div>

        <div class="stat">
            <h2>120 KM</h2>
            <p>Trail Distance</p>
        </div>

        <div class="stat">
            <h2>2 DAYS</h2>
            <p>Adventure</p>
        </div>

    </section>


    <!-- ABOUT -->

    <section class="section" id="about">

        <div class="section-title">

            <small>THE ADVENTURE</small>

            <h2>MORE THAN JUST A RIDE.</h2>

            <p>
                Join a community of motorcycle enthusiasts and
                experience the thrill of riding through forests,
                mountains, mud tracks and rocky trails.
            </p>

        </div>

        <div class="features">

            <div class="feature">

                <div class="icon">🏍️</div>

                <h3>Real Off-Road Trails</h3>

                <p>
                    Take on challenging mountain, forest and
                    muddy trails designed for adventure riders.
                </p>

            </div>

            <div class="feature">

                <div class="icon">👥</div>

                <h3>Ride With Friends</h3>

                <p>
                    Meet fellow riders and enjoy the adventure
                    together as a group.
                </p>

            </div>

            <div class="feature">

                <div class="icon">🛡️</div>

                <h3>Safety First</h3>

                <p>
                    Safety equipment, experienced guides and
                    support teams are available throughout the event.
                </p>

            </div>

            <div class="feature">

                <div class="icon">🏔️</div>

                <h3>Explore Nature</h3>

                <p>
                    Discover beautiful landscapes and experience
                    the outdoors from a completely different perspective.
                </p>

            </div>

        </div>

    </section>


    <!-- FEATURED BIKE -->

    <section class="section bike-section" id="bike">

        <div class="bike-content">

            <div class="bike-image">

                <img
                    src="https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=1200&q=90"
                    alt="Off Road Motorcycle">

            </div>

            <div class="bike-info">

                <small class="small-title">
                    FEATURED MACHINE
                </small>

                <h2>
                    BUILT FOR <span>ADVENTURE.</span>
                </h2>

                <p>
                    Modern off-road motorcycles are built to handle
                    difficult terrain, steep climbs, muddy trails and
                    high-speed sections while giving riders complete
                    control.
                </p>

                <div class="bike-specs">

                    <div class="spec">
                        <strong>450cc</strong>
                        <span>ENGINE</span>
                    </div>

                    <div class="spec">
                        <strong>6 SPEED</strong>
                        <span>TRANSMISSION</span>
                    </div>

                    <div class="spec">
                        <strong>110 KG</strong>
                        <span>LIGHTWEIGHT</span>
                    </div>

                    <div class="spec">
                        <strong>21"</strong>
                        <span>FRONT WHEEL</span>
                    </div>

                </div>

                <a href="#event" class="button">
                    JOIN THE EVENT
                </a>

            </div>

        </div>

    </section>


    <!-- RIDERS -->

    <section class="section" id="riders">

        <div class="section-title">

            <small>THE COMMUNITY</small>

            <h2>RIDE WITH FRIENDS.</h2>

            <p>
                Adventure becomes better when you share it
                with people who love motorcycles as much as you do.
            </p>

        </div>

        <div class="riders">

            <div class="rider">

                <img
                    src="https://images.unsplash.com/photo-1558980394-0c2f3e4f1d08?auto=format&fit=crop&w=900&q=85"
                    alt="Off Road Rider">

                <div class="rider-info">
                    <h3>Trail Riders</h3>
                    <p>Experienced off-road enthusiasts</p>
                </div>

            </div>


            <div class="rider">

                <img
                    src="https://images.unsplash.com/photo-1525160354320-d8e92641c563?auto=format&fit=crop&w=900&q=85"
                    alt="Motorcycle Rider">

                <div class="rider-info">
                    <h3>Adventure Crew</h3>
                    <p>Friends who ride together</p>
                </div>

            </div>


            <div class="rider">

                <img
                    src="https://images.unsplash.com/photo-1558981280-5e63cfae1d6b?auto=format&fit=crop&w=900&q=85"
                    alt="Motorcycle Adventure">

                <div class="rider-info">
                    <h3>Mountain Riders</h3>
                    <p>Exploring new terrain</p>
                </div>

            </div>

        </div>

    </section>


    <!-- EVENT -->

    <section class="section event" id="event">

        <div class="event-box">

            <small class="small-title">
                UPCOMING EVENT
            </small>

            <h2>
                READY TO <span>RIDE?</span>
            </h2>

            <p>
                Join us for two days of off-road riding,
                mountain trails, friends, camping and
                unforgettable motorcycle adventures.
            </p>

            <div class="event-details">

                <div class="detail">
                    <h3>📅 DATE</h3>
                    <p>November 15–16, 2026</p>
                </div>

                <div class="detail">
                    <h3>📍 LOCATION</h3>
                    <p>Coimbatore, Tamil Nadu</p>
                </div>

                <div class="detail">
                    <h3>🏁 TERRAIN</h3>
                    <p>Mountain • Forest • Mud</p>
                </div>

            </div>

            <a href="#" class="button">
                REGISTER FOR EVENT →
            </a>

        </div>

    </section>


    <!-- GALLERY -->

    <section class="section" id="gallery">

        <div class="section-title">

            <small>EVENT GALLERY</small>

            <h2>LIVE THE ADVENTURE.</h2>

        </div>

        <div class="gallery">

            <img
                src="https://images.unsplash.com/photo-1529422643029-d4585747aaf2?auto=format&fit=crop&w=900&q=85"
                alt="Motorcycle">

            <img
                src="https://images.unsplash.com/photo-1558981359-219d6364c9c8?auto=format&fit=crop&w=900&q=85"
                alt="Adventure Bike">

            <img
                src="https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=900&q=85"
                alt="Off Road Bike">

            <img
                src="https://images.unsplash.com/photo-1558980394-0c2f3e4f1d08?auto=format&fit=crop&w=900&q=85"
                alt="Rider">

            <img
                src="https://images.unsplash.com/photo-1525160354320-d8e92641c563?auto=format&fit=crop&w=900&q=85"
                alt="Bike Adventure">

            <img
                src="https://images.unsplash.com/photo-1558981280-5e63cfae1d6b?auto=format&fit=crop&w=900&q=85"
                alt="Mountain Ride">

        </div>

    </section>


    <!-- FOOTER -->

    <footer>

        <h2>
            🏔️ OFF-ROAD <span>RIDERS</span>
        </h2>

        <p>
            Ride hard. Explore more. Make memories.
        </p>

        <br>

        <p>
            © 2026 Off-Road Riders. All rights reserved.
        </p>

    </footer>


</body>
</html>
'''


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
