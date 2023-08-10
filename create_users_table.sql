CREATE TABLE Users (
  UserID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  CollectorID INT,
  StartDate DATETIME,
  Email VARCHAR(255),
  # host 1 if they said yes to hosting land 0 if NOT
);

## Ufarms