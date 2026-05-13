from openrgb import OpenRGBClient
from openrgb.utils import DeviceType, RGBColor


def main():
    print("Open RGB script starting")
    client = OpenRGBClient()

    my_ram = client.get_devices_by_type(DeviceType.DRAM)
    my_motherboard = client.get_devices_by_type(DeviceType.MOTHERBOARD)

    color = RGBColor(0, 0, 0)

    for i in my_ram:
        i.set_color(color)

    my_motherboard[0].set_color(color)


if __name__ == "__main__":
    main()
