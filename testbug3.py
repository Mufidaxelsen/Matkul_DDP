<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Tester JavaScript</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }

        #box {
            width: 200px;
            height: 200px;
            background: steelblue;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            transition: 0.3s;
            margin-bottom: 20px;
        }

        button {
            padding: 10px 15px;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <div id="box">Kotak</div>

    <button onclick="ubahWarna()">Ubah Warna</button>
    <button onclick="ubahUkuran()">Ubah Ukuran</button>
    <button onclick="resetBox()">Reset</button>

    <script>
        const box = document.getElementById('box');

        function randomColor() {
            return '#' + Math.floor(Ma
