const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send('Hi there dcc class: Bismuth!');
});

app.listen(8081, () => {
    console.log('Server listening on port 8081');
});