import pygsheets


def drive_update(index, joke):
    cell_conversion = joke + str(index + 2)
    update_the_master_sheet(cell_conversion)
    return


def update_the_master_sheet(cell, laugh=False):
    # authorization
    google_client = pygsheets.authorize(service_file='static/pvt/gardata-test-f05cbfa3dde5.json')
    master_sheet = google_client.open('TestSheet')
    data_sheet = master_sheet[0]

    laugh_counter_column = 'N'

    data_sheet.update_value(cell, int(data_sheet.get_value(cell, 'UNFORMATTED_VALUE')) + 1)
