import os
from google.protobuf.json_format import MessageToJson
import olympics_pb2


def main():
    athlete = olympics_pb2.Athlete()
    athlete.id = 1
    athlete.name = "Rebeca Andrade"
    athlete.country = "Brazil"
    athlete.sport = "Artistic gymnastics"
    medal = athlete.medals.add()
    medal.type = olympics_pb2.Medal.GOLD
    medal.event = "Women's Floor"
    medal.year = 2024

    with open("olympics.bin", "wb") as f:
        f.write(athlete.SerializeToString())

    with open("olympics.bin", "rb") as f:
        athlete = olympics_pb2.Athlete()
        athlete.ParseFromString(f.read())

    with open("olympics.json", "w", encoding="utf-8") as f:
        f.write(MessageToJson(athlete))

    # compare the size of the binary and JSON files
    print(f"Size of binary file: {os.path.getsize('olympics.bin')} bytes")
    print(f"Size of JSON file: {os.path.getsize('olympics.json')} bytes")


if __name__ == "__main__":
    main()
