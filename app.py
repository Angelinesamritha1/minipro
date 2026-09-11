
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
            m

