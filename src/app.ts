import express from 'express';
import helmet from 'helmet';
import morgan from 'morgan';

const app = express();

app.use(helmet());
app.use(morgan('dev'));

app.get('/', (req, res) => {
    res.send('Lorem ipsum');
});

export default app;
