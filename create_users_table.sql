CREATE TABLE Users (
  `UserID` bigint NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `PublicID` varchar(12) DEFAULT NULL,
  `Name` varchar(255) NOT NULL,
  `IsActive` BOOLEAN DEFAULT True,
  `Bio` varchar(255) DEFAULT NULL,
  `CreatedAt` datetime(6) NOT NULL,
  `UpdatedAt` datetime(6) NOT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `idx_public_id` (`PublicID`),
  `Email` VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;