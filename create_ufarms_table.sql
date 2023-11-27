-- Create Table

CREATE TABLE Ufarms (
    UfarmID INT PRIMARY KEY AUTO_INCREMENT,
    PublicFarmID VARCHAR(12) UNIQUE,
    UserID INT,
    Name VARCHAR(255) UNIQUE,
    IsActive BOOLEAN,
    AddressStr VARCHAR(255) UNIQUE,
    Contact VARCHAR(255) UNIQUE,
    Request VARCHAR(255),
    Privacy_lat FLOAT,
    Privacy_lon FLOAT,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    -- FOREIGN KEY (UserID) REFERENCES users(UserID)

-- Insert Data
INSERT INTO Ufarms (UserID, Name, IsActive, AddressStr, Contact, Request, Privacy_lat, Privacy_lon)
VALUES
    (12, 'Shelburne Farmer Market', 1, 'Church Street, Shelburne, Chittenden County, Vermont, 05482, United States', 'info@sbpavt.com', 'vendor', 44.378, -73.2275),
    (41, 'City Market Onion River Co-op', 1, '82, South Winooski Avenue, Downtown, Burlington, Chittenden County, Vermont, 05401, United States', 'info@citymarket.coop', 'watering', 44.4773, -73.2121),
    (23, 'Intervale Community Farm', 1, '232, Intervale Road, Burlington, Chittenden County, Vermont, 05401, United States', 'info@intervalecommunityfarm.com', 'planting', 44.4911, -73.204),
    (54, 'Vermont Community Garden Network', 0, '1, Mill Street, Riverside, Burlington, Chittenden County, Vermont, 05401, United States', 'garden@vtgardens.org', 'building beds', 44.486, -73.1905),
    (1, 'My Place', 1, '102, Quarry Hill Road, South Burlington, Chittenden County, Vermont, 05403, United States', 'ehlerm42@gmail.com', 'space in garden', 44.4655, -73.1878),
    (2, 'My Old Place', 0, '406, South Union Street, South End, Burlington, Chittenden County, Vermont, 05401, United States', 'm.ehler@comcast.net', 'space in garden', 44.461, -73.2046),
    (42, 'Burlington Farmer Market', 1, '345, Pine Street, South End, Burlington, Chittenden County, Vermont, 05401, United States', 'manager@burlingtonfarmersmarket.org', 'vendor', 44.4629, -73.2156);
