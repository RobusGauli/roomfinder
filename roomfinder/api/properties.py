from roomfinder.api import api


@api.route('/home', methods=['GET'])
def home():
    print('thisis called')
    return 'this is ome'

