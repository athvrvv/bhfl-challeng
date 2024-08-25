const express = require('express');
const app = express();

app.use(express.json());

app.post('/bfhl', (req, res) => {
    const data = req.body.data || [];
    const numbers = data.filter(x => /^\d+$/.test(x));
    const alphabets = data.filter(x => /^[A-Za-z]+$/.test(x));
    const highestLowercase = alphabets.filter(x => /^[a-z]+$/.test(x)).sort().pop();

    res.json({
        is_success: true,
        user_id: "john_doe_17091999",
        email: "john@xyz.com",
        roll_number: "ABCD123",
        numbers: numbers,
        alphabets: alphabets,
        highest_lowercase_alphabet: highestLowercase ? [highestLowercase] : []
    });
});

app.get('/bfhl', (req, res) => {
    res.json({ operation_code: 1 });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
