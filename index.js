import express from 'express';

const app = express();
const PORT = process.env.PORT || 3000;

app.get('/auth/me', (req, res) => {
  res.json({ status: 'Hello World' });
});

app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});
