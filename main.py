from openrgb import OpenRGBClient

from computer import Computer


def main():
    print("Open RGB script starting")
    client = OpenRGBClient()

    print(client.devices)

    Computer()

if __name__ == "__main__":
    main()
