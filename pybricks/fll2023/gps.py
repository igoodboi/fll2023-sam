from pybricks.hubs import PrimeHub


class Gps:
    # class member
    gps = None
    hub = None

    def __init__(self, hub: PrimeHub):
        self.hub = hub

    @classmethod
    def init(cls, hub: PrimeHub = None):
        if not cls.gps:
            if not hub:
                raise ValueError(f'Argument Error: hub is null. Please pass in a non-null hub')
            cls.gps = cls(hub)
            cls.hub = hub

    @classmethod
    def heading(cls):
        return cls.hub.imu.heading()

    @classmethod
    def coord(cls):
        # TODO
        return 0, 0


if __name__ == '__main__':
    from pybricks.hubs import PrimeHub

    try:
        Gps.init()
        assert ValueError()
    except:
        pass

    hub = PrimeHub()
    Gps.init(hub)
    assert Gps.hub == hub
    assert Gps.gps != Gps(hub)
    hub2 = PrimeHub()

    # No op
    Gps.init()
    assert Gps.hub == hub
    print('done!')