import express, { Request, Response } from 'express';
import getUUID from '../utils/getUUID';
import Loan from '../models/loan';
import data from '../data/loans';

const router = express.Router();

const blacklist = [
  '0123456789',
  '0987654321'
]

router.post("/apply", (req: Request, res: Response) => {
  const {
    term,
    name,
    surname,
    personalId,
    loanAmount,
    countryCode = "GB",
  } = req.body;

  if([name, surname, personalId, loanAmount, term].some(field => !field)) {
    res.status(400).send({ message: 'Missing required fields.' });
  }

  if(blacklist.includes(personalId)) {
    res.status(403).send({ message: 'Specified personal ID is blacklisted.'});
  }

  const newLoan: Loan = {
    id: getUUID(),
    name,
    surname,
    personalId,
    loanAmount,
    term,
    countryCode,
    approved: false,
  };

  data.push(newLoan);
  res.status(201).send({ message: "Loan application submitted", loan: newLoan });

});

router.get('/all', (req: Request, res: Response) => {
  const approvedLoans = data.filter((loan) => loan.approved);
  res.status(200).send(approvedLoans);
});

router.get('/user/:personalId', (req: Request, res: Response) => {
  const persId = req.params.personalId;
  const userLoans = data.filter((loan) => loan.personalId === persId && loan.approved);

  if(userLoans.length === 0) {
    res.status(404).send({ error: "This personalId does not have any approved loans" });
  }

  res.status(200).send(userLoans);
});

export default router;
