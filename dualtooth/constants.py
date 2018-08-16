PATHS = {
    'btle': 'ControlSet001\Services\BTHPORT\Parameters',
}
MAXDEPTH=6
ATTRS = (
    ('Name', 'Name'),
    ('VIDType', 'Source'),
    ('VID', 'Vendor'),
    ('PID', 'Product'),
    ('Version', 'Version'),
)
ATTRS_BLE = (
    ('LEFlags', 'is_LE'),
    ('LEAddressType', 'AddressType'),
    ('LEAppearance', 'Appearance'),
)
