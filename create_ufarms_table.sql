CREATE TABLE Ufarms (
  UfarmID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  UserID INT,
  Name VARCHAR(255),
  Host BOOLEAN,
  IsActive BOOLEAN,
  AddressStr VARCHAR(255),
  Contact VARCHAR(255),
  Request VARCHAR(255)
  Privacy_lat FLOAT,
  Privacy_lon FLOAT
  KEY UserID (UserID)
);

## FOREIGN KEY (UserID) REFERENCES Users(UserID)

