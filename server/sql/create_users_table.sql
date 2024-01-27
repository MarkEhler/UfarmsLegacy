CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    PublicID VARCHAR(12) DEFAULT NULL UNIQUE,
    Username VARCHAR(30) UNIQUE,
    Fname VARCHAR(30),
    Lname VARCHAR(30),
    password VARCHAR(128) NOT NULL,
    IsActive BOOLEAN DEFAULT TRUE,
    AddressStr VARCHAR(255) UNIQUE,
    Email VARCHAR(255) UNIQUE,
    Bio VARCHAR(255),
    IsHost BOOLEAN DEFAULT FALSE,
    IsAdmin BOOLEAN DEFAULT FALSE,
    ProfilePic VARBINARY(MAX), --findme method 2
    Carrots INT DEFAULT 3,
    Exp INT DEFAULT 3,
    StripeID VARCHAR(25) UNIQUE,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


-- properties to work on -- 
-- badges are filled automatically once a badge is earned the user is sent an email and a badge is added to their list of badges
-- gender is offered as 3/4 options in the welcome route
-- some user data should be collected upon signup:
-- self rated experience, what they're looking for, their intrests, and their reason for joining Uf -- look to dating sites for their intake process

