import psycopg2
from accounts.models.address import Address


class AddressRepository():
    def insert(self, address: Address) -> Address:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO address 
                        (Address, City, State, ZipCode) VALUES
                        (%(address)s, %(city)s, %(state)s, %(zip_code)s)
                        RETURNING id
                    """, {
                    'address': address.address,
                    'city': address.city,
                    'state': address.state,
                    'zip_code': address.zip_code
                }
                )
                address.id = cursor.fetchone()[0]
        return address

    def get_by_id(self, id) -> Address:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, Address, City, State, ZipCode FROM 
                        address WHERE ID=%(address_id)s
                    """, {
                    'address_id': id
                }
                )
                row = cursor.fetchone()
        # In a larger enterprise app, you would likely be using an ORM like
        # SQLAlchemy, which would handle the mapping of the database row to the object
        # (and its hierarchy) automatically. The other approach you could take is to
        # use a separate set of DTOs (Data Transfer Objects) and manage mapping between
        # the DTO and the Pydantic model.
        return Address.construct(id=row[0], address=row[1], city=row[2], state=row[3], zip_code=row[4])

    def delete(self, id) -> None:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM address WHERE ID=%(address_id)s
                    """, {
                    'address_id': id
                }
                )
