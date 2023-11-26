CREATE TABLE users (
  UserID bigint NOT NULL AUTO_INCREMENT PRIMARY KEY,
  PublicID varchar(12) DEFAULT NULL UNIQUE,
  Name varchar(255) NOT NULL UNIQUE,
  IsActive BOOLEAN DEFAULT True,
  AddressStr varchar(255) UNIQUE,
  Contact varchar(255) UNIQUE,
  Host BOOLEAN DEFAULT False,
  Bio varchar(255),
  CreatedAt datetime DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
