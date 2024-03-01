import os
from datetime import datetime
from typing import Iterable

from sqlalchemy import create_engine, Integer, String, DateTime, select, Select, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from hvpy import DataSource

from common import DATE_FORMAT

HOSTNAME = os.environ["HOSTNAME"]

# Create connection to SQL backend.
user = os.environ["DB_USER"]
password = os.environ["DB_PASSWORD"]
dbname = os.environ["DB_NAME"]
dbhost = os.environ["DB_HOST"] if "DB_HOST" in os.environ else "localhost"
engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{dbhost}/{dbname}",
    pool_size=3,
    max_overflow=0,
    pool_recycle=3600,
)


class _Base(DeclarativeBase):
    pass


# Define the relevant portion of helioviewer's data table for use with the query builder
class DataRow(_Base):
    __tablename__ = "data"
    id: Mapped[int] = mapped_column(primary_key=True)
    filepath: Mapped[str] = mapped_column(String(255))
    filename: Mapped[str] = mapped_column(String(255))
    date: Mapped[datetime] = mapped_column(DateTime)
    sourceId: Mapped[int] = mapped_column(Integer)

    @property
    def url(self):
        return f"{HOSTNAME}{self.filepath}/{self.filename}"
    
    @property
    def path(self):
        return f"{self.filepath}/{self.filename}"

    def to_csv(self, columns: list[str]) -> str:
        # Special case when "Time" is the only parameter
        if len(columns) == 1 and columns[0] == "Time":
            return self.date.strftime(DATE_FORMAT)
        _columns = list(map(lambda x: getattr(self, x), columns))
        _columns.insert(0, self.date.strftime(DATE_FORMAT))
        return ",".join(_columns)

    def __repr__(self) -> str:
        return self.url


class HAPIDataset:
    def __init__(self, id: str) -> None:
        """
        Construct a HAPI dataset which can be used to get data from the underlying database

        Parameters
        ----------
        id: `str`
            Dataset ID
        """
        self.id = DataSource[id].value

    def _select(self, selector: any) -> Select:
        """
        Returns common select statement for this instance

        Parameters
        ----------
        selector: `any`
            Selector to pass to sqlalchemy's select.
            This could be DataRow to get all columns.
            Or it could be DataRow.<column> or DataRow["column1", "column2"] to query specific columns.
            It could also be func.min(DataRow.<column>) to apply sql functions to the select statement.
        """
        return select(selector).where(DataRow.sourceId == self.id)

    def _exec(self, stmt: Select):
        """
        Executs the given select statement

        Parameters
        ----------
        stmt: `Select`
            Select statement created with self._select
        """
        with Session(engine) as session:
            return session.execute(stmt).all()

    def GetStartDate(self) -> datetime:
        """
        Returns the date of the earliest entry in this dataset
        """
        stmt = self._select(func.min(DataRow.date))
        result = self._exec(stmt)
        assert len(result) == 1
        return result[0][0]

    def GetStopDate(self) -> datetime:
        """
        Returns the date of the newest entry in this dataset
        """
        stmt = self._select(func.max(DataRow.date))
        result = self._exec(stmt)
        assert len(result) == 1
        return result[0][0]

    def Get(self, start: datetime, stop: datetime) -> Iterable[DataRow]:
        """
        Returns all rows between the given start and stop times
        """
        stmt = (
            self._select(DataRow)
            .where(DataRow.date >= start)
            .where(DataRow.date <= stop)
            .order_by(DataRow.date.asc())
        )
        result = self._exec(stmt)
        return map(lambda row: row[0], result)
