CREATE TABLE users (
  UserID bigint NOT NULL AUTO_INCREMENT PRIMARY KEY,
  PublicID varchar(12) DEFAULT NULL UNIQUE,
  Username varchar(255) NOT NULL UNIQUE,
  Fname varchar(128) NOT NULL,
  Lname varchar(128) NOT NULL,
  _password varchar(128) NOT NULL,
  IsActive BOOLEAN DEFAULT True,
  AddressStr varchar(255) UNIQUE,
  Email varchar(255) UNIQUE,
  Host BOOLEAN DEFAULT False,
  Bio varchar(255),
  CreatedAt datetime DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- test insert
-- INSERT INTO users (Name, AddressStr, Email, Bio)
-- VALUES ('John Doe', '123 Main St, Burlington, VT', 'john.doe@example.com', 'A short bio about John Doe');
