interface Loan {
  id: string;
  name: string;
  surname: string;
  personalId: string;
  loanAmount: number;
  term: number;
  countryCode: string;
  approved: boolean;
}

export default Loan;
