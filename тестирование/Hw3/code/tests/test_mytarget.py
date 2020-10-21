from datetime import datetime
import pytest
from tests.base import BaseCase


class TestMyTarget(BaseCase):

    @pytest.mark.api
    def test_delete_segment(self):
        name_of_segment = 'Сегмент для удаления'
        self.target_client.create_segment(name_of_segment)
        self.target_client.delete_segment(name_of_segment)
        assert not self.target_client.check_segment_existence(name_of_segment)

    @pytest.mark.api
    def test_create_segment(self):
        time_now = datetime.now()
        name_of_segment_to_create = time_now
        self.target_client.create_segment(name_of_segment_to_create)
        assert self.target_client.check_segment_existence(name_of_segment_to_create)
