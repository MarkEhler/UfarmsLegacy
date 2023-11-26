CREATE TABLE Ufarms (
  `UfarmID` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `PublicFarmID` varchar(12) DEFAULT NULL,
  `UserID` INT,  ##Fkey
  `Name` VARCHAR(255),
  `Host` BOOLEAN,
  `IsActive` BOOLEAN,
  `AddressStr` VARCHAR(255),
  `Contact` VARCHAR(255),
  `Request` VARCHAR(255),
  `Privacy_lat` FLOAT DEFAULT NULL,
  `Privacy_lon` FLOAT DEFAULT NULL,
  `CreatedAt` datetime(6) NOT NULL,
  `UpdatedAt` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

## FOREIGN KEY (UserID) REFERENCES Users(UserID)

