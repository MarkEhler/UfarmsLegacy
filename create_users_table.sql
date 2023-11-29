CREATE TABLE users (
  UserID bigint NOT NULL AUTO_INCREMENT PRIMARY KEY,
  PublicID varchar(12) DEFAULT NULL UNIQUE,
  Name varchar(255) NOT NULL UNIQUE,
  IsActive BOOLEAN DEFAULT True,
  AddressStr varchar(255) UNIQUE,
  Email varchar(255) UNIQUE,
  Host BOOLEAN DEFAULT False,
  Bio varchar(255),
  CreatedAt datetime DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


INSERT INTO users (Name, AddressStr, Email, Bio)
VALUES ('John Doe', '123 Main St, Burlington, VT', 'john.doe@example.com', 'A short bio about John Doe');
