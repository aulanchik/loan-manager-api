import express from 'express';
import helmet from 'helmet';
import morgan from 'morgan';
import loanRouter from './routes/loan';

const app = express();

app.use(helmet());
app.use(morgan('dev'));
app.use(express.json());
app.use('/api/loans', loanRouter);

export default app;
