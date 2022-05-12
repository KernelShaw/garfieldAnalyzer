import pygsheets


def drive_update(index, joke, laugh_bool):
    cell_conversion = joke + str(index + 2)
    if laugh_bool is None:
        update_the_master_sheet(cell_conversion)
    else:
        update_the_master_sheet(cell_conversion, "N" + str(index + 2))
    return


def update_the_master_sheet(cell, laugh=None):
    # authorization
    google_client = pygsheets.authorize(service_file='static/pvt/gardata-test-f05cbfa3dde5.json')
    master_sheet = google_client.open('TestSheet')
    data_sheet = master_sheet[0]

    if laugh is not None:
        data_sheet.update_value(laugh, int(data_sheet.get_value(cell, 'UNFORMATTED_VALUE')) + 1)

    data_sheet.update_value(cell, int(data_sheet.get_value(cell, 'UNFORMATTED_VALUE')) + 1)
