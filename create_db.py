from sqlalchemy import create_engine, Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date

# Create SQLite database
DATABASE_URL = "sqlite:///./Housekeeping.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# -------------------
# Tables
# -------------------


class Cabin(Base):
    __tablename__ = "Cabins"

    Name = Column(String, primary_key=True)  # unique identifier
    Status = Column(String) #which will be "Clean", "Dirty", "Occupied", "Winterized"
    NumQueen = Column(Integer)
    NumFull = Column(Integer)
    NumTwin = Column(Integer)
    NextBooking = Column(Date)
    NextGuest = Column(String)


class Booking(Base):
    __tablename__ = "Bookings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    CabinName = Column(String, ForeignKey("Cabins.Name"))
    Guest = Column(String)
    StartDate = Column(Date)
    EndDate = Column(Date)

cabins = [
    Cabin(
        Name='Wellspring',
        Status = 'dirty',
        NumQueen=2,
        NumFull=0,
        NumTwin=6,
        NextBooking = date(2026, 3, 12),
        NextGuest = "Rob Ribbe"
    ),
    Cabin(
        Name='Kenozha',
        Status = 'clean',
        NumQueen=1,
        NumFull=2,
        NumTwin=3,
        NextBooking = date(2026, 4, 13),
        NextGuest = "Charlie Goeke"
    ),
    Cabin(
        Name='Living Waters',
        Status = 'in-use',
        NumQueen=2,
        NumFull=0,
        NumTwin=4,
        NextBooking = date.today()
    ),
    Cabin(
        Name='Engedi',
        NumQueen=1,
        NumFull=0,
        NumTwin=3
    ),
    Cabin(
        Name='WPL_101',
        NumQueen=1,
        NumFull=0,
        NumTwin=0
    ),
    Cabin(
        Name='WPL_102',
        NumQueen=0,
        NumFull=0,
        NumTwin=2
    ),
    Cabin(
        Name='WPL_103',
        NumQueen=1,
        NumFull=0,
        NumTwin=0
    ),
    Cabin(
        Name='WPL_104',
        NumQueen=1,
        NumFull=0,
        NumTwin=0
    )
]

if __name__ == "__main__":
    # -------------------
    # Create tables
    # -------------------

    Base.metadata.create_all(bind=engine)

    # -------------------
    # Insert sample data
    # -------------------

    db = SessionLocal()



    db.add_all(cabins)

    # Add bookings
    # booking1 = Booking(
    #     CabinName="CabinA",
    #     StartDate=date(2026, 3, 12),
    #     EndDate=date(2026, 3, 15)
    # )

    # booking2 = Booking(
    #     CabinName="CabinB",
    #     StartDate=date(2026, 3, 13),
    #     EndDate=date(2026, 3, 20)
    # )

    # db.add_all([booking1, booking2])

    db.commit()
    db.close()

    print("Database and sample data created!")