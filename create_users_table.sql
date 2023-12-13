CREATE TABLE Users (
  UserID bigint NOT NULL AUTO_INCREMENT PRIMARY KEY,
  PublicID varchar(12) DEFAULT NULL UNIQUE,
  Username varchar(255) NOT NULL UNIQUE,
  Fname varchar(128) DEFAULT NULL,
  Lname varchar(128) DEFAULT NULL,
  Gender varchar(12),
  password varchar(128) NOT NULL,
  IsActive BOOLEAN DEFAULT True,
  AddressStr varchar(255) UNIQUE,
  Email varchar(255) UNIQUE,
  Badges varchar(255) DEFAULT NULL,
  IsHost BOOLEAN DEFAULT False,
  Bio varchar(255),
  IsAdmin BOOLEAN DEFAULT False,
  ProfilePic varchar(255),
  CreatedAt datetime DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- properties to work on -- 
-- badges are filled automatically once a badge is earned the user is sent an email and a badge is added to their list of badges
-- gender is offered as 3/4 options in the welcome route
-- some user data should be collected upon signup:
-- self rated experience, what they're looking for, their intrests, and their reason for joining Uf -- look to dating sites for their intake process

