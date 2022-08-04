from utils.utils import *

import pytest
import json

@pytest.mark.gen3
@pytest.mark.dependency()
def test_get_all_applications(be_byos):
    response = be_byos.be_byos_get_all_application()
    print_response(response=response)
    assert response.status_code == 200
    json_response = json.loads(response.text)
    assert 'page' in json_response


