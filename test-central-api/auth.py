from authup.domains.robot.api import RobotAPI
from authup.domains.robot.types import Robot, RobotCreate

# from hub_python_client import MasterImageAPI

from authup.domains.base_api import AuthupClient
from authup.domains.realm.api import RealmAPI
from authup.domains.realm.types import Realm
import unittest
import os
from dotenv import load_dotenv
import pytest


class TestAuhup(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        load_dotenv()
        self.client = AuthupClient(
            authup_url=os.getenv('AUTHUP_URL'),
            username=os.getenv('AUTHUP_USERNAME'),
            password=os.getenv('AUTHUP_PASSWORD'),
        )

    @pytest.mark.asyncio
    async def test_authup(self):
        realm_client = RealmAPI(Realm, self.client.http, prefix='realms')
        realms = await realm_client.get_many()
        master_realm = realms[0]
        print(master_realm)

        robot_client = RobotAPI(Robot, self.client.http, prefix='robots')
        #robot = await robot_client.create(RobotCreate(name=os.urandom(8).hex(), secret="test", realm_id=master_realm.id))
        robots = await robot_client.get_many()

        print(len(robots))
        robot = robots[1]
        print(robot.name)
        print(robot.secret)
        print(robot.realm)
        
        assert isinstance(robot, Robot)
        self.assertIsNotNone(master_realm)


if __name__ == '__main__':
    unittest.main()




