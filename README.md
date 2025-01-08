## Loan Manager Restful Application
### Problem definition

Create a tiny RESTful web service with the following business requirements:

Application must expose REST API endpoints for the following functionality:
* apply for loan (loan amount, term, name, surname and personal id must be provided)
 - list all approved loans
 - list all approved loans by user

Service must perform loan application validation according to the following rules and reject application if:
 - Application comes from blacklisted `personalId`
 - N application / second are received from a single country (essentially we want to limit number of loan applications coming from a country in a given timeframe)

### Note ###
Service must perform origin country resolution using a web service and store country code together with the loan application. Because network is unreliable and services tend to fail, let's agree on default country code that is defined via configuration file or variable.
