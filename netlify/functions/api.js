const express = require('express');
const serverless = require('serverless-http');
const app = express();

app.use(express.json());

// Import delle route
const authRoutes = require('../../../routes/auth');
const miningRoutes = require('../../../routes/mining');
const apiRoutes = require('../../../routes/api');

// Registrazione delle route
app.use('/.netlify/functions/api', authRoutes);
app.use('/.netlify/functions/api', miningRoutes);
app.use('/.netlify/functions/api', apiRoutes);

// Handler per gli errori
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal Server Error' });
});

// Esporta l'handler per le funzioni Netlify
module.exports.handler = serverless(app);
