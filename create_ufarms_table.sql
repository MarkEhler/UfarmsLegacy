CREATE TABLE Ufarms (
  UfarmID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  UserID INT,
  Name VARCHAR(255),
  Host Boolean,
  IsActive Boolean,
  AddressStr, VARCHAR(255)
  Contact VARCHAR(255),
  Request VARCHAR(255),
  REFERENCES Users(UserID)
);