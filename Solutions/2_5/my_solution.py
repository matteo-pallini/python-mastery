from collections.abc import Sequence
from datetime import date


class RideData(Sequence):
    def __init__(self):
        # Each value is a list with all of the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, key):
        if isinstance(key, slice):
            rides = RideData()
            rides.routes = list(self.routes[key])
            rides.dates = list(self.dates[key])
            rides.daytypes = list(self.daytypes[key])
            rides.numrides = list(self.numrides[key])
            return rides
        else:
            return {
                 'route': self.routes[key],
                 'date': self.dates[key],
                 'daytype': self.daytypes[key],
                 'rides': self.numrides[key]
                 }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

    def __str__(self) -> str:
        vals = [str(self[idx]) for idx in range(len(self))]
        return ",\n".join(vals)

    def __repr__(self):
        return f"RideData({str(self)})"

def create_ride(route, date, daytype, rides):
    return {
        "route": route,
        "date": date,
        "daytype": daytype,
        "rides": rides
            }


def run():
    ride = RideData()
    ride.append(create_ride("a", date(2020, 1, 1), "m", 2))
    ride.append(create_ride("b", date(2020, 1, 1), "m", 4))
    ride.append(create_ride("a", date(2020, 10, 1), "w", 2))
    ride.append(create_ride("c", date(2020, 7, 1), "t", 1))
    print(ride)
    print(f"\n slice 1:3 --> \n {ride[1:3]}")


run()


if __name__ == "__main__":
    run()
