
CREATE TABLE Buyer(
    buyerFirstName VARCHAR(20) NOT NULL,
    buyerLastName VARCHAR(20) NOT NULL,
    buyerPhone VARCHAR(20) PRIMARY KEY
);

CREATE TABLE Artist(
    artistFirstName VARCHAR(20) NOT NULL,
    artistLastName VARCHAR(20) NOT NULL,
    artistId VARCHAR(20) PRIMARY KEY,
    artistPhone VARCHAR(20) NOT NULL,
    artistAge INT
);

CREATE TABLE Exhibition(
    exhibitionTitle VARCHAR(20) PRIMARY KEY,
    exhibitionDateOfStart DATE NOT NULL,
    exhibitionDateOfEnd DATE NOT NULL
);

CREATE TABLE Art(
    artTitle VARCHAR(20),
    artInfo VARCHAR(255) DEFAULT 'No Description was Entered!',
    artCategory VARCHAR(20) CHECK(artCategory IN ('photo','painting','sculpture')),
    artArtist VARCHAR(20),
    artExhibition VARCHAR(20),
    artPrice INT CHECK(artPrice >= 1000),
    PRIMARY KEY (artTitle,artPrice),
    FOREIGN KEY (artArtist) REFERENCES Artist(artistId),
    FOREIGN KEY (artExhibition) REFERENCES Exhibition(exhibitionTitle)
);

CREATE TABLE Auction(
    auctionExhibition VARCHAR(20),
    auctionDate DATE NOT NULL,
    PRIMARY KEY (auctionExhibition, auctionDate),
    FOREIGN KEY (auctionExhibition) REFERENCES Exhibition(exhibitionTitle)
);

CREATE TABLE factor(
    buyer VARCHAR(20),
    artist VARCHAR(20),
    exhibition VARCHAR(20),
    factorDate DATE,
    suggestedPrice INT  CHECK(suggestedPrice >= 1000),
    PRIMARY KEY (buyer, artist),
    FOREIGN KEY (buyer) REFERENCES Buyer(buyerPhone),
    FOREIGN KEY (artist) REFERENCES Artist(artistId),
    FOREIGN KEY (exhibition) REFERENCES Auction(auctionExhibition)
);
