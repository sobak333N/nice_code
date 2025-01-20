CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    balance NUMERIC
);

INSERT INTO accounts (balance) VALUES (1000), (2000), (3000);
